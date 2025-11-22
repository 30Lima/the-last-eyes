import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

models = genai.list_models()

for m in models:
    print("\n==============================")
    print("NAME:", m.name)

    # Campos comuns que normalmente existem
    for attr in ["display_name", "description", "input_token_limit", "output_token_limit"]:
        if hasattr(m, attr):
            print(f"{attr.upper()}: {getattr(m, attr)}")

    # Verifica se o modelo suporta geração
    generative = False
    if hasattr(m, "supported_generation_methods"):
        generative = "generateContent" in m.supported_generation_methods

    print("GENERATION SUPPORTED:", generative)
