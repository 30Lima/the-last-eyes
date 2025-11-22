# app/services/sentiment_analyzer.py
import os
import joblib
from typing import Tuple

MODEL_PATH = os.getenv("SENTIMENT_MODEL_PATH", "model/sentiment_model.pkl")

class SentimentAnalyzer:
    def __init__(self, model_path: str = MODEL_PATH):
        self.model_path = model_path
        self.model = None
        self._load_model()

    def _load_model(self):
        try:
            self.model = joblib.load(self.model_path)
            print(f"[SentimentAnalyzer] Modelo carregado: {self.model_path}")
        except Exception as e:
            print(f"[SentimentAnalyzer] Não foi possível carregar o modelo ({self.model_path}): {e}")
            self.model = None

    def analyze(self, text: str) -> Tuple[str, float]:
        """
        Retorna (label, score) onde label é 'positivo'/'negativo' e score é probabilidade máxima (0..1).
        Se o modelo não estiver disponível, retorna fallback.
        """
        if not self.model:
            lower = text.lower()
            if any(w in lower for w in ["bom", "bem", "feliz", "motivad", "excelente"]):
                return "positivo", 0.6
            if any(w in lower for w in ["ruim", "pessimo", "triste", "ansios", "cansad", "sobrecarreg"]):
                return "negativo", 0.6
            return "neutro", 0.5

        pred = self.model.predict([text])[0]
        try:
            proba = max(self.model.predict_proba([text])[0])
        except Exception:
            proba = 0.0
        return pred, float(proba)
