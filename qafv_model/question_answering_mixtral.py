import time

from qafv_model.gpt3_template import GPT3_Template
from qafv_model.question_answering import GPT3_T5_Question_Answering

from mixtral import login, prompt


class GPT3_T5_Question_Answering_Mixtral(GPT3_T5_Question_Answering):

    def generate(self, input_string, max_token):
        generated_text = prompt(None, input_string, web=False)

        return generated_text
    
    def retrieve_evidence(self, question, filter_domains=True):

        #input_string = f'{question}\nRetrieve a Wikipedia article relevant to this question.'
        input_string = f'{question}\n Give evidence relevant to this question.'      
        generated_text = self.generate(input_string, 512)
        
        return generated_text
    
      