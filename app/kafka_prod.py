import json
import time
from kafka import KafkaProducer

from app import webScraper


def send_kafka(topic):
    try:
        producer = KafkaProducer(
            bootstrap_servers='localhost:9092',
            value_serializer=lambda x: json.dumps(x).encode('utf-8')
        )
    except Exception as e:
        print(f'kafka connection: {e}')
        return
    try:
        data = webScraper.web_scraper()
        for item in data:
            producer.send(topic, item)
            print(f"sent: {item}")
            time.sleep(1)
    except Exception as e:
        print(f'sending msg kafka: {e}')