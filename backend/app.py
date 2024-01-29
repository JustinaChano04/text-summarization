from fastapi import FastAPI, Request
from main import get_articles, parse_answer
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from pymongo import MongoClient

app =  FastAPI(swagger_ui_parameters={"syntaxHighlight": False})
origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



# API endpoint to request articles from NewsAPI and parse prompt ChatGPT for summary and vocab definitions
@app.get("/articles")
async def root():

    # requests articles from NewsApi given key words
    articles = get_articles(3, "Finance, Technology") 
    summary, definitions = parse_answer()
    return articles, definitions

# 
@app.post("/store_vocab/")
async def post_vocab(request: Request):
    data = await request.json()
    # insert data into MongDB
    return data
    # {'word': 'Utility bill', 'definition': ' A regular charge for services like electricity, water, or gas.'}


# returns entire list of vocabulary terms 
@app.get("/all_definitions/")
async def definition_words():
    # return a list of vocabulary terms + definitions from the DB
    pass




if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=5000, log_level="debug")
