from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    """ Class with setting to project and Postgres DB """

    project_name: str = "Secret Santa (FastAPI)"
    version: str = "1.0.0"

    user: str
    password: str
    server: str
    port: int
    db_name: str
    database_url: str = Field(..., env='DATABASE_URL')

    class Config:
        env_file = '.env'
        env_prefix = 'POSTGRES_'


settings = Settings(_env_file='.env')
