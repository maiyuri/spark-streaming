from kafka import KafkaProducer
from random import random, randint
from datetime import datetime
import json

bootstrap_servers = ['localhost:9092']
topicName = 'test'
producer = KafkaProducer(bootstrap_servers=bootstrap_servers)
key = None

headers = []

def gen_msg(qtd_msg):
    msgs = []
    for i in range(qtd_msg):
        msgs.append({
            'codigo_cliente': i,
            'agencia': '00019',
            'valor_operacao': random() * 100,
            'tipo_operacao': ['DEPOSITO', 'SAQUE'][randint(0,1)],
            'data': datetime.now().isoformat(),
            'saldo_conta': random() * 150
        })
    return msgs

for msg in gen_msg(10):
    message_data = json.dumps(msg).encode('utf-8')
    # Send the serialized message to the Kafka topic
    producer.send(topicName, message_data, key, headers)
    

producer.flush()