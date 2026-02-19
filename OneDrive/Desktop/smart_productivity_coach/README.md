# Smart Productivity Coach API

## Description
API intelligente permettant aux étudiants d'améliorer leur productivité grâce à une analyse IA.

## Fonctionnalités
- Génération de planning intelligent
- Calcul de charge mentale
- Analyse de progression
- Score de productivité
- Historique des sessions

## Technologies
- FastAPI
- OpenAI API
- Python

## Installation

pip install -r requirements.txt
uvicorn main:app --reload

## Routes principales
POST /generate-plan
POST /mental-load
POST /analyze-progress
GET /history
