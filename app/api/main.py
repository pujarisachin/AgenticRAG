from fastapi import FastAPI
from app.core.config import get_settings
from app.core.logging import setup_logging,get_logger

settings = get_settings()

setup_logging(settings.log_level)
logger = get_logger(__name__)

app = FastAPI(
    title=settings.app_name,
    version= "1.0.0"
)

@app.get("/health",tags=["System"])
def health_check():
    logger.info("Health check end point is called")
    return{
        "status": "ok",
        "environment": settings.log_level
    }