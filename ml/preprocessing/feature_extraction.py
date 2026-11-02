import pandas as pd

FEATURE_COLUMNS = [
    "message_frequency",
    "inter_arrival_time",
    "payload_length",
]


def extract_features(data: pd.DataFrame) -> pd.DataFrame:
    if data.empty:
        raise ValueError("Cannot extract features from an empty dataset.")

    missing_columns = [
        column for column in FEATURE_COLUMNS
        if column not in data.columns
    ]

    if missing_columns:
        raise ValueError(f"Missing feature columns: {missing_columns}")

    features = data[FEATURE_COLUMNS].copy()

    return features