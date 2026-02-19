Smart Productivity Coach API

Description

Smart Productivity Coach est une API développée avec FastAPI intégrant une intelligence artificielle (OpenAI) afin d’aider les étudiants à améliorer leur organisation, leur discipline et leur gestion du temps.

L’API ne se contente pas de stocker des données :
elle analyse les tâches, calcule la charge mentale, génère des plans intelligents et fournit un retour personnalisé basé sur l’IA.

Problème Résolu

Les étudiants :
Procrastinent
Ont du mal à prioriser
Sous-estiment le temps nécessaire
Manquent de discipline

Fonctionnalités
Génération de planning intelligent
Calcul de charge mentale
Analyse de progression
Score de productivité
Historique des sessions

Technologies
FastAPI
OpenAI API
Python
Uvicorn

Installation
pip install -r requirements.txt uvicorn main:app --reload

Routes principales
POST /generate-plan POST /mental-load POST /analyze-progress GET /history
