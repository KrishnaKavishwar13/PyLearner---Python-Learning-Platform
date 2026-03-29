from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.question import Question
from app.models.result import Result
from app.schemas.question import QuestionOut
from app.schemas.result import QuizSubmit

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# 🎯 Get Quiz Questions
@router.get("/", response_model=list[QuestionOut])
def get_questions(db: Session = Depends(get_db)):
    questions = db.query(Question).all()
    return questions


# 🧠 Submit Quiz
@router.post("/submit")
def submit_quiz(data: QuizSubmit, db: Session = Depends(get_db)):
    score = 0
    total = len(data.answers)

    for q_id, user_ans in data.answers.items():
        q = db.query(Question).filter(Question.id == int(q_id)).first()
        if q and q.correct_answer == user_ans:
            score += 1

    result = Result(user_id=1, score=score, total_questions=total)  # temp user_id
    db.add(result)
    db.commit()

    return {
        "score": score,
        "total_questions": total
    }