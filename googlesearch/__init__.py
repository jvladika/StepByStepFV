"""googlesearch is a Python library for searching Google, easily."""
from time import sleep
from textwrap import wrap
from bs4 import BeautifulSoup
from requests import get
from googlesearch.user_agents import get_useragent
#from sentence_transformers import SentenceTransformer, util
import urllib
#import torch


def _req(term, results, lang, start, proxies, timeout):
    resp = get(
        url="https://www.google.com/search",
        headers={
            "User-Agent": get_useragent()
        },
        params={
            "q": term,
            "num": results + 2,  # Prevents multiple requests
            "hl": lang,
            "start": start,
        },
        proxies=proxies,
        timeout=timeout,
    )
    resp.raise_for_status()
    return resp


class SearchResult:
    def __init__(self, url, title, description):
        self.url = url
        self.title = title
        self.description = description

    def __repr__(self):
        return f"SearchResult(url={self.url}, title={self.title}, description={self.description})"


def _read_page(url):
    return get(url).text


def _get_text_chunks(url, length=256):
    page = _read_page(url)
    soup = BeautifulSoup(page, "html.parser")

    text = soup.get_text()

    return wrap(text, width=length, break_long_words=False)


def _parse_answer_box(soup):
    result_block = soup.find("div", attrs={"class": "V3FYCf"})

    if not result_block:
        return None

    answer = result_block.find("span", "hgKElc").text
    source = result_block.find("a", attrs={"jsname": "UWckNb"})["href"]

    return SearchResult(source, None, answer)


def _parse_sidebox(soup):
    result_block = soup.find("div", attrs={"class": "kno-rdesc"})

    if not result_block:
        return None

    text = result_block.find("span").text
    source = result_block.find("a")["href"]
    title = soup.find("div", attrs={"class": "PZPZlf ssJ7i B5dxMb"}).text

    return SearchResult(source, title, text)


def _parse_results(soup, advanced=True):
    result_block = soup.find_all("div", attrs={"class": "g"})

    for result in result_block:
        # Find link, title, description
        link = result.find("a", href=True)
        title = result.find("h3")
        description_box = result.find(
            "div", {"style": "-webkit-line-clamp:2"})
        if description_box:
            description = description_box.text
            if link and title and description:
                if advanced:
                    yield SearchResult(link["href"], title.text, description)
                else:
                    yield link["href"]


def search_question(term, num_results=10, lang="en", proxy=None, advanced=False, sleep_interval=10, timeout=5):
    """Search the Google search engine"""
    sleep(sleep_interval)

    escaped_term = urllib.parse.quote_plus(term)  # make 'site:xxx.xxx.xxx ' works.

    # Proxy
    proxies = None
    if proxy:
        if proxy.startswith("https"):
            proxies = {"https": proxy}
        else:
            proxies = {"http": proxy}

    # Fetch
    start = 0

    resp = _req(escaped_term, num_results - start,
                lang, start, proxies, timeout)


    # Parse
    soup = BeautifulSoup(resp.text, "html.parser")

    # Find the answer box
    result = _parse_answer_box(soup)
    if result:
        print("Found answer box")
        return result

    # Find the side box
    result = _parse_sidebox(soup)
    if result:
        print("Found sidebox")
        return _parse_sidebox(soup)

    result = list(_parse_results(soup))
    return result


def _search_page(query, url):
    pars = _get_text_chunks(url)

    return _find_paragraph(query, pars)


def search(term, num_results=10, lang="en", proxy=None, advanced=False, sleep_interval=0, timeout=5):
    """Search the Google search engine"""

    escaped_term = urllib.parse.quote_plus(term)  # make 'site:xxx.xxx.xxx ' works.

    # Proxy
    proxies = None
    if proxy:
        if proxy.startswith("https"):
            proxies = {"https": proxy}
        else:
            proxies = {"http": proxy}

    # Fetch
    start = 0
    while start < num_results:
        # Send request
        print("searching")
        resp = _req(escaped_term, num_results - start,
                    lang, start, proxies, timeout)

        # Parse
        soup = BeautifulSoup(resp.text, "html.parser")
        result_block = soup.find_all("div", attrs={"class": "g"})
        if len(result_block) == 0:
            start += 1
        for result in result_block:
            # Find link, title, description
            link = result.find("a", href=True)
            title = result.find("h3")
            description_box = result.find(
                "div", {"style": "-webkit-line-clamp:2"})
            if description_box:
                description = description_box.text
                if link and title and description:
                    start += 1
                    if advanced:
                        yield SearchResult(link["href"], title.text, description)
                    else:
                        yield link["href"]
        sleep(sleep_interval)

        if start == 0:
            return []


def _find_paragraph(query, paragraphs):
    embedder = SentenceTransformer('all-MiniLM-L6-v2')

    paragraph_embeddings = embedder.encode(paragraphs, convert_to_tensor=True)
    query_embedding = embedder.encode(query, convert_to_tensor=True)

    cos_scores = util.cos_sim(query_embedding, paragraph_embeddings)[0]
    top_results = torch.topk(cos_scores, k=1)

    return paragraphs[top_results[1][0]]
