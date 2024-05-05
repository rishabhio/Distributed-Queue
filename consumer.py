

from confluent_kafka import Consumer, KafkaError

# Kafka broker settings
bootstrap_servers = 'localhost:9092'
topic = 'test-topic'

# Create Kafka Consumer instance
conf = {'bootstrap.servers': bootstrap_servers, 'group.id': 'my-consumer-group'}
consumer = Consumer(conf)
consumer.subscribe([topic])

# Poll for messages
while True:
    msg = consumer.poll(1.0)
    if msg is None:
        continue
    if msg.error():
        if msg.error().code() == KafkaError._PARTITION_EOF:
            continue
        else:
            print(f'Consumer error: {msg.error()}')
            break
    print(f'Received message: {msg.value().decode("utf-8")}')

consumer.close()
