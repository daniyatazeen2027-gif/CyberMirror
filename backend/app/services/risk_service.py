
from app.services.graph_service import get_ecu_criticality


def classify_risk(risk_score: int) -> str:
    """
    LOW: 0-24
    MEDIUM: 25-49
    HIGH: 50-74
    CRITICAL: 75-100
    """

    if not isinstance(risk_score, int) or isinstance(risk_score, bool):
        raise TypeError("Risk score must be an integer")

    if not 0 <= risk_score <= 100:
        raise ValueError("Risk score must be between 0 and 100")

    if risk_score < 25:
        return "low"
    elif risk_score < 50:
        return "medium"
    elif risk_score < 75:
        return "high"
    else:
        return "critical"


def calculate_risk_score(
    threat_severity: int,
    ecu_criticality: int
) -> int:
    """
    Threat severity weight: 60%
    ECU criticality weight: 40%
    """

    for name, value in {
        "threat_severity": threat_severity,
        "ecu_criticality": ecu_criticality,
    }.items():
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError(f"{name} must be an integer")

        if not 0 <= value <= 100:
            raise ValueError(f"{name} must be between 0 and 100")

    score = (0.6 * threat_severity) + (0.4 * ecu_criticality)

    return round(score)


def classify_attack_type(
    is_anomaly: bool,
    message_frequency: float,
    inter_arrival_time: float
) -> str:
    """
    Provisionally classify anomalous CAN traffic.
    Thresholds are based on the current synthetic dataset.
    """

    if not isinstance(is_anomaly, bool):
        raise TypeError("is_anomaly must be a boolean")

    if message_frequency < 0 or inter_arrival_time < 0:
        raise ValueError("Traffic measurements cannot be negative")

    if not is_anomaly:
        return "NORMAL"

    if message_frequency >= 100 and inter_arrival_time <= 0.01:
        return "CAN_FLOODING"

    return "UNKNOWN_ANOMALY"


def get_threat_severity(attack_type: str) -> int:
    """
    Return provisional threat severity for each attack type.
    """

    severity_mapping = {
        "NORMAL": 0,
        "UNKNOWN_ANOMALY": 50,
        "CAN_FLOODING": 85,
    }

    if attack_type not in severity_mapping:
        raise ValueError(f"Unsupported attack type: {attack_type}")

    return severity_mapping[attack_type]


def analyze_traffic_risk(
    ecu_id: str,
    is_anomaly: bool,
    message_frequency: float,
    inter_arrival_time: float
) -> dict:
    """
    Classify traffic and calculate its risk using
    threat severity and ECU criticality from Neo4j.
    """

    attack_type = classify_attack_type(
        is_anomaly,
        message_frequency,
        inter_arrival_time
    )

    # Normal traffic should not generate a security risk.
    if attack_type == "NORMAL":
        return {
            "ecu_id": ecu_id,
            "attack_type": attack_type,
            "threat_severity": 0,
            "ecu_criticality": None,
            "risk_score": 0,
            "severity": "low",
        }

    ecu_data = get_ecu_criticality(ecu_id)

    if ecu_data is None or ecu_data["criticality"] is None:
        raise ValueError(
            f"Criticality not found for ECU: {ecu_id}"
        )

    threat_severity = get_threat_severity(attack_type)
    ecu_criticality = ecu_data["criticality"]

    risk_score = calculate_risk_score(
        threat_severity,
        ecu_criticality
    )

    return {
        "ecu_id": ecu_id,
        "attack_type": attack_type,
        "threat_severity": threat_severity,
        "ecu_criticality": ecu_criticality,
        "risk_score": risk_score,
        "severity": classify_risk(risk_score),
    }
