from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    'weather',
    bootstrap_servers=['localhost:9092'],
    value_deserializer=lambda v: json.loads(v.decode('utf-8')),
    auto_offset_reset='earliest',
    enable_auto_commit=True
)

cities = ["Moscow", "Saint Petersburg", "Krasnoyarsk", "Sochi", "Vladivostok"]
weather_data = []

for message in consumer:
    data = message.value
    if data["city"] in cities:
        weather_data.append(data)
        print(f"Received and processed: {data}")

    # Сохранение в файл, если получены данные из всех городов
    if len(weather_data) >= len(cities):
        with open('weather_data.json', 'w') as f:
            json.dump(weather_data, f, indent=4)
        print("Saved to weather_data.json")
        break