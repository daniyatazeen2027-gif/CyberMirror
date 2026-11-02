
import joblib
import pandas as pd
from pathlib import Path
from sklearn.ensemble import IsolationForest


def train_anomaly_detector(
    features: pd.DataFrame,
    contamination: float = 0.05,
    random_state: int = 42,
):
    if features.empty:
        raise ValueError("Cannot train on an empty dataset.")

    if len(features) < 10:
        raise ValueError(
            "At least 10 records are required for this initial model."
        )

    if not 0 < contamination <= 0.5:
        raise ValueError("Contamination must be between 0 and 0.5.")

    model = IsolationForest(
        n_estimators=100,
        contamination=contamination,
        random_state=random_state,
    )

    model.fit(features)

    return model


def predict_anomalies(model, features: pd.DataFrame) -> pd.DataFrame:
    if features.empty:
        raise ValueError("Cannot predict on an empty dataset.")

    predictions = model.predict(features)
    anomaly_scores = model.decision_function(features)

    return pd.DataFrame({
        "prediction": predictions,
        "anomaly_score": anomaly_scores,
        "is_anomaly": predictions == -1,
    }, index=features.index)


def save_anomaly_detector(model, file_path: str):
    path = Path(file_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, path)


def load_anomaly_detector(file_path: str):
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"Model not found: {file_path}")

    return joblib.load(path)
