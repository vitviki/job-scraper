from pydantic import BaseModel, Field


class HealthCheckResponseSchema(BaseModel):
    status: str = Field(
        description="The status of the health check, typically 'ok' if everything is functioning properly."
    )
    environment: str = Field(
        description="Current running environment"
    )
    database: str = Field(
        description="Status of the database connection"
    )

    class Config:
        json_schema_extra = {
            "example": {
                "status": "ok",
                "environment": "development",
                "database": "connected"
            }
        }
