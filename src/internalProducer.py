from broker import MessageBroker

broker = MessageBroker()
broker.create_topic("orders")

# Producer sends message
broker.publish("orders", {"event": "OrderCreated", "orderId":123})