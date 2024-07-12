# Kafka-Flask-App

This project integrates a web scraper with Kafka and Flask. The scraper collects data, sends it to Kafka, and Flask serves the data through a REST API. The application is containerized using Docker.

## Features

- Web scraping with BeautifulSoup
- Kafka producer and consumer integration
- Flask REST API
- Docker containerization

## Getting Started

### Prerequisites

- Docker
- Docker Compose

### Installation

1. Clone the repository:
   git clone https://github.com/your-username/kafka-flask-app.git
   cd kafka-flask-app

2. Build and start the Docker containers:
   docker-compose build
   docker-compose up

3. Access the Flask application at:

  http://localhost:5000
