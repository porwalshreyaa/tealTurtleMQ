# what is an event? User sign up? okay let's create an event
from datetime import datetime
import pytz

# Ideal event example - where data and meta data are nested dicts

# {
#     "eventType": "OrderCreated",
#     "timestamp": "2025-10-25....",
#     "data": {
#         "orderId": 125,
#         "userId": 45,
#         "amount": 1999.99
#     },
#     "metadata": {
#         "source": "orderService",
#         "traceId": "abc-123"
#     }
# }


class Event:
    eventType = None
    timestamp = None
    data = None
    metadata = None
    # dummy event create
    def __init__(self, event_type, data, metadata):
        currentTime = datetime.now()
        tz = pytz.timezone('Asia/Kolkata')
        self.timestamp = tz.localize(currentTime)
        self.eventType = event_type
        self.data = data
        self.metadata = metadata
    def returnEvent(self):
        return {"eventType": self.eventType, "timestamp": self.timestamp, "data": self.data, "metadata": self.metadata}



class MessageProducer:
    # sends post req to broker with event and data args to add the event into topic queue
    def __init__(self):
        # self.topics = {}
        pass
    pass
    # def create_topic(self, name):
    #     self.topics[name] = Queue()

    # def publish(self, topic, message):
    #     if topic in self.topics:
    #         self.topics[topic].put(message)
    #         # put message into that topic/queue
    #         print(f"[BROKER] Published to {topic}: {message}")
    #     else:
    #         print(f"[BROKER] Topic '{topic}' not found")
    # def consume(self, topic):
    #     if topic in self.topics and not self.topics[topic].empty():
    #         message = self.topics[topic].get()
    #         print(f"[BROKER] Delivering message from {topic}")
    #         return message
    #     return None
    # created event/msg, encodes/serializes it
    # sends msg to broker along with topic
event1 = Event("orders", {"orderId": 743, "userId": 834, "amount": 999}, {"source": "orderService", "traceId": "oic-85392"})

print(event1.returnEvent())