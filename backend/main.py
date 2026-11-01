
from fastapi import FastAPI

from app.api.alerts import router as alerts_router

app = FastAPI(
    title="CyberMirror API",
    description="Backend API for the CyberMirror vehicle cybersecurity project",
    version="0.1.0",
)

# Register the alerts API routes
app.include_router(alerts_router)


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "project": "CyberMirror",
        "message": "Backend is running successfully",
    }
