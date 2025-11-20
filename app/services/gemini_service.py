import os
import google.generativeai as genai
from google.generativeai.types import HarmCategory, HarmBlockThreshold

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Configuração Inicial
if GOOGLE_API_KEY:
    genai.configure(api_key=GOOGLE_API_KEY)
    try:
        # Tenta carregar o modelo. 
        # Se der erro de "modelo não encontrado", tente mudar para "gemini-1.5-flash"
        model_name = "gemini-2.5-flash" 
        model = genai.GenerativeModel(model_name)
        print(f"[Gemini] Modelo carregado com sucesso: {model_name}")
    except Exception as e:
        print(f"[Gemini] Erro ao inicializar modelo Gemini: {e}")
        model = None
else:
    model = None
    print("[Gemini] GOOGLE_API_KEY não encontrada — Gemini desativado")


def extract_text(response):
    """
    Extrai texto independente do formato retornado pelo Gemini.
    Essa função funciona para TODAS as versões do SDK.
    """
    try:
        # 1 — Se houver método .text direto e válido
        if hasattr(response, "text") and response.text:
            return response.text

        # 2 — Verificar structure candidates → content → parts
        if hasattr(response, "candidates") and response.candidates:
            cand = response.candidates[0]
            
            # Verifica se foi bloqueado
            if hasattr(cand, "finish_reason") and cand.finish_reason != 1: # 1 = STOP (sucesso)
                print(f"[Gemini] Bloqueio detectado. Finish Reason: {cand.finish_reason}")

            if hasattr(cand, "content") and cand.content and hasattr(cand.content, "parts"):
                texts = []
                for part in cand.content.parts:
                    if hasattr(part, "text"):
                        texts.append(part.text)
                if texts:
                    return "\n".join(texts)

        return None

    except Exception as e:
        print(f"[Gemini] Erro na extração: {e}")
        return None


def generate_text(prompt: str, max_tokens: int = 2000) -> str:
    if model is None:
        return "Erro: modelo Gemini não configurado."

    try:
        # --- CORREÇÃO PRINCIPAL: Configurações de Segurança ---
        # Isso define os filtros para NÃO bloquear nada (BLOCK_NONE)
        safety_settings = {
            HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_NONE,
            HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_NONE,
            HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_NONE,
            HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
        }

        response = model.generate_content(
            contents=[{"role": "user", "parts": [{"text": prompt}]}],
            generation_config={
                "temperature": 0.7,
                "max_output_tokens": max_tokens
            },
            safety_settings=safety_settings # Aplica as configurações aqui
        )

        # Verifica feedback do prompt (se o prompt em si violou regras)
        if hasattr(response, "prompt_feedback") and response.prompt_feedback:
            if response.prompt_feedback.block_reason:
                print(f"[Gemini] Prompt bloqueado! Motivo: {response.prompt_feedback.block_reason}")
                return f"Erro: O prompt foi bloqueado por segurança ({response.prompt_feedback.block_reason})."

        # Tenta extrair o texto
        text = extract_text(response)
        if text:
            return text

        # Se chegou aqui e não tem texto, tenta descobrir o motivo no primeiro candidato
        if response.candidates:
            reason = response.candidates[0].finish_reason
            return f"Erro: Resposta bloqueada pelo modelo. Motivo (Finish Reason): {reason}"

        return "Erro: resposta vazia ou bloqueada pelas políticas do modelo (sem detalhes adicionais)."

    except Exception as e:
        return f"Erro ao gerar texto: {e}"