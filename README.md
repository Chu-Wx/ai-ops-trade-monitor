# 🧠 AI Ops Risk Reporter Demo

This project is a full-stack AI Ops risk-monitoring pipeline, combining **Kafka + GPT + SQLite + FastAPI** to simulate and analyze financial trade data in real time.

---

## 🚀 Features

✅ Kafka-powered streaming trade ingestion  
✅ Real-time risk flagging with rule-based engine  
✅ GPT-generated risk summary reports (OpenAI API)  
✅ PDF report generation and download  
✅ RESTful API built with FastAPI  
✅ Dry-run mode for cost-free testing  
✅ SQLite persistence for trades and logs  

---

## 📁 Project Structure

```
ai-ops-trade-monitor/
├── app/
│   ├── kafka_consumer.py         # Kafka consumer to process trade events
│   ├── main.py                   # FastAPI app entry point
│   ├── models.py                 # DB schema (if needed for expansion)
│   ├── pdf_generator.py          # PDF export logic
│   ├── report_generator.py       # GPT summary generation
├── sample_data/
│   └── sample_trade_stream.py    # Kafka producer simulator
├── report_output/                # Generated PDF reports
├── trades.db                     # SQLite database
├── docker-compose.yml           # Kafka + Zookeeper setup
├── requirements.txt
└── README.md
```

---

## 📦 Installation

1. **Clone the repo**  
```bash
git clone https://github.com/your-user/ai-ops-trade-monitor.git
cd ai-ops-trade-monitor
```

2. **Install dependencies**  
```bash
pip install -r requirements.txt
```

3. **Set up `.env`**  
Create a `.env` file with:
```
OPENAI_API_KEY=sk-...
```

4. **Start Kafka (via Docker)**  
```bash
docker compose up -d
```

5. **Start the backend service**
```bash
uvicorn app.main:app --reload
```

---

## ▶️ Usage

### ✅ Send Trade Events (Producer)
```bash
python sample_data/sample_trade_stream.py
```

### ✅ Run Consumer (Database Ingestion)
```bash
python app/kafka_consumer.py
```

### ✅ View Report (Dry-run)
Visit:  
[http://localhost:8000/report/today?dry_run=true](http://localhost:8000/report/today?dry_run=true)

### ✅ Download Report PDF
[http://localhost:8000/report/pdf?dry_run=true](http://localhost:8000/report/pdf?dry_run=true)

---

## 🔧 Configs

- Default Kafka topic: `trade-events`
- Database: `trades.db`
- Report output: `report_output/report_<date>.pdf`

---

## ✨ TODO Ideas

- [ ] Add scheduling (APScheduler)
- [ ] Email daily reports
- [ ] GPT-4 analysis per trader
- [ ] Web frontend with charts and flags
- [ ] Multi-user access control

---

## 🧠 Credits

Built by Chuwei, powered by FastAPI, Kafka, OpenAI, and Python 🚀