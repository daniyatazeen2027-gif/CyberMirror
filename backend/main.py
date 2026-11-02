from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.alerts import router as alerts_router

app = FastAPI(
    title="CyberMirror API",
    description="Backend API for the CyberMirror vehicle cybersecurity project",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
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
