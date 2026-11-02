
from ml.preprocessing.preprocess_pipeline import preprocess_pipeline
from ml.preprocessing.feature_scaling import save_scaler
from ml.models.anomaly_detector import (
    train_anomaly_detector,
    save_anomaly_detector,
)

DATASET_PATH = "ml/datasets/raw/synthetic_can_training.csv"

MODEL_PATH = "ml/models/trained/isolation_forest.joblib"
SCALER_PATH = "ml/models/trained/feature_scaler.joblib"

# Load data and fit the scaler
data, features, scaler = preprocess_pipeline(DATASET_PATH)

# Train the model using the selected experimental setting
model = train_anomaly_detector(
    features,
    contamination=0.15,
    random_state=42,
)

# Save the matching model and scaler
save_anomaly_detector(model, MODEL_PATH)
save_scaler(scaler, SCALER_PATH)

print("Model training completed successfully.")
print("Training records:", len(data))
print("Contamination:", 0.15)
print("Model saved:", MODEL_PATH)
print("Scaler saved:", SCALER_PATH)

