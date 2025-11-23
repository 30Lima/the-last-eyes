# The Last Eyes 
> Solução para a global solution promovido pela FIAP (Disruptive Architectures)

## Descrição da solução
Aplicar ela aqui futuramente

## Integrantes

| Nome Completo                 | RM      |
|-----------------------------|---------|
| Pedro Henrique Lima Santos  | 558243  |
| Vitor Gomes Martins         | 558244  |
| Leonardo Pimentel Santos    | 557541  |

### Link do PITCH
```bash
Inserir o link aqui futuramente (em modo não listado)
```

## 4. Estrutura do Projeto
```bash
/
├── app/                      # Código principal da API (FastAPI)
│   ├── core/
│   │   └── config.py               # Configurações globais (carrega variáveis de ambiente e API Keys)
│   ├── models/                     # Schemas Pydantic (Validação de dados de Entrada/Saída)
│   │   ├── analysis_input.py       # Modelo de dados para análise de sentimento
│   │   ├── generate_input.py       # Modelo de dados para o prompt do Gemini
│   │   └── generate_output.py      # Estrutura da resposta gerada
│   ├── routers/                    # Definição das Rotas/Endpoints da API
│   │   ├── analyze.py              # Rota de análise de sentimento (usa o modelo local)
│   │   ├── generate.py             # Rota de geração de texto (usa Google Gemini)
│   │   ├── health.py               # Health Check (para monitoramento do Render)
│   │   └── version.py              # Endpoint de versão da API
│   ├── services/                   # Lógica de negócio e Serviços
│   │   ├── gemini_service.py       # Lógica de conexão com o Google AI Studio
│   │   └── sentiment_analyzer.py   # Carregamento do modelo .pkl e lógica de predição
│   └── main.py                     # Ponto de entrada da aplicação (Inicializa o FastAPI e CORS)
├── model/                          # Artefatos de Machine Learning
│   └── sentiment_model.pkl         # O modelo treinado serializado (Salvo pelo train_model.py)
├── .dockerignore                   # Arquivos ignorados pelo Docker (reduz tamanho da imagem)
├── .gitignore                      # Arquivos ignorados pelo Git
├── dockerfile                      # Receita da imagem Docker (Configuração do container)
├── readme.md                       # Documentação do projeto
├── requirements.txt                # Dependências do projeto (FastAPI, Scikit-learn, Google GenAI...)
└── train_model.py                  # Script standalone para treinar e salvar o modelo .pkl
```

## 🛠️ Como rodar o projeto localmente

Siga os passos abaixo para configurar o ambiente de desenvolvimento na sua máquina.

### 1. Criar e ativar o ambiente virtual

```bash
# Criar a venv
python -m venv .venv
```

# Ativar a venv (Windows)
```bash
.venv\Scripts\activate
```

# Ativar a venv (Linux/Mac)

# Windows
```bash
.venv\Scripts\activate
```

# Linux/Mac
```bash
source .venv/bin/activate
```

### 2. Instalar dependências
```bash
pip install -r requirements.txt
```

### 3. Configurar Variáveis de Ambiente (Segurança)
- Gere sua API Key no Google AI Studio: https://aistudio.google.com/api-keys
- Na raiz do projeto, crie um arquivo chamado .env (sem nome, só a extensão).
- Cole sua chave dentro dele neste formato:
```bash
GOOGLE_API_KEY="insira_ua_chave_aqui"
```

### Executar a API
```bash
uvicorn app.main:app --reload --port 8000 --env-file .env
```

### 🚀 Deploy (Produção)
A API já está publicada e rodando no Render. Você pode testar os endpoints diretamente pelo link abaixo:
🔗 Swagger UI: https://the-last-eyes-api.onrender.com/docs

---
© 2025 MontClio. Todos os direitos reservados.

