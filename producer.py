from kafka import KafkaProducer
import json
import time
import random

producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

cities = ["Moscow", "Saint Petersburg", "Krasnoyarsk", "Sochi", "Vladivostok"]
conditions = ["sunny", "rainy", "cloudy", "snowy", "windy"]

while True:
    message = {
        "city": random.choice(cities),
        "temperature": random.randint(-30, 35),
        "condition": random.choice(conditions)
    }
    producer.send('weather', value=message)
    print(f"Sent: {message}")
    time.sleep(1)