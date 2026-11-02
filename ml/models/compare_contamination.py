
from sklearn.metrics import precision_score, recall_score, f1_score

from ml.preprocessing.preprocess_pipeline import preprocess_pipeline
from ml.models.anomaly_detector import train_anomaly_detector, predict_anomalies

# Load and preprocess the synthetic dataset
_, features, _ = preprocess_pipeline(
    "ml/datasets/raw/synthetic_can_training.csv"
)

# Synthetic ground-truth labels
actual_labels = [0] * 30 + [1] * 10

contamination_values = [0.10, 0.15, 0.20, 0.25]

print("Contamination | Precision | Recall | F1")
print("-" * 43)

for value in contamination_values:
    model = train_anomaly_detector(
        features,
        contamination=value,
    )

    results = predict_anomalies(model, features)
    predicted_labels = results["is_anomaly"].astype(int)

    precision = precision_score(actual_labels, predicted_labels)
    recall = recall_score(actual_labels, predicted_labels)
    f1 = f1_score(actual_labels, predicted_labels)

    print(
        f"{value:12.2f} | {precision:9.2f} | "
        f"{recall:6.2f} | {f1:.2f}"
    )
