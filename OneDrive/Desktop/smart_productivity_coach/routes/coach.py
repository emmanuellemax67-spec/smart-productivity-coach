from fastapi import APIRouter
from models import PlanRequest, ProgressRequest
from services.productivity_service import calculate_mental_load, calculate_productivity_score
from ai_service import generate_productivity_plan, analyze_progress
from database import sessions_db

router = APIRouter()


@router.post("/generate-plan")
def generate_plan(data: PlanRequest):

    plan = generate_productivity_plan(
        tasks=data.tasks,
        energy_level=data.energy_level,
        available_hours=data.available_hours
    )

    sessions_db.append({
        "tasks": data.tasks,
        "energy": data.energy_level
    })

    return {
        "generated_plan": plan
    }


@router.post("/mental-load")
def mental_load(data: PlanRequest):
    return calculate_mental_load(data.tasks)


@router.post("/analyze-progress")
def analyze_user_progress(data: ProgressRequest):

    ai_feedback = analyze_progress(data.completed_tasks, data.total_tasks)

    score = calculate_productivity_score(
        data.completed_tasks,
        data.total_tasks
    )

    return {
        "productivity_analysis": score,
        "ai_feedback": ai_feedback
    }


@router.get("/history")
def get_history():
    return {
        "total_sessions": len(sessions_db),
        "sessions": sessions_db
    }
