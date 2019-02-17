from confluent_kafka import Producer, Consumer, KafkaError, TopicPartition


def consume_messages(topics, config):
    try:
        consumer = Consumer(config)
        consumer.subscribe(topics)
        while True:
            msg = consumer.poll()
            if msg is None:
                continue
            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    continue
                else:
                    print(msg.error())
                    break
            return bytes(msg.value())
    finally:
        consumer.close()


def __delivery_report(err, msg):
    """ Called once for each message produced to indicate delivery result.
        Triggered by poll() or flush(). """
    if err is not None:
        print('Message delivery failed: {}'.format(err))
    else:
        print('Message delivered to {} [{}]'.format(msg.topic(), msg.partition()))


def publish_message(config, topic, message):
    producer = Producer(config)
    producer.poll(0)
    producer.produce(topic=topic, value=message, callback=__delivery_report)
    producer.flush()
