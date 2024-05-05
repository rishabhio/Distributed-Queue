# Distributed-Queue
Let's Learn Kafka Distributed Queue by Exploring its functionality. 


# Producer 

```
from confluent_kafka import Producer
```
This line imports the Producer class from the confluent_kafka module. This class is used to create a Kafka producer instance.

# Kafka broker settings
```
bootstrap_servers = 'localhost:9092'
topic = 'test-topic'
```
These lines define the Kafka broker's address (bootstrap_servers) and the topic to which the message will be published (topic).

# Create Kafka Producer instance

```
conf = {'bootstrap.servers': bootstrap_servers}
producer = Producer(conf)
```

Here, a configuration dictionary (conf) is created with the specified bootstrap servers. Then, a Kafka producer instance is created using this configuration.


# Define a callback function to handle delivery reports

```
def delivery_callback(err, msg):
    if err:
        print(f'Message delivery failed: {err}')
    else:
        print(f'Message delivered to topic {msg.topic()} [partition {msg.partition()}]')
```


This section defines a callback function (delivery_callback) that will be invoked after each message delivery attempt. It checks if there's any error (err) and prints a message indicating whether the message was successfully delivered or not.


# Publish a message to the Kafka topic

```
message = 'Hello, Kafka!'
producer.produce(topic, value=message, callback=delivery_callback)

```


Here, a message ('Hello, Kafka!') is defined, and the produce() method of the Kafka producer instance is called to publish this message to the specified topic. The callback parameter is used to specify the delivery callback function defined earlier.

# Wait for the message to be delivered

```
producer.flush()

```


Finally, the flush() method is called on the producer to ensure that all messages are delivered before the program exits. This waits until all messages have been delivered to Kafka or until the specified timeout period expires.


# Consumer 

```
from confluent_kafka import Consumer, KafkaError
```

This line imports the Consumer class and the KafkaError class from the confluent_kafka module. The Consumer class is used to create a Kafka consumer instance, and the KafkaError class represents errors that may occur during Kafka operations.

# Kafka broker settings
```
bootstrap_servers = 'localhost:9092'
topic = 'test-topic'
```

These lines define the Kafka broker's address (bootstrap_servers) and the topic from which the consumer will consume messages (topic).

# Create Kafka Consumer instance

```
conf = {'bootstrap.servers': bootstrap_servers, 'group.id': 'my-consumer-group'}
consumer = Consumer(conf)
consumer.subscribe([topic])
```

Here, a configuration dictionary (conf) is created with the specified bootstrap servers and consumer group ID. Then, a Kafka consumer instance is created using this configuration, and it subscribes to the specified topic.


# Poll for messages

```
while True:
    msg = consumer.poll(1.0)
    if msg is None:
        continue

```


This section starts a loop where the consumer continuously polls for messages from the subscribed topic. The poll() method is called with a timeout of 1.0 second. If no message is available within this timeout, it continues to the next iteration of the loop.

```
    if msg.error():
        if msg.error().code() == KafkaError._PARTITION_EOF:
            continue
        else:
            print(f'Consumer error: {msg.error()}')
            break
```


If an error occurs while consuming messages, this section checks if it's an end-of-partition event (KafkaError._PARTITION_EOF). If so, it continues to the next iteration of the loop. Otherwise, it prints the error message and breaks out of the loop.

```
    print(f'Received message: {msg.value().decode("utf-8")}')

```


If no error occurs and a message is successfully received, this line prints the message value to the console after decoding it from bytes to a UTF-8 string.

```
consumer.close()

```


Finally, the close() method is called on the consumer to gracefully close the consumer instance and release any associated resources.






