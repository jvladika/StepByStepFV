import backoff  # for exponential backoff
import openai
import spacy_dbpedia_spotlight
import spacy
import pickle

from enums.reasoning import ReasoningEnum
from mixtral import prompt, login
import rdflib
from rdflib import Graph, URIRef
from qafv_model.gpt3_template import GPT3_Template
from qafv_model.kggpt_template import KGGPT_Template
from qafv_model.question_answering import GPT3_T5_Question_Answering


@backoff.on_exception(backoff.expo, openai.error.RateLimitError)
def completions_with_backoff(**kwargs):
    return openai.Completion.create(**kwargs)


@backoff.on_exception(backoff.expo, openai.error.RateLimitError)
def chat_completions_with_backoff(**kwargs):
    return openai.ChatCompletion.create(**kwargs)


class GPT3_T5_Question_Answering_KGGPT(GPT3_T5_Question_Answering):
    def __init__(self, API_KEY, model_name, hugging_face_email) -> None:
        self.API_KEY = API_KEY
        self.model_name = model_name
        openai.api_key = API_KEY
        self.gpt3_template = KGGPT_Template()

        if hugging_face_email:
            self.chat = login(hugging_face_email)

        self.nlp = spacy.blank('en')
        self.nlp.add_pipe('dbpedia_spotlight')

        file = open("qafv_model/relations_for_final.pickle", 'rb')
        self.relations_final_list = pickle.load(file)

    # used for chat-gpt and gpt-4
    def generate(self, input_string, max_token):
        if self.model_name in [ReasoningEnum.GPT_4, ReasoningEnum.GPT_3_5]:
            response = chat_completions_with_backoff(
                model=self.model_name,
                messages=[
                    {"role": "user", "content": input_string}
                ],
                max_tokens=64,
                temperature=0.01,
                top_p=1.0,
                frequency_penalty=0.0,
                presence_penalty=0.0
            )
            generated_text = response['choices'][0]['message']['content'].strip()

        elif self.model_name in [ReasoningEnum.MIXTRAL]:
            generated_text = prompt(self.chat, input_string, web=False)

        return generated_text

    def answer_question(self, question):

        doc = self.nlp(question)
        entities = [(ent.text, ent.kb_id_, ent._.dbpedia_raw_result['@similarityScore']) for ent in doc.ents]
        entities = [e[1] for e in entities]
        print(f"entities from spotlight: {entities}")


        example = (f"From a given sentence, find named entities within the sentence and return only its DBpedia URI. \n"
                   f" Write only the URI.\n"
                   f"Sentence: {question}")

        llm_entities = [line.strip() for line in self.generate(example, max_token=64).splitlines()]

        print(f"entities from llm: {llm_entities}")

        entities = entities + llm_entities
        entities = set(entities)

        g = Graph()
        valid_entities = []
        for e in entities:
            print(e)
            try:
                g.parse(e)
                valid_entities.append(e)
            except Exception as ex:
                print(f"coudl not parse: {e}")
                continue

            aliases = list(g.triples((URIRef(e), URIRef('http://dbpedia.org/ontology/wikiPageRedirects'), None)))
            for a in aliases:
                print(f"retrieved alias: {a[2]}")
                g.parse(str(a[2]))
                valid_entities.append(str(a[2]))

        entities = valid_entities
        tuples = []
        if len(entities) >= 2:
            # retrieve direct relations between the entities
            for e in entities:
                for f in entities:
                    if e == f:
                        continue

                    tuples = tuples + list(
                        g.triples((URIRef(e), None, URIRef(f))))

            if len(tuples) == 0:
                tuples = list(g)

        elif len(entities) == 1:
            tuples = list(g)

        parsed_tuples = []
        for tuple in tuples:
            subject = tuple[0].split("/")[-1]
            predicate = tuple[1].split("/")[-1]
            if type(tuple[2]) == rdflib.term.Literal:
                obj = tuple[2].value
            else:
                obj = tuple[2].split("/")[-1]

            if predicate not in self.relations_final_list:
                continue
            else:
                parsed_tuples.append((subject, predicate, obj))

        print(parsed_tuples)
        relation_candidates = set([tuple[1] for tuple in parsed_tuples])
        print(relation_candidates)
        example = self.gpt3_template.fill_RR_template(question, relation_candidates)
        relation = self.generate(example, max_token=32)
        print(f"retrieved relation: {relation}")
        if relation == "[]":
            evidence = "No evidence could be found."
            selected_tuples = []
        else:
            selected_tuples = []
            for tuple in parsed_tuples:
                if tuple[1] == relation:
                    selected_tuples.append(tuple)

            # input_string = f'Generate a sentence from this subject-predicate-object tuple: {str(selected_tuples)}'
            input_string = self.gpt3_template.fill_triples_to_sentence_template(selected_tuples)
            evidence = self.generate(input_string, max_token=128)

        example = (
            f'Given the evidence, answer the following question. If no evidence could be found, answer in a negative way.\n'
            f'Evidence: {evidence}\n'
            f'Question: {question}\n'
            f'The answer is:')
        answer_text = self.generate(example, max_token=64)

        return {
            "answer_text": answer_text,
            "rationale": evidence,
            "retrieved_tuples": selected_tuples,
            "entities": entities,
            "relation_candidates": relation_candidates
        }
