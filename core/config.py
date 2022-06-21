from dotenv import dotenv_values

values = dotenv_values()


class Settings:
    """ Class with setting to project and Postgres DB """

    PROJECT_NAME: str = "Secret Santa (FastAPI)"
    PROJECT_VERSION: str = "1.0.0"

    POSTGRES_USER: str = values.get("POSTGRES_USER")
    POSTGRES_PASSWORD = values.get("POSTGRES_PASSWORD")
    POSTGRES_SERVER: str = values.get("POSTGRES_SERVER", "localhost")
    POSTGRES_PORT: str = values.get("POSTGRES_PORT", 5432)
    POSTGRES_DB: str = values.get("POSTGRES_DB", "fastapi_db")
    DATABASE_URL = f"postgresql://" \
                   f"{POSTGRES_USER}:{POSTGRES_PASSWORD}@" \
                   f"{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"


settings = Settings()
