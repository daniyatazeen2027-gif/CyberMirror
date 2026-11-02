
from pathlib import Path

import joblib
import pandas as pd
from sklearn.preprocessing import StandardScaler

FEATURE_COLUMNS = [
    "message_frequency",
    "inter_arrival_time",
    "payload_length",
]


def scale_features(features: pd.DataFrame, scaler=None):
    if features.empty:
        raise ValueError("Cannot scale an empty dataset.")

    missing_columns = [
        column for column in FEATURE_COLUMNS
        if column not in features.columns
    ]

    if missing_columns:
        raise ValueError(f"Missing feature columns: {missing_columns}")

    if scaler is None:
        scaler = StandardScaler()
        scaled_values = scaler.fit_transform(features[FEATURE_COLUMNS])
    else:
        scaled_values = scaler.transform(features[FEATURE_COLUMNS])

    scaled_features = pd.DataFrame(
        scaled_values,
        columns=FEATURE_COLUMNS,
        index=features.index,
    )

    return scaled_features, scaler


def save_scaler(scaler, file_path):
    path = Path(file_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(scaler, path)


def load_scaler(file_path):
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"Scaler not found: {file_path}")

    return joblib.load(path)
