# app/models/analysis_input.py
from pydantic import BaseModel

class AnalysisInput(BaseModel):
    text: str
    userId: int 
