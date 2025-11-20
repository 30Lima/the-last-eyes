# train_model.py
import os
from pathlib import Path
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression

# Dataset pequeno de exemplo (substitua/expanda com dados reais)
TRAIN_DATA = [
    ("Estou muito feliz com o progresso", "positivo"),
    ("Hoje foi um dia péssimo, me senti mal", "negativo"),
    ("Sinto que tudo está indo bem", "positivo"),
    ("Estou cansado e desmotivado", "negativo"),
    ("Excelente trabalho da equipe hoje", "positivo"),
    ("Me sinto sobrecarregado e estressado", "negativo"),
    ("Estou tranquilo", "positivo"),
    ("Ansioso com as entregas", "negativo"),
    ("Muito motivado e animado", "positivo"),
    ("Não consigo me concentrar", "negativo"),
]

def train_and_save_model(output_path="model/sentiment_model.pkl"):
    X = [t[0] for t in TRAIN_DATA]
    y = [t[1] for t in TRAIN_DATA]

    pipeline = Pipeline([
        ("tfidf", TfidfVectorizer(ngram_range=(1,2), max_features=5000)),
        ("clf", LogisticRegression(max_iter=1000))
    ])

    pipeline.fit(X, y)
    os.makedirs(Path(output_path).parent, exist_ok=True)
    joblib.dump(pipeline, output_path)
    print(f"Modelo treinado e salvo em: {output_path}")

if __name__ == "__main__":
    train_and_save_model()
