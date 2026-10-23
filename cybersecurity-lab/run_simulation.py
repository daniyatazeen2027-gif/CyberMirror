import json
from vehicle_simulator import generate_vehicle_event
from alert_generator import create_alert

for _ in range(5):
    event = generate_vehicle_event()
    alert = create_alert(event)
    print(json.dumps(alert, indent=2))
    print("-" * 40)

