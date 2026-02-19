from fastapi import FastAPI
from routes import coach

app = FastAPI(
    title="Smart Productivity Coach API",
    description="API intelligente de coaching en productivité avec IA",
    version="1.0"
)

app.include_router(coach.router)
