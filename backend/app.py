from fastapi import FastAPI, Request
from main import get_articles, parse_answer
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from pymongo import MongoClient
from mongodb_utils import db_insert, db_retrieve_all

app =  FastAPI(swagger_ui_parameters={"syntaxHighlight": False})
origins = [
    "http://localhost:3000",
]
summary_articles = []

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
    print(keywords)
    articles = get_articles(3, keywords)
    summary_articles = articles
    return keywords


# API endpoint to request articles from NewsAPI and parse prompt ChatGPT for summary and vocab definitions
@app.get("/articles")
async def articles(request: Request):
    summary, definitions = parse_answer()
    print(summary_articles)
    return summary_articles, definitions

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
    # return a list of vocabulary terms + definitions from the DB
    terms = db_retrieve_all()
    print(terms)
    return terms





if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=5000, log_level="debug")
