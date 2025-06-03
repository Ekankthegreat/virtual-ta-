from fastapi import FastAPI, Request
from pydantic import BaseModel

app = FastAPI()

class Question(BaseModel):
    question: str

@app.post("/answer")
async def answer_question(q: Question):
    # Replace this with actual logic
    if "alias" in q.question.lower():
        return {"answer": "A type alias in TypeScript is a name for any type."}
    return {"answer": "Sorry, I don't know the answer yet."}
