from pydantic import BaseSettings


class BotSettings(BaseSettings):
    telegram_bot_key: str

    class Config:
        env_file = '.env'
