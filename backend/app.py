from fastapi import FastAPI, Request
from openai import OpenAI
from main import get_articles, parse_answer
import uvicorn
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from pymongo import MongoClient
import gpt_utils as gpt
from mongodb_utils import db_insert, db_retrieve_all
import os
app =  FastAPI(swagger_ui_parameters={"syntaxHighlight": False})
origins = ["http://localhost:3000",]
stored_articles = []
assistant, thread = gpt.initialize_gpt()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/keywords")
async def keywords(request: Request):
    keywords = await request.json()
    keywords = keywords['keywords']
    article = get_articles(1, keywords)

    print("Number of articles: ", len(article))
    with open("articles.txt", "w") as file:
        file.write(str(article))
    global stored_articles
    stored_articles = []
    stored_articles = article
    
    return keywords

# API endpoint to request articles from NewsAPI and parse prompt ChatGPT for summary and vocab definitions
@app.get("/articles")
async def articles(request: Request):
    prompt_response = []
    for article in stored_articles:
        print(article["title"])
        with open("test_article.txt", "w") as fp:
            fp.write(f"{article['title']} \n {article['body']}")

        file_id = gpt.create_message(thread.id)
        data = gpt.run_thread(assistant, thread, file_id)
        prompt_response.append(data)
    
    if len(prompt_response) > 0:
        return prompt_response
    else:
        return {"error": "no articles with these keywords, try again."}
# 
@app.post("/store_vocab/")
async def post_vocab(request: Request):
    data = await request.json()
    # insert data into MongDB
    print(data)
    db_insert(data)

# returns entire list of vocabulary terms 
@app.get("/all_definitions")
async def definition_words():
    terms = db_retrieve_all()
    return terms

if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=5000, log_level="debug")
