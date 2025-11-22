from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import analyze, health, version, generate

app = FastAPI(
    title="The Last Eyes - API com IA Generativa",
    description="API para classificação de sentimento e geração de texto com Gemini.",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],          
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health.router, prefix="/health", tags=["Health"])
app.include_router(version.router, prefix="/version", tags=["Version"])
app.include_router(analyze.router, prefix="/api", tags=["Sentiment Analysis"])
app.include_router(generate.router, prefix="/api", tags=["Generative AI"])

@app.get("/", tags=["Root"])
def root():
    return {
        "message": "The Last Eyes API está rodando!",
        "docs": "/docs",
        "health": "/health",
        "sentiment_analysis": "/api/analyze",
        "generative_ai": "/api/generate"
    }
