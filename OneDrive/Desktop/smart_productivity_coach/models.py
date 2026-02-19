from pydantic import BaseModel, Field
from typing import List

class Task(BaseModel):
    title: str
    deadline: str
    difficulty: int = Field(ge=1, le=5)

class PlanRequest(BaseModel):
    tasks: List[Task]
    energy_level: int = Field(ge=1, le=10)
    available_hours: float = Field(gt=0)

class ProgressRequest(BaseModel):
    completed_tasks: int
    total_tasks: int
