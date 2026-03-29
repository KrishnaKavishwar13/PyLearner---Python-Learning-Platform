from pydantic import BaseModel

class QuizSubmit(BaseModel):
    answers: dict  # {question_id: answer}

class ResultOut(BaseModel):
    score: int
    total_questions: int