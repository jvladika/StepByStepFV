import backoff  # for exponential backoff
import openai
import random

from enums.reasoning import ReasoningEnum
from mixtral import login, prompt
from .folk_template import FOLK_Template
from .gpt3_template import GPT3_Template


@backoff.on_exception(backoff.expo, openai.error.RateLimitError)
def completions_with_backoff(**kwargs):
    return openai.Completion.create(**kwargs)


@backoff.on_exception(backoff.expo, openai.error.RateLimitError)
def chat_completions_with_backoff(**kwargs):
    return openai.ChatCompletion.create(**kwargs)


class Fact_Reasoner_FOLK:
    def __init__(self, API_KEY, model_name, hugging_face_email) -> None:
        self.API_KEY = API_KEY
        self.model_name = model_name
        openai.api_key = API_KEY
        self.gpt3_template = FOLK_Template()
        self.chat = "chat"

        if hugging_face_email:
            #self.chat = login(hugging_face_email)
            self.chat = "chat"

    # used for chat-gpt and gpt-4
    def generate(self, input_string, max_token):
        if self.model_name in [ReasoningEnum.GPT_4, ReasoningEnum.GPT_3_5]:
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
            generated_text = response['choices'][0]['message']['content'].strip()

        elif self.model_name in [ReasoningEnum.MIXTRAL]:
            generated_text = prompt(self.chat, input_string, web=False)

        return generated_text

    def claim_verification(self, claim, qa_contexts):
        example = self.gpt3_template.fill_R_template(claim, qa_contexts)
        raw_output = self.generate(example, max_token=512)

        return raw_output

    def map_prediction(self, prediction):
        prediction = prediction.lower().strip()
        refutes_indicator = ["no", "false"]
        supports_indicator = ["yes", "true"]

        for indicator in supports_indicator:
            if prediction.find(indicator) >= 0:
                return 'supports'

        for indicator in refutes_indicator:
            if prediction.find(indicator) >= 0:
                return 'refutes'

        return random.sample(['supports', 'refutes'], 1)[0]

    def is_information_sufficient(self, claim, qa_contexts):
        def map_text_to_label(raw_text):
            indicators = ['yes']
            for indicator in indicators:
                if raw_text.lower().find(indicator) >= 0:
                    return True
            return False

        example = self.gpt3_template.fill_can_we_step_question(claim, qa_contexts)
        raw_output = self.generate(example, max_token=128)
        print("is information sufficient:")
        print(raw_output)
        prediction = map_text_to_label(raw_output)
        return prediction
