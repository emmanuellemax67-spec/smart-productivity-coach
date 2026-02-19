from fastapi import HTTPException

def calculate_mental_load(tasks):

    total_tasks = len(tasks)
    total_difficulty = sum(task.difficulty for task in tasks)

    score = (total_tasks * 5) + (total_difficulty * 3)

    if score > 100:
        score = 100

    level = "Faible"

    if score > 30:
        level = "Modéré"
    if score > 60:
        level = "Élevé"
    if score > 80:
        level = "Critique"

    return {
        "total_tasks": total_tasks,
        "mental_load_score": score,
        "stress_level": level
    }


def calculate_productivity_score(completed, total):

    if total == 0:
        raise HTTPException(status_code=400, detail="Total tasks cannot be zero")

    score = (completed / total) * 100

    level = "Faible"
    if score > 50:
        level = "Bon"
    if score > 75:
        level = "Excellent"

    return {
        "productivity_score": round(score, 2),
        "performance_level": level
    }
