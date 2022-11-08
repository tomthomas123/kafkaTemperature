import time
from kafka import KafkaProducer
import random

bootstrap_server = ["localhost:9092"]
topic = "temperature"
producer = KafkaProducer(bootstrap_servers = bootstrap_server)
producer = KafkaProducer()

def senddata():
    temp_data =random.randint(0,40)
    message = producer.send(topic,bytes(str(temp_data),"utf-8"))
    metadata = message.get()
    print(metadata.topic)
    print(metadata.partition)
    time.sleep(5)
while True:
    senddata()