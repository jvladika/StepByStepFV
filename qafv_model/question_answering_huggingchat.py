import os
import time
import backoff  # for exponential backoff
import openai
# import tldextract
from qafv_model.gpt3_template import GPT3_Template
from qafv_model.question_answering import GPT3_T5_Question_Answering
from dotenv import load_dotenv
from mixtral import login, prompt

load_dotenv()


@backoff.on_exception(backoff.expo, openai.error.RateLimitError)
def completions_with_backoff(**kwargs):
    return openai.Completion.create(**kwargs)


@backoff.on_exception(backoff.expo, openai.error.RateLimitError)
def chat_completions_with_backoff(**kwargs):
    return openai.ChatCompletion.create(**kwargs)


class GPT3_T5_Question_Answering_Huggingchat(GPT3_T5_Question_Answering):
    def __init__(self, API_KEY, model_name, hugging_face_email):
        print("qa huggingchat")
        self.chatbot = login(hugging_face_email)

        super().__init__(API_KEY, model_name, hugging_face_email)

    def retrieve_evidence(self, question):
        time.sleep(12)

        i = 0
        while i < 5:
            i = i + 1
            try:
                print(question)
                query_result = prompt(self.chatbot,
                                      question + "Please be concise. Use only the web search results for your answer. Answer with a whole sentence. Disregard the previous questions.",
                                      web=True)

                evidence = query_result.text + "\nRetrieved from: "
                print(evidence)
            except Exception as e:
                if "Server returns an error: This conversation has more than 500 messages. Start a new one to continue" in str(e):
                    self.chatbot.new_conversation(switch_to=True)

                print(f"Huggingchat exception: {e}")
                print(f"Question: {question}")
                time.sleep(5)
                continue

            for source in query_result.web_search_sources:
                evidence = evidence + " " + source.link

            return evidence

        raise Exception("Exceeded 5 tries")
