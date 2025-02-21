from time import sleep

import backoff  # for exponential backoff
import openai
import random

from enums.reasoning import ReasoningEnum
from mixtral import login, prompt

from .gpt3_template import GPT3_Template

@backoff.on_exception(backoff.expo, openai.error.RateLimitError)
def completions_with_backoff(**kwargs):
    return openai.Completion.create(**kwargs)

@backoff.on_exception(backoff.expo, openai.error.RateLimitError)
def chat_completions_with_backoff(**kwargs):
    return openai.ChatCompletion.create(**kwargs)

class Fact_Reasoner:
    def __init__(self, API_KEY, model_name, hugging_face_email) -> None:
        self.API_KEY = API_KEY
        self.model_name = model_name

        self.gpt3_template = GPT3_Template()

        self.chat = "chat"

        if hugging_face_email:
            #self.chat = login(hugging_face_email)
            self.chat = "chat"

    # used for chat-gpt and gpt-4
    def generate(self, input_string, max_token):
        if self.model_name in [ReasoningEnum.GPT_4, ReasoningEnum.GPT_3_5]:
            print("reasoner")
            openai.api_key = self.API_KEY
            if self.model_name == ReasoningEnum.MIXTRAL:
                openai.api_base = "https://api.llama-api.com"

            while True:
                try:
                    response = chat_completions_with_backoff(
                        model=self.model_name,
                        messages=[
                            {"role": "user", "content": input_string}
                        ],
                        max_tokens=max_token,
                        temperature=0.01,
                        top_p=1.0,
                        frequency_penalty=0.0,
                        presence_penalty=0.0
                    )
                    break
                except Exception as e:
                    print(e)
                    sleep(10)
                    continue

            generated_text = response['choices'][0]['message']['content'].strip()

        elif self.model_name in [ReasoningEnum.MIXTRAL]:
            generated_text = prompt(self.chat, input_string, web=False)

        return generated_text

    def claim_verification(self, claim, qa_contexts):
        qa_contexts_txt = ''
        for ques, ans in qa_contexts:
            qa_contexts_txt += f'Q: {ques}\nA: {ans}\n'
        
        # template = f'''Based on the above information, is it true that {claim[:-1]}? \n Options: (A) True (B) False (C) Impossible to tell \n A: Let's think step by step.'''
        template = f'''Based on the above information, is it true that {claim[:-1]}? True, false, or neither? Please also state the confidence level of your answer as a percentage. \n A: Let's think step by step.'''
        example = f'{qa_contexts_txt}\n{template}'.strip()

        out = self.generate(example, max_token = 256)
        return out

    def map_prediction(self, prediction):
        prediction = prediction.lower().strip()
        refutes_indicator = ["no", "false", "refuted"]
        supports_indicator = ["yes", "true", "supported"]

        for indicator in supports_indicator:
            if prediction.find(indicator) >= 0:
                return 'supports'
        
        for indicator in refutes_indicator:
            if prediction.find(indicator) >= 0:
                return 'refutes'

        print("using random prediction")
        return random.sample(['supports', 'refutes'], 1)[0]

    # A more stable claim verification that first list all evidence gathered and then do chain-of-thoughts
    def CoT_claim_verification(self, claim, qa_contexts):
        # convert each q-a pair into a statement
        statements = []
        for ques, ans in qa_contexts:
            example = f'''Question = {ques}\nAnswer = {ans}\n Convert the above question-answer pair into a statement. Please do not any additional information, but only summarize the provided answer.'''
            statement = self.generate(example, max_token = 64)
            statements.append(statement)
        evidence = ' '.join(statements)
        
        # verify the claim with CoT
        template = f'''{claim} Is this claim true or false based on evidence? \n\n Answer: {evidence} \n Therefore, the final answer is: '''
        prediction = self.generate(template, max_token = 32)


        # get the final label
        label = self.map_prediction(prediction)
        label_map = {'supports': 'True', 'refutes': 'False'}
        label_str = label_map[label]
        explanation = f'{evidence} Therefore, the final answer is: {label_str}.'
        return explanation

    def is_information_sufficient(self, claim, qa_contexts):
        def map_text_to_label(raw_text):
            indicators = ['yes']
            for indicator in indicators:
                if raw_text.lower().find(indicator) >= 0:
                    return True
            return False

        example = self.gpt3_template.fill_can_we_step_question(claim, qa_contexts)
        raw_output = self.generate(example, max_token = 32)
        prediction = map_text_to_label(raw_output)
        return prediction