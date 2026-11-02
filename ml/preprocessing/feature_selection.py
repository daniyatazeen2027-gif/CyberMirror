import pandas as pd

FEATURE_COLUMNS = [
    "message_frequency",
    "inter_arrival_time",
    "payload_length",
]


def select_features(features: pd.DataFrame) -> pd.DataFrame:
    if features.empty:
        raise ValueError("Cannot select features from an empty dataset.")

    missing_columns = [
        column for column in FEATURE_COLUMNS
        if column not in features.columns
    ]

    if missing_columns:
        raise ValueError(f"Missing feature columns: {missing_columns}")

    selected_features = features[FEATURE_COLUMNS].copy()

    return selected_features