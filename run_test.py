import argparse
import os
import random
import time

import openai

from enums.datasets import DatasetEnum
from enums.method import MethodEnum
from enums.reasoning import ReasoningEnum
from enums.source import EvidenceSourceEnum
from qafv_model.fact_checker import QAFV_Fact_Checker
from pysondb import db
from datetime import datetime
from dotenv import load_dotenv

from qafv_model.fact_checker_folk import QAFV_Fact_Checker_FOLK
from qafv_model.question_answering import GPT3_T5_Question_Answering
from qafv_model.question_answering_google import GPT3_T5_Question_Answering_Google
from qafv_model.question_answering_ddg import GPT3_T5_Question_Answering_Duck
from qafv_model.question_answering_huggingchat import GPT3_T5_Question_Answering_Huggingchat
from qafv_model.question_answering_mixtral import GPT3_T5_Question_Answering_Mixtral
from test.prepocess_dataset import DatasetLoader
from test.test_configs import TEST_CONFIGS

load_dotenv()


class FactCheckerException(Exception):
    pass


def extract_veracity(prediction, method: MethodEnum):
    if method in [MethodEnum.QACHECK, MethodEnum.KGGPT]:
        verdict = prediction.split()[-1]

        if verdict == "True.":
            return 1
        else:
            return 0

    if method == MethodEnum.FOLK:
        if "[SUPPORTED]" in prediction:
            return 1
        elif "[NOT_SUPPORTED]" in prediction:
            return 0
        elif "not supported" in prediction:
            return 0
        elif "supported" in prediction:
            return 1
        else:
            print("random FOLK prediction")
            return random.randint(0, 1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    # parser.add_argument('method', type)
    # parser.add_argument('model', type=str, choices=list(EvidenceSourceEnum), default=EvidenceSourceEnum.GPT_3_5)
    # parser.add_argument('dataset', type=str, choices=list(DatasetEnum), default=DatasetEnum.HOVER)
    parser.add_argument('config', type=str)
    parser.add_argument('range_from', type=int, nargs="?", default=0)
    parser.add_argument('range_to', type=int, nargs="?", default=0)
    parser.add_argument('file', type=str, nargs="?", default=None)
    args = parser.parse_args()

    config = TEST_CONFIGS[args.config]

    if config["reasoning"] == ReasoningEnum.MIXTRAL:
        api_key = os.environ["TOGETHER_API_KEY"]
    else:
        api_key = os.environ['OPENAI_KEY']

    now = datetime.now()
    current_time = now.strftime("%d-%m-%Y_%H:%M:%S")

    try:
        hg_email = config["hg_email"]
    except:
        hg_email = None

    print(hg_email)

    # set evidence source
    if config["evidence_source"] == EvidenceSourceEnum.GPT_3_5:
        evidence_source = GPT3_T5_Question_Answering
    elif config["evidence_source"] == EvidenceSourceEnum.HUGGING_CHAT:
        evidence_source = GPT3_T5_Question_Answering_Huggingchat
    elif config["evidence_source"] == EvidenceSourceEnum.GOOGLE:
        evidence_source = GPT3_T5_Question_Answering_Google
    elif config["evidence_source"] == EvidenceSourceEnum.DUCK:
        evidence_source = GPT3_T5_Question_Answering_Duck
    elif config["evidence_source"] == EvidenceSourceEnum.MIXTRAL:
        evidence_source = GPT3_T5_Question_Answering_Mixtral

    # set method and reasoning model
    if config["method"] == MethodEnum.QACHECK:
        fact_checker = QAFV_Fact_Checker(api_key=api_key,
                                         qa_module=evidence_source,
                                         model_name=config["reasoning"],
                                         hugging_face_email=hg_email)
    elif config["method"] == MethodEnum.FOLK:
        fact_checker = QAFV_Fact_Checker_FOLK(api_key=api_key,
                                              qa_module=evidence_source,
                                              model_name=config["reasoning"])
    elif config["method"] == MethodEnum.KGGPT:
        fact_checker = QAFV_Fact_Checker_KGGPT(api_key=api_key,
                                               model_name=config["reasoning"],
                                               hugging_face_email=hg_email)
    else:
        raise FactCheckerException(f"Method {config['method']} not available.")

    dataset = DatasetLoader.load(config)

    if args.file:
        predictions_db_file = args.file
    elif config['dataset'] == DatasetEnum.HOVER:
        predictions_db_file = (f"runs/{current_time}"
                               f"_{config['dataset']}-{config['num_hops']}HOP"
                               f"_{config['method']}"
                               f"_{config['reasoning']}"
                               f"_{config['evidence_source']}.json")

    else:
        predictions_db_file = (f"runs/{current_time}"
                               f"_{config['dataset']}"
                               f"_{config['method']}"
                               f"_{config['reasoning']}"
                               f"_{config['evidence_source']}.json")

    predictions_db = db.getDb(predictions_db_file)

    i = args.range_from
    r = args.range_to

    if r > len(dataset) or r == 0:
        r = len(dataset)

    print(f"Now running: \n"
          f"Dataset: {config['dataset']}\n"
          f"Number of claims: {len(dataset)}\n"
          f"Ranger: {i} to {r}\n"
          f"Method: {config['method']}\n"
          f"Reasoner: {config['reasoning']}\n"
          f"Evidence source: {config['evidence_source']}\n")

    while i < r:
        if (i - args.range_from) % 50 == 0:
            print(f"{datetime.now().strftime('%d-%m-%Y_%H:%M:%S')}: Claim {i}")
            print("...")
        try:
            prediction_with_rationale, contexts_history = fact_checker.verify_single_claim_GPT3(dataset[i]["claim"])
        except openai.error.Timeout as e:
            # Handle timeout error, e.g. retry or log
            print(f"OpenAI API request timed out: {e}")
            time.sleep(10)
            continue
        except openai.error.APIError as e:
            # Handle API error, e.g. retry or log
            print(f"OpenAI API returned an API Error: {e}")
            time.sleep(10)
            continue
        except openai.error.APIConnectionError as e:
            # Handle connection error, e.g. check network or log
            print(f"OpenAI API request failed to connect: {e}")
            time.sleep(10)
            continue
        except openai.error.InvalidRequestError as e:
            # Handle invalid request error, e.g. validate parameters or log
            print(f"OpenAI API request was invalid: {e}")
            time.sleep(10)
            continue
        except openai.error.AuthenticationError as e:
            # Handle authentication error, e.g. check credentials or log
            print(f"OpenAI API request was not authorized: {e}")
            time.sleep(10)
            continue
        except openai.error.PermissionError as e:
            # Handle permission error, e.g. check scope or log
            print(f"OpenAI API request was not permitted: {e}")
            time.sleep(10)
            continue
        except openai.error.RateLimitError as e:
            # Handle rate limit error, e.g. wait or log
            print(f"OpenAI API request exceeded rate limit: {e}")
            time.sleep(10)
            continue
        except Exception as e:
            print(e)
            time.sleep(60)
            continue

        result = dataset[i]
        result["prediction"] = extract_veracity(prediction_with_rationale, config["method"])
        result["rationale"] = prediction_with_rationale
        result["context"] = contexts_history
        result["row"] = i

        predictions_db.add(result)
        i = i + 1

    print("Finished.")
   
