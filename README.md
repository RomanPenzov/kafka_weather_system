# Kafka Weather System

## Описание проекта
**Kafka Weather System** — это система обработки сообщений, которая отправляет и обрабатывает данные о погодных условиях в реальном времени с использованием Apache Kafka. Проект включает:
- Генерацию сообщений о погоде продюсером.
- Обработку и сохранение сообщений потребителем.

Пример использования: мониторинг погоды в нескольких городах.

---

## Структура проекта

```
kafka_weather_system/
├── docker-compose.yml        # Конфигурация для запуска Apache Kafka и Zookeeper через Docker
├── producer.py               # Скрипт продюсера, отправляющего данные о погоде в Kafka
├── consumer.py               # Скрипт потребителя, обрабатывающего данные о погоде
├── weather_data.json         # Файл для сохранения обработанных данных о погоде
├── venv/                     # Виртуальное окружение Python (опционально)
└── README.md                 # Документация проекта
```

---

## Требования

- Python 3.8+
- Docker и Docker Compose
- Установленные библиотеки Python:
  - kafka-python

---

## Инструкция по запуску

### 1. Запуск кластера Kafka

1. Убедитесь, что Docker установлен и запущен на вашем устройстве.
2. В каталоге проекта выполните команду для запуска контейнеров Kafka и Zookeeper:
   ```bash
   docker-compose up -d
   ```
3. Убедитесь, что контейнеры работают:
   ```bash
   docker ps
   ```

4. Создайте топик `weather`:
   ```bash
   docker exec -it kafka_weather_system-kafka-1 kafka-topics --create --topic weather --bootstrap-server localhost:9092 --partitions 3
   ```

---

### 2. Настройка виртуального окружения

1. Создайте виртуальное окружение (опционально):
   ```bash
   python -m venv venv
   ```
2. Активируйте виртуальное окружение:
   - Windows:
     ```bash
     .\venv\Scripts\activate
     ```
   - Linux/MacOS:
     ```bash
     source venv/bin/activate
     ```
3. Установите зависимости:
   ```bash
   pip install kafka-python
   ```

---

### 3. Запуск продюсера и потребителя

1. Запустите продюсер:
   ```bash
   python producer.py
   ```
   Продюсер начнет отправлять случайные данные о погоде в топик `weather`.

2. В другом терминале запустите потребителя:
   ```bash
   python consumer.py
   ```
   Потребитель будет обрабатывать данные и сохранять их в файл `weather_data.json`.

---

## Пример выходных данных

Файл `weather_data.json` будет содержать сохраненные данные:
```json
[
    {
        "city": "Moscow",
        "temperature": -5,
        "condition": "cloudy"
    },
    {
        "city": "Saint Petersburg",
        "temperature": 2,
        "condition": "rainy"
    }
]
```

---

## Дополнительная информация

### Масштабируемость
- Топик `weather` имеет три раздела (partition).
- Можно запустить несколько экземпляров потребителей для увеличения производительности.

### Обработка ошибок
- В продюсере и потребителе реализуйте повторные попытки отправки/чтения сообщений в случае ошибок (можно использовать библиотеки или написать собственную логику).

---