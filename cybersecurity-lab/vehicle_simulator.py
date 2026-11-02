
import json
import random
from datetime import datetime, timezone


ECUS = ["Engine_ECU", "Brake_ECU", "Gateway_ECU"]


def generate_vehicle_event():
    attack_type = random.choice([
        "normal_traffic",
        "can_spoofing",
        "replay_attack",
        "simulated_dos",
        "suspicious_gateway_traffic"
    ])

    event = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "ecu_id": random.choice(ECUS),
        "attack_type": attack_type,
        "source": "vehicle_network_simulator",
        "description": "",
        "severity": "low",
        "risk_score": 10,
        "status": "new"
    }

    if attack_type == "normal_traffic":
        event["description"] = "Normal simulated ECU communication."

    elif attack_type == "can_spoofing":
        event["description"] = "Simulated CAN message with an unexpected sender."
        event["severity"] = "high"
        event["risk_score"] = 85

    elif attack_type == "replay_attack":
        event["description"] = "Simulated replay of a previously observed CAN message."
        event["severity"] = "high"
        event["risk_score"] = 80

    elif attack_type == "simulated_dos":
        event["description"] = "Simulated burst of CAN messages."
        event["severity"] = "critical"
        event["risk_score"] = 95

    elif attack_type == "suspicious_gateway_traffic":
        event["description"] = "Simulated unexpected traffic through the vehicle gateway."
        event["severity"] = "medium"
        event["risk_score"] = 60

    return event


if __name__ == "__main__":
    print("CyberMirror Vehicle Network Simulator")
    print("Generating 5 synthetic events...\n")

    for _ in range(5):
        print(json.dumps(generate_vehicle_event(), indent=2))
        print("-" * 40)
