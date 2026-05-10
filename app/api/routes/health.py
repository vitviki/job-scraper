from fastapi import APIRouter
from sqlalchemy import text

from app.db.database import engine
from app.core.config import settings
from app.schemas.health_schema import HealthCheckResponseSchema

router = APIRouter()


@router.get("/health", response_model=HealthCheckResponseSchema)
async def health_check():
    db_status = "disconnected"

    try:
        async with engine.connect() as connection:
            await connection.execute(text("SELECT 1"))
            db_status = "connected"
    except Exception as e:
        db_status = str(e)

    return {
        "status": "ok",
        "environment": settings.ENV,
        "database": db_status,

    }
