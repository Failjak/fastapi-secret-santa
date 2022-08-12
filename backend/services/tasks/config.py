from pydantic import BaseSettings


class CelerySettings(BaseSettings):

    name: str
    broker_url: str
    result_backend: str

    class Config:
        env_prefix = 'CELERY_'
        env_file = '.env'


config = CelerySettings()
