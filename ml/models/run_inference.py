
from pathlib import Path

import pandas as pd

from ml.preprocessing.preprocess_pipeline import preprocess_pipeline
from ml.preprocessing.feature_scaling import load_scaler
from ml.models.anomaly_detector import (
    load_anomaly_detector,
    predict_anomalies,
)


# File paths
BASE_DIR = Path(__file__).resolve().parents[2]

DATASET_PATH = BASE_DIR / "ml/datasets/raw/synthetic_can_training.csv"
MODEL_PATH = BASE_DIR / "ml/models/trained/isolation_forest.joblib"
SCALER_PATH = BASE_DIR / "ml/models/trained/feature_scaler.joblib"
OUTPUT_PATH = BASE_DIR / "ml/datasets/processed/inference_results.csv"


def run_inference(dataset_path=DATASET_PATH):

    # Step 1: Load the trained model
    model = load_anomaly_detector(str(MODEL_PATH))

    # Step 2: Load the scaler fitted during training
    scaler = load_scaler(str(SCALER_PATH))

    # Step 3: Preprocess incoming traffic using the saved scaler
    cleaned_data, features, _ = preprocess_pipeline(
        str(dataset_path),
        scaler=scaler,
    )

    # Step 4: Generate anomaly predictions and scores
    predictions = predict_anomalies(model, features)

    # Step 5: Combine predictions with original traffic information
    results = cleaned_data.loc[features.index].copy()

    results["prediction"] = predictions["prediction"]
    results["anomaly_score"] = predictions["anomaly_score"]
    results["is_anomaly"] = predictions["is_anomaly"]

    results["traffic_status"] = results["is_anomaly"].map({
        True: "Anomaly",
        False: "Normal",
    })

    # Step 6: Save inference results
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    results.to_csv(OUTPUT_PATH, index=False)

    print("\nInference completed successfully!")
    print("Total records:", len(results))
    print("Normal records:", int((~results["is_anomaly"]).sum()))
    print("Anomalous records:", int(results["is_anomaly"].sum()))
    print("Results saved to:", OUTPUT_PATH)

    return results


if __name__ == "__main__":
    inference_results = run_inference()
    print("\nPrediction results:")
    print(
        inference_results[
            ["ecu_id", "can_id", "prediction",
             "anomaly_score", "traffic_status"]
        ].to_string(index=False)
    )
