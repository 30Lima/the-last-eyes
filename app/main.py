from fastapi import FastAPI
from app.routers import analyze, health, version

app = FastAPI(
    title="The Last Eyes - Sentiment Analysis API",
    description="API para classificação de sentimento do projeto The Last Eyes.",
    version="1.0.0"
)

app.include_router(analyze.router)
app.include_router(health.router)
app.include_router(version.router)

@app.get("/")
def root():
    return {
        "message": "The Last Eyes API está rodando!",
        "docs": "/docs",
        "analyze": "/analyze"
    }
