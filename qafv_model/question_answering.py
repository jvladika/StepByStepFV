import backoff  # for exponential backoff
import openai
import os

from enums.reasoning import ReasoningEnum
from mixtral import prompt, login
from qafv_model.gpt3_template import GPT3_Template
from dotenv import load_dotenv

load_dotenv()

@backoff.on_exception(backoff.expo, openai.error.RateLimitError)
def completions_with_backoff(**kwargs):
    return openai.Completion.create(**kwargs)

@backoff.on_exception(backoff.expo, openai.error.RateLimitError)
def chat_completions_with_backoff(**kwargs):
    return openai.ChatCompletion.create(**kwargs)

class GPT3_T5_Question_Answering:
    def __init__(self, API_KEY, model_name, hugging_face_email) -> None:
        self.API_KEY = API_KEY
        self.model_name = "gpt-4o-mini"

        self.gpt3_template = GPT3_Template()


    # used for chat-gpt and gpt-4
    def generate(self, input_string, max_token):
        print("question answering")
        openai.api_key = os.environ['OPENAI_KEY']
        openai.api_base = "https://api.openai.com/v1"
        response = chat_completions_with_backoff(
            model=self.model_name,
            messages=[
                {"role": "user", "content": input_string}
            ],
            max_tokens=max_token,
            temperature=0.1,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0
        )
        generated_text = response['choices'][0]['message']['content'].strip()

        return generated_text

    def retrieve_evidence(self, question):
        #input_string = f'{question}\nRetrieve a Wikipedia article relevant to this question.'
        input_string = f'{question}\n Give evidence relevant to this question.'      
        generated_text = self.generate(input_string, max_token = 512)
        return generated_text
    
    def answer_question(self, question):
        # retrieve evidence
        rationale = self.retrieve_evidence(question).strip()

        # answer question
        predict_answer = {}
        example = f'Evidence: {rationale}\nQuestion: {question}\n Based on the provided evidence snippet, the answer is:'
        answer_text = self.generate(example, max_token = 64)
        
        predict_answer['rationale'] = rationale
        predict_answer['answer_text'] = answer_text
        return predict_answer


