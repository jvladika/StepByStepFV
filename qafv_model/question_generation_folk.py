import backoff  # for exponential backoff
import openai

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


class GPT3_Question_Generator_FOLK:
    def __init__(self, API_KEY, model_name, hugging_face_email) -> None:
        self.API_KEY = API_KEY
        self.model_name = model_name
        openai.api_key = API_KEY
        self.gpt3_template = FOLK_Template()

        if hugging_face_email:
            #self.chat = login(hugging_face_email)
            self.chat = "chat" ##dummy

    # used for chat-gpt and gpt-4
    def generate(self, input_string):
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

    def generate_first_question(self, claim):
        example = self.gpt3_template.fill_QG_template_start(claim)
        generated_text = self.generate(example)

        if self.model_name in [ReasoningEnum.GPT_3_5, ReasoningEnum.GPT_4]:
            generated_text = generated_text.splitlines()
            if "" in generated_text:
                generated_text.remove("")
            return [generated_text[1], generated_text[3]]

        elif self.model_name in [ReasoningEnum.MIXTRAL]:
            generated_text = (generated_text.replace("Question:", "")
                              .replace("Question", "")
                              .replace("Predicate:", "")
                              .replace("Predicate", "")
                              .strip()
                              .splitlines())

            generated_text = [term for term in generated_text if term.strip()]

            if "=" in generated_text:
                right_text = generated_text.split("= ")[1:]
                final_text = ""
                for t in right_text:
                    final_text += t + " "
                generated_text = final_text

            return generated_text


    def generate_next_question(self, claim, qa_contexts):
        example = self.gpt3_template.fill_QG_template_followup(claim, qa_contexts)
        generated_text = self.generate(example)

        if self.model_name in [ReasoningEnum.GPT_3_5, ReasoningEnum.GPT_4]:
            generated_text = generated_text.splitlines()
            if "" in generated_text:
                generated_text.remove("")
            return [generated_text[1], generated_text[3]]


        elif self.model_name in [ReasoningEnum.MIXTRAL]:
            generated_text = (generated_text.replace("Followup Question:", "")
                              .replace("Followup Question", "")
                              .replace("Question", "")
                              .replace("Predicate:", "")
                              .replace("Predicate", "")
                              .strip()
                              .splitlines())

            generated_text = [term for term in generated_text if term.strip()]

            if "=" in generated_text:
                right_text = generated_text.split("= ")[1:]
                final_text = ""
                for t in right_text:
                    final_text += t + " "
                generated_text = final_text

            return generated_text

