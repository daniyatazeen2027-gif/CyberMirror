
from datetime import datetime, timezone
from uuid import uuid4


def create_alert(event):
    return {
        "alert_id": str(uuid4()),
        "timestamp": event.get(
            "timestamp",
            datetime.now(timezone.utc).isoformat()
        ),
        "severity": event.get("severity", "low"),
        "attack_type": event.get("attack_type", "unknown"),
        "source": event.get("source", "vehicle_network_simulator"),
        "description": event.get("description", "Simulated vehicle event"),
        "ecu_id": event.get("ecu_id", "unknown"),
        "risk_score": event.get("risk_score", 0),
        "status": event.get("status", "new")
    }


if __name__ == "__main__":
    sample_event = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "ecu_id": "Gateway_ECU",
        "attack_type": "can_spoofing",
        "source": "vehicle_network_simulator",
        "description": "Simulated CAN spoofing event",
        "severity": "high",
        "risk_score": 85,
        "status": "new"
    }

    print("CyberMirror structured alert:")
    print(create_alert(sample_event))
