from pydantic import BaseModel
from typing import List, Optional

class QuestionOut(BaseModel):
    id: int
    type: str
    question: str
    options: Optional[List[str]]

    class Config:
        orm_mode = True