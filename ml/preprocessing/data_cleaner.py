import pandas as pd


def clean_traffic_data(data: pd.DataFrame) -> pd.DataFrame:
    if data.empty:
        raise ValueError("The traffic dataset is empty.")

    cleaned_data = data.copy()

    # Remove duplicate records
    cleaned_data = cleaned_data.drop_duplicates()

    # Remove records with missing values
    cleaned_data = cleaned_data.dropna()

    # Reset row numbering
    cleaned_data = cleaned_data.reset_index(drop=True)

    return cleaned_data