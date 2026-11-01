
from uuid import uuid4

from fastapi import APIRouter, HTTPException, status

from app.schemas.alert import AlertCreate, AlertResponse
from app.utils.database import get_db_connection

router = APIRouter(prefix="/api/v1/alerts", tags=["Alerts"])


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=AlertResponse,
)
def create_alert(alert: AlertCreate):
    alert_id = uuid4()
    alert_data = alert.model_dump()

    query = """
        INSERT INTO alerts (
            alert_id, timestamp, severity, attack_type,
            source, description, ecu_id, risk_score, status
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        RETURNING alert_id, timestamp, severity, attack_type,
                  source, description, ecu_id, risk_score, status
    """

    try:
        with get_db_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    query,
                    (
                        alert_id,
                        alert_data["timestamp"],
                        alert_data["severity"],
                        alert_data["attack_type"],
                        alert_data["source"],
                        alert_data["description"],
                        alert_data["ecu_id"],
                        alert_data["risk_score"],
                        "open",
                    ),
                )
                row = cur.fetchone()

        return {
            "alert_id": str(row[0]),
            "timestamp": row[1].isoformat(),
            "severity": row[2],
            "attack_type": row[3],
            "source": row[4],
            "description": row[5],
            "ecu_id": row[6],
            "risk_score": row[7],
            "status": row[8],
        }

    except Exception as exc:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Could not save alert to the database",
        ) from exc


@router.get("/", response_model=list[AlertResponse])
def get_all_alerts():
    query = """
        SELECT alert_id, timestamp, severity, attack_type,
               source, description, ecu_id, risk_score, status
        FROM alerts
        ORDER BY timestamp DESC
    """

    try:
        with get_db_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(query)
                rows = cur.fetchall()

        return [
            {
                "alert_id": str(row[0]),
                "timestamp": row[1].isoformat(),
                "severity": row[2],
                "attack_type": row[3],
                "source": row[4],
                "description": row[5],
                "ecu_id": row[6],
                "risk_score": row[7],
                "status": row[8],
            }
            for row in rows
        ]

    except Exception as exc:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Could not retrieve alerts from the database",
        ) from exc


@router.get("/{alert_id}", response_model=AlertResponse)
def get_alert(alert_id: str):
    query = """
        SELECT alert_id, timestamp, severity, attack_type,
               source, description, ecu_id, risk_score, status
        FROM alerts
        WHERE alert_id = %s
    """

    try:
        with get_db_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(query, (alert_id,))
                row = cur.fetchone()

    except Exception as exc:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Could not retrieve alert from the database",
        ) from exc

    if row is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Alert not found",
        )

    return {
        "alert_id": str(row[0]),
        "timestamp": row[1].isoformat(),
        "severity": row[2],
        "attack_type": row[3],
        "source": row[4],
        "description": row[5],
        "ecu_id": row[6],
        "risk_score": row[7],
        "status": row[8],
    }
