import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_productivity_plan(tasks, energy_level, available_hours):

    task_description = "\n".join(
        [f"- {task.title} (deadline: {task.deadline}, difficulté: {task.difficulty}/5)" for task in tasks]
    )

    prompt = f"""
    Tu es un coach expert en productivité.

    Voici les tâches :
    {task_description}

    Niveau d'énergie : {energy_level}/10
    Temps disponible : {available_hours} heures

    1. Classe les tâches par priorité.
    2. Propose un planning horaire structuré.
    3. Donne des conseils personnalisés.
    4. Donne un conseil motivationnel final.
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Tu es un coach professionnel en productivité."},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content


def analyze_progress(completed, total):

    prompt = f"""
    Un étudiant a complété {completed} tâches sur {total}.
    Analyse sa discipline, ses habitudes et donne des conseils d'amélioration.
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Tu es un coach comportemental."},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content