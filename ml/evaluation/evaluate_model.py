from ml.evaluation.metrics import calculate_classification_metrics


def evaluate_model(y_true, y_pred):
    """
    Evaluate a classification model using standard metrics.
    """

    if len(y_true) != len(y_pred):
        raise ValueError("Actual and predicted labels must have equal lengths.")

    if len(y_true) == 0:
        raise ValueError("Cannot evaluate an empty dataset.")

    results = calculate_classification_metrics(y_true, y_pred)

    print("MODEL EVALUATION RESULTS")
    print("-" * 30)

    for metric, value in results.items():
        print(f"{metric}: {value}")

    return results