
from pathlib import Path

import pandas as pd


REQUIRED_COLUMNS = [
    "timestamp",
    "can_id",
    "message_frequency",
    "inter_arrival_time",
    "payload_length",
    "ecu_id",
]

NUMERIC_COLUMNS = [
    "message_frequency",
    "inter_arrival_time",
    "payload_length",
]


def validate_traffic_data(data: pd.DataFrame) -> pd.DataFrame:
    """
    Validate the structure and values of a CAN traffic dataset.
    Returns a validated copy of the DataFrame.
    """

    if data.empty:
        raise ValueError("The traffic dataset is empty.")

    missing_columns = [
        column for column in REQUIRED_COLUMNS
        if column not in data.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Missing required columns: {missing_columns}"
        )

    data = data.copy()

    if data[REQUIRED_COLUMNS].isnull().any().any():
        raise ValueError(
            "The dataset contains missing values in required columns."
        )

    data["timestamp"] = pd.to_datetime(
        data["timestamp"], errors="coerce"
    )

    if data["timestamp"].isnull().any():
        raise ValueError("Invalid timestamp values found.")

    for column in NUMERIC_COLUMNS:
        data[column] = pd.to_numeric(
            data[column], errors="coerce"
        )

        if data[column].isnull().any():
            raise ValueError(
                f"Invalid numeric values found in {column}."
            )

        if (data[column] < 0).any():
            raise ValueError(
                f"Negative values are not allowed in {column}."
            )

    for column in ["can_id", "ecu_id"]:
        data[column] = data[column].astype(str).str.strip()

        if data[column].eq("").any():
            raise ValueError(f"Empty values found in {column}.")

    return data


def load_traffic_data(file_path: str) -> pd.DataFrame:
    """
    Load a CAN traffic CSV file and validate its contents.
    """

    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(
            f"Dataset not found: {file_path}"
        )

    if path.suffix.lower() != ".csv":
        raise ValueError("Only CSV datasets are supported.")

    data = pd.read_csv(path)

    return validate_traffic_data(data)
