from app import kafka_prod
from app import kafka_consume
from app import service
import threading


def run_flask():
    service.app.run(host='0.0.0.0')


def main():
    kafka_prod.send_kafka('scraped-data')
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.start()
    kafka_consume.save_file('kafka_scraped_data.json')
    flask_thread.join()


if __name__ == "__main__":
    main()
