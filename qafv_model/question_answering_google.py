import time
import random

import backoff  # for exponential backoff
import openai
from googlesearch import search, search_question, _search_page, SearchResult
#import tldextract
from qafv_model.gpt3_template import GPT3_Template
from qafv_model.question_answering import GPT3_T5_Question_Answering


@backoff.on_exception(backoff.expo, openai.error.RateLimitError)
def completions_with_backoff(**kwargs):
    return openai.Completion.create(**kwargs)


@backoff.on_exception(backoff.expo, openai.error.RateLimitError)
def chat_completions_with_backoff(**kwargs):
    return openai.ChatCompletion.create(**kwargs)


trusted_domain_suffixes = [
    "org",
    "edu",
    "gov"
]

trusted_domains = [
    "wikipedia.org",
    "theatlantic.com",
    "bbc.com",
    "economist.com",
    "nytimes.com",
    "smithsonianmag.com",
    "wsj.com",
    "washingtonpost.com"
]


class GPT3_T5_Question_Answering_Google(GPT3_T5_Question_Answering):

    def retrieve_evidence(self, question, filter_domains=True):
        """
        search_result = search_question(question)

        if isinstance(search_result, SearchResult):
            print("is instance")
            return search_result.description + "\nRetrieved from: " + search_result.url

        return search_result[0].description + "\nRetrieved from: " + search_result[0].url
        """

        time.sleep(random.randint(1, 10))

        big_sleep = random.uniform(0, 1)
        if big_sleep > 0.9:
            print("big sleep")
            time.sleep(random.randint(60,120))

        if big_sleep > 0.95:
            print("very big sleep")
            time.sleep(random.randint(120, 300))

        i = 0
        while i < 5:
            i = i + 1
            try:
                print(question)
                search_result = list(search(question, advanced=True,sleep_interval=5))

            except Exception as e:
                #print(f"Google Search exception: {e}")
                raise Exception(e)
                #time.sleep(30)
                continue

            try:
                print("search result")
                print(search_result[0])
            except IndexError as e:
                print(search_result)
                return f"No evidence could be found: {question}"

            return search_result[0].description + "\nRetrieved from: " + search_result[0].url

        return "No evidence could be found"
