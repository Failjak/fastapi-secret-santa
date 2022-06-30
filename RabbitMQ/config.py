from dotenv import dotenv_values

values = dotenv_values()


class Config:
    RABBITMQ_USERNAME: str = values.get('RABBITMQ_DEFAULT_USER', 'rabbit')
    RABBITMQ_PASSWORD: str = values.get('RABBITMQ_DEFAULT_PASS', 'rabbit')
    RABBITMQ_PORT: str = values.get('RABBITMQ_PORT', '5672')
    RABBITMQ_HOST: str = values.get('RABBITMQ_HOST', '0.0.0.0')
    RABBITMQ_QUEUE_NAME: str = values.get('RABBITMQ_QUEUE_NAME', 'users')


config = Config()
