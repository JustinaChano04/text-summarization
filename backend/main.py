import requests
import json
import config
from fastapi import FastAPI
import re


def get_articles(articleCount, keyword):
    url = "http://eventregistry.org/api/v1/article/getArticles"
    headers = {
        "Content-Type": "application/json",
    }
    body = {
        "action": "getArticles",
        "keyword": keyword,
        "articlesCount": articleCount,
        "apiKey": config.api_key,
    }

    r = requests.request("post", url, headers=headers, data=json.dumps(body))

    if r.status_code == 200:
        result = r.json()
        article_list = []
        for text in result["articles"]["results"]:
            art_dict = {}
            art_dict["title"] = text["title"]
            art_dict["body"] = text["body"]
            article_list.append(art_dict)
        return article_list
    else:
        return {"message": r.status_code}


def parse_answer():

    # change test prompt based on GPT API Call
    with open("test_prompt.txt", 'r') as f:
        sample_response = f.read()
    
    vocab_index = sample_response.find("VOCAB")
    lines = sample_response[vocab_index:].splitlines()
    def_dict = []
    for term in lines[2:]:
        term_dict = {}
        word, definition = term.split(":")
        term_dict["title"] = word
        term_dict["body"] = definition
        def_dict.append(term_dict)

    return sample_response[:vocab_index], def_dict

    
# if __name__ == "__main__":

# #     # ret = get_articles(3, "Finance, Technology")
# #     # # app = FastAPI()
#     vocab = parse_answer()
