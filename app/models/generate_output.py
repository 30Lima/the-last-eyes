# app/models/generate_output.py
from pydantic import BaseModel

class GenerateOutput(BaseModel):
    generated_text: str
