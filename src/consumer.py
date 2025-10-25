class MessageConsumer:
    def __init__(self):
        # self.topics = {}
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


    # waits for topic and msg in it. receive msg, decodes/deserializes it
    # if received, send ack to broker