from kafka import KafkaProducer, KafkaConsumer
from json import loads
import json
import pickle


def kfk(request):
    producer = KafkaProducer(bootstrap_servers='kafka1:9091')
    v = {
        'msg': {
            'hello': 'world'
        }
    }
    serialized_data = pickle.dumps(v, pickle.HIGHEST_PROTOCOL)
    res = producer.send('Ptopic', serialized_data)
    return res


def cons(request):
    consumer = KafkaConsumer(
        'Ptopic',
        bootstrap_servers=['localhost:9092'],
        api_version=(0, 10)
    )

    for message in consumer:
        deserialized_data = pickle.loads(message.value)
        print(deserialized_data)
