from datetime import datetime
import pytz, random, json, base64, os
tz = pytz.timezone('Asia/Kolkata')
def current_time():
    currentTime = datetime.now()
    return tz.localize(currentTime)

def generate_id(role:str):
    created_at = str(current_time())
    # return (role + str(base64.b64encode(created_at.encode("ascii")).decode("ascii")))
    return (role[0] +"-"+ str(base64.b64encode(created_at.encode("utf-8")).rstrip(b'=').decode('utf-8')))




class Producer:
    def __init__(self, broker):
        self.broker = broker
        self.producer_id = generate_id("producer")
        print(f"{self.producer_id} initialized as Producer.")
        return
    def connect_broker(self):
        if self.broker.connect("Producer", self.producer_id):
            print("[Producer] Connection Established with broker")
            return
    def send(self, event):
        pass



# a new broker has stored lists of producers, consumers and event queue in disk
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
class Broker:
    def __init__(self):
        current_directory = os.path.dirname(os.path.abspath(__file__))
        self.file_path = os.path.join(current_directory, "broker.json")
        print(self.file_path)
        if os.path.exists(self.file_path):
            with open(self.file_path, "r") as f:
                try:
                    self.broker_data = json.load(f)
                except json.JSONDecodeError:
                    self.broker_data = {
                        "producers": [],
                        "consumers": [],
                        "queue": []
                    }
        else:
            self.broker_data = {
                "producers": [],
                "consumers": [],
                "queue": []
            }

        print("[Broker] Broker initialized.")

    def store_data(self, data_obj, storage):
        pass

    def _save(self):
        """Helper to persist current broker data safely"""
        with open(self.file_path, "w") as f:
            json.dump(self.broker_data, f, indent=4)

    def connect(self,role, id):
        """Register a Producer or Consumer, but don't lose existing data."""
        if role == "Producer":
            if id not in self.broker_data["producers"]:
                self.broker_data["producers"].append(id)
        elif role == "Consumer":
            if id not in self.broker_data["consumers"]:
                self.broker_data["consumers"].append(id)
        else:
            print(f"[Broker] Invalid role: {role}")
            return 0

        self._save()
        print(f"[Broker] {role} '{id}' added to connection database.")
        return 1



    def receive(self, event,topic):
        if topics[topic]:
            topics[topic].append(event)
        else:
            topics[topic] = []
            topics[topic].append(event)




    def deliver(self):
        if  Consumer.receive():
            return "[Broker] Delivered Successfully"
        else:
            count +=1
    pass


class Consumer:
    def __init__(self, broker):
        self.broker = broker
        self.consumer_id = generate_id("consumer")
        print(f"{self.consumer_id} initialized as Consumer.")
        return
    def connect_broker(self):
        if self.broker.connect("Consumer", self.consumer_id):
            print("[Consumer] Connection Established with broker")
            return
    def receive():
        availability = random.choices([0,1])
        if availability[0] ==1:
            return 1
        return 0
    pass

broker = Broker()
producer1 = Producer(broker)
producer1.connect_broker()
consumer1 = Consumer(broker)
consumer1.connect_broker()