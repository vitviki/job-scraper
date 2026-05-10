from dotenv import load_dotenv
import os

load_dotenv()


class Settings:
    APP_NAME = os.getenv("APP_NAME", "Job Scraper")
    ENV = os.getenv("ENV", "development")
    DATABASE_URL = os.getenv("DATABASE_URL")
    DATABASE_ECHO = os.getenv(
        "DATABASE_ECHO", "False").lower() in ("true", "1", "t")


settings = Settings()
