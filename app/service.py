from flask import Flask, jsonify
import json

app = Flask(__name__)


def load_data(filename):
    with open(filename, 'r') as file:
        data = [json.loads(line) for line in file]
    return data


@app.route('/', methods=['GET'])
def get_data():
    data = load_data('kafka_scraped_data.json')
    return jsonify(data)
