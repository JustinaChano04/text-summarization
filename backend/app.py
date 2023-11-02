from fastapi import FastAPI
from main import get_articles, parse_answer
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()
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
class word(BaseModel):
    data: str


@app.get("/load_articles")
async def root():
    articles = get_articles(3, "Finance, Technology") 
    summary, definitions = parse_answer()
    return articles, definitions

@app.post("/post_vocab")
async def post_vocab():
    print('1')




if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=5000, log_level="debug")
