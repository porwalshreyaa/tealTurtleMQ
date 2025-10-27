from src.tealTurtle import Consumer
import json

# this is how we plan to init and create consumer object
# consumer = Consumer('orders', servers=['localhost:9092'], value_deserializer=lambda v: json.dumps(v).encode('utf-8'))

# for message in consumer:
#     print("Got event:", message.value)
