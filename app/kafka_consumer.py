from kafka import KafkaConsumer
import json
import sqlite3
from datetime import datetime

# 设置 Kafka 消费者
consumer = KafkaConsumer(
    'trade-events',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='risk-analyzer-group',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

# 连接数据库（第一次会自动创建）
conn = sqlite3.connect("trades.db")
cursor = conn.cursor()

# 建表（如果不存在）
cursor.execute('''
CREATE TABLE IF NOT EXISTS trades (
    trade_id TEXT PRIMARY KEY,
    symbol TEXT,
    amount REAL,
    price REAL,
    timestamp TEXT,
    risk_level TEXT
)
''')
conn.commit()

print("✅ Kafka Consumer is listening for trade-events...")

# 消费数据
for message in consumer:
    payload = message.value
    print(f"📥 Received message: {payload}")

    # 如果是一组交易（列表），逐条处理
    if isinstance(payload, list):
        trades = payload
    else:
        trades = [payload]

    for trade in trades:
        amount = trade.get("amount", 0)
        risk_level = "HIGH" if amount > 50000 else "LOW"

        try:
            cursor.execute('''
            INSERT INTO trades (trade_id, symbol, amount, price, timestamp, risk_level)
            VALUES (?, ?, ?, ?, ?, ?)
            ''', (
                trade['trade_id'],
                trade['symbol'],
                trade['amount'],
                trade['price'],
                trade['timestamp'],
                risk_level
            ))
            conn.commit()
            print(f"✅ Stored trade {trade['trade_id']} with risk level: {risk_level}")
        except sqlite3.IntegrityError:
            print(f"⚠️  Trade {trade['trade_id']} already exists, skipped.")
