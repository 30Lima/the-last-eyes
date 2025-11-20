# app/models/analysis_input.py
from pydantic import BaseModel

class AnalysisInput(BaseModel):
    text: str
    userId: str | None = None  # opcional, se quiser ligar ao usuário no app
