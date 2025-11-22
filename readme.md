# Criar a venv
python -m venv .venv

# Ativar a venv (Windows)
.venv\Scripts\activate

# Instalar dependências principais
pip install -r requirements.txt

# (Opcional) Usar o endpoint do Gemini
pip install google-generativeai

# Gerar sua API Key:
# Acesse: https://aistudio.google.com/api-keys
# Clique em "Criar chave da API" no canto superior direito

# Após gerar a chave, cole no arquivo:
# app/core/config.py  (linha 6)
