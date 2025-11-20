# app/models/generate_input.py
from pydantic import BaseModel
from typing import Optional

class GenerateInput(BaseModel):
    userId: Optional[str] = None
    context: Optional[str] = None 
    mood: Optional[str] = None     
    request: str                 
