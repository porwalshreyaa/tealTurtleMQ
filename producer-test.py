from src.tealTurtle import Producer
import json

# this is how we plan to init and create producer object
producer = Producer(servers=['localhost:9092'], value_serializer=lambda v: json.dumps(v).encode('utf-8'))

event = {
    "eventType": "orderCreated",
    "data": {
        "orderId": 123,
        "userId": 45
    }
}

producer.send("orders", event)
producer.flush()