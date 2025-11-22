# app/routers/analyze.py
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.models.analysis_input import AnalysisInput
from app.services.sentiment_analyzer import SentimentAnalyzer

router = APIRouter(tags=["Analyze"])
analyzer = SentimentAnalyzer()

@router.post("/analyze")
async def analyze(payload: AnalysisInput):
    """
    Recebe { text, userId } e retorna { sentiment, score, text }.
    """
    try:
        text = payload.text
        label, score = analyzer.analyze(text)
        return {
            "userId": payload.userId,
            "text": text,
            "sentiment": label,
            "score": score
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
