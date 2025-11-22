# app/routers/generate.py
from fastapi import APIRouter, HTTPException
from app.models.generate_input import GenerateInput
from app.models.generate_output import GenerateOutput
from app.services.gemini_service import generate_text

router = APIRouter(tags=["Generate"])

@router.post("/generate", response_model=GenerateOutput)
async def generate(payload: GenerateInput):
    """
    Gera texto via Gemini baseado no prompt.
    userId, context e mood são opcionais — ajudam a personalizar o prompt.
    "request" é a instrução principal para a IA (ex: "gere dicas", "insights para bem-estar").
    """
    prompt_parts = []

    if payload.context:
        prompt_parts.append(f"Contexto do usuário: {payload.context}")
    if payload.userId:
        prompt_parts.append(f"ID do usuário: {payload.userId}")
    if payload.mood:
        prompt_parts.append(f"Humor atual: {payload.mood}")
    prompt_parts.append(f"Instrução: {payload.request}")

    prompt = "\n".join(prompt_parts)

    generated = generate_text(prompt)
    if generated is None:
        raise HTTPException(status_code=500, detail="Falha ao gerar texto com a IA.")

    return {"generated_text": generated}
