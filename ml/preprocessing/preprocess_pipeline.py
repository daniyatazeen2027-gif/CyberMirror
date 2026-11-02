
from ml.preprocessing.data_loader import load_traffic_data
from ml.preprocessing.data_cleaner import clean_traffic_data
from ml.preprocessing.feature_extraction import extract_features
from ml.preprocessing.feature_selection import select_features
from ml.preprocessing.feature_scaling import scale_features


def preprocess_pipeline(file_path: str, scaler=None):
    # Step 1: Load and validate traffic data
    data = load_traffic_data(file_path)

    # Step 2: Clean the dataset
    cleaned_data = clean_traffic_data(data)

    # Step 3: Extract numerical features
    features = extract_features(cleaned_data)

    # Step 4: Select relevant features
    selected_features = select_features(features)

    # Step 5: Scale using a new or previously trained scaler
    scaled_features, scaler = scale_features(
        selected_features,
        scaler=scaler,
    )

    return cleaned_data, scaled_features, scaler
