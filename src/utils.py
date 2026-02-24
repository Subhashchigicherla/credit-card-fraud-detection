import joblib
import numpy as np

def load_model(path="models/fraud_model.pkl"):
    return joblib.load(path)

def predict(model, X):
    proba = model.predict_proba(X)[:, 1]
    pred = (proba > 0.5).astype(int)
    return pred, proba