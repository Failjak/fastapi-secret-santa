from pydantic import BaseSettings, Field


class QueueSettings(BaseSettings):

    username: str = Field(..., env='RABBITMQ_DEFAULT_USER')
    password: str = Field(..., env='RABBITMQ_DEFAULT_PASS')
    port: int
    host: str
    queue_name: str

    class Config:
        env_prefix = 'RABBITMQ_'
        env_file = '.env'


config = QueueSettings()
