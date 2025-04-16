from kafka import KafkaProducer
import json
import time

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

trades = [
    {"trade_id": "TX1002", "symbol": "TSLA", "amount": 80000, "price": 720.5},
    {"trade_id": "TX1003", "symbol": "GOOGL", "amount": 20000, "price": 2825.0},
    {"trade_id": "TX1004", "symbol": "META", "amount": 120000, "price": 310.3},
]

for trade in trades:
    trade["timestamp"] = time.strftime("%Y-%m-%dT%H:%M:%S")
    producer.send('trade-events', value=trade)
    time.sleep(1)


producer.send('trade-events', value=trades)
producer.flush()
print("✅ Sent trade event to Kafka.")
