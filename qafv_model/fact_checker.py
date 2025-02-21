import argparse

from qafv_model.question_generation import GPT3_Question_Generator
from qafv_model.reasoner import Fact_Reasoner
from qafv_model.question_answering import GPT3_T5_Question_Answering

class QAFV_Fact_Checker:
    def __init__(self, api_key, qa_module, hugging_face_email=None, model_name="gpt-4"):
        # load model

        # initialize sub-modules
        API_KEY = api_key
        model_name = model_name
        self.question_generator = GPT3_Question_Generator(API_KEY, model_name, hugging_face_email)
        self.QA_module = qa_module(API_KEY, model_name, hugging_face_email)
        self.reasoner = Fact_Reasoner(API_KEY, model_name, hugging_face_email)
        print(f"Individual modules initialized.")

    '''
    This one collaborates with GPT3
    '''
    def verify_single_claim_GPT3(self, claim, MAX_ROUND = 5):
        contexts_history = []
        qa_contexts = []
        for round_ind in range(MAX_ROUND):
            Should_Stop = False
            # Question Generation
            sub_question = ""
            if round_ind == 0:
                sub_question = self.question_generator.generate_first_question(claim)
            else:
                # Whether we should stop here. 
                Should_Stop = self.reasoner.is_information_sufficient(claim, qa_contexts)
                if Should_Stop == True:
                    break
                # otherwise, generate the next subquestion
                sub_question = self.question_generator.generate_next_question(claim, qa_contexts)
            
            # Question Answering
            answer = self.QA_module.answer_question(sub_question)
            answer_text = answer['answer_text']
            answer_rationale = answer['rationale']

            # Save Result
            qa_result = {'round': round_ind, 
                         'target_entity': "", 
                         'generated_question': sub_question, 
                         'answer': answer_text, 
                         'rationale': answer_rationale,
                         'predicate': None}
            
            contexts_history.append(qa_result)
            qa_contexts.append([sub_question, answer_text])

        # reason the label
        prediction_with_rationale = self.reasoner.CoT_claim_verification(claim, qa_contexts)

        return prediction_with_rationale, contexts_history