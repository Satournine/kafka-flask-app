from kafka import KafkaConsumer
import json


def save_file(filename):
    consumer = KafkaConsumer(
        'scraped-data',
        bootstrap_servers='localhost:9092',
        auto_offset_reset='earliest',
        enable_auto_commit=True,
        group_id='my_group',
        value_deserializer=lambda x: json.loads(x.decode('utf-8'))
    )

    with open(filename, 'w') as file:
        for message in consumer:
            file.write(json.dumps(message.value) + "\n")
            print(f'saved to file: {message.value}')
            file.flush()

    print("File writing complete.")
