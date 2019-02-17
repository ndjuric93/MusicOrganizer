from kafka import KafkaProducer
from kafka import KafkaConsumer

class TopicProducer:

    def __init__(self, config, topic):
        self.producer = KafkaProducer(**config)
        self.topic = topic

    def produce(self, message):
        self.producer.send(value=message, topic=self.topic)

    # def __enter__(self):
    #     return self

    # def __exit__(self, exc_type, exc_val, exc_tb):
    #     self.producer.poll(0)


class TopicConsumer:

    def __init__(self, config, topics=()):
        self.consumer = KafkaConsumer(**config)
        self.topics = topics

    def __enter__(self):
        self.consumer.subscribe(self.topics)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.consumer.close()