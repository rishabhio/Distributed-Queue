

from confluent_kafka import Producer

# Kafka broker settings
bootstrap_servers = 'localhost:9092'
topic = 'test-topic'

# Create Kafka Producer instance
conf = {'bootstrap.servers': bootstrap_servers}
producer = Producer(conf)

# Define a callback function to handle delivery reports
def delivery_callback(err, msg):
    if err:
        print(f'Message delivery failed: {err}')
    else:
        print(f'Message delivered to topic {msg.topic()} [partition {msg.partition()}]')

# Publish a message to the Kafka topic
message = 'Hello, Kafka!'
producer.produce(topic, value=message, callback=delivery_callback)

# Wait for the message to be delivered
producer.flush()


