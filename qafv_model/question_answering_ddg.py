import time
import random

from qafv_model.gpt3_template import GPT3_Template
from qafv_model.question_answering import GPT3_T5_Question_Answering

from duckduckgo_search import DDGS

class GPT3_T5_Question_Answering_Duck(GPT3_T5_Question_Answering):

    def retrieve_evidence(self, question, filter_domains=True):

        """
        Searches the query using DuckDuckGo.

        Args:
            query: Search query.
            timeout: Timeout of the requests call.

        Returns:
            search_results: A list of the top URLs relevant to the query.
        """
        
        timeout = 3.0
        time.sleep(1)

        try:
            results = DDGS(timeout=timeout).text(keywords=question, max_results=5)
            search_urls = [result["href"] for result in results]

            evidences = [result["body"] for result in results]
            evidence_text = ""
            counter = 1
            for e in evidences:
                evidence_text += str(counter) + ". "
                evidence_text += e
                evidence_text += "\n"
                counter += 1
            if len(evidences) == 0:
                evidence_text = "No results found."
                
            return evidence_text
            
        except Exception as e:
            print(f"An error occurred: {e}")
            return "No results found." 


        """
        search_result = search_question(question)

        if isinstance(search_result, SearchResult):
            print("is instance")
            return search_result.description + "\nRetrieved from: " + search_result.url

        return search_result[0].description + "\nRetrieved from: " + search_result[0].url
        
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

        """