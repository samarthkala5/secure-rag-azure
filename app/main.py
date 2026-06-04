from fastapi import FastAPI
from pydantic import BaseModel

from app.rag.generator import generate_answer

app = FastAPI(
    title="Secure RAG Service",
    description="Security-focused RAG API",
    version="1.0.0"
)


class QuestionRequest(BaseModel):
    question: str


@app.get("/")
def health():
    return {
        "status": "healthy"
    }


@app.post("/ask")
def ask(req: QuestionRequest):

    answer = generate_answer(
        req.question
    )

    return {
        "question": req.question,
        "answer": answer
    }