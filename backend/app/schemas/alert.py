
from datetime import datetime
from typing import Literal

from pydantic import BaseModel, Field


class AlertCreate(BaseModel):
    timestamp: datetime
    severity: Literal["low", "medium", "high", "critical"]
    attack_type: str
    source: str
    description: str
    ecu_id: str
    risk_score: int = Field(ge=0, le=100)


class AlertResponse(BaseModel):
    alert_id: str
    timestamp: datetime
    severity: Literal["low", "medium", "high", "critical"]
    attack_type: str
    source: str
    description: str
    ecu_id: str
    risk_score: int = Field(ge=0, le=100)
    status: str
