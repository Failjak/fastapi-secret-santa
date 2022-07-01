from dotenv import dotenv_values

values = dotenv_values()


class Config:
    USERNAME: str = values.get('RABBITMQ_DEFAULT_USER', 'rabbit')
    PASSWORD: str = values.get('RABBITMQ_DEFAULT_PASS', 'rabbit')
    PORT: int = values.get('RABBITMQ_PORT', 5672)
    HOST: str = values.get('RABBITMQ_HOST', '0.0.0.0')
    QUEUE_NAME: str = values.get('RABBITMQ_QUEUE_NAME', 'users')


config = Config()
