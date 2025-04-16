# AI Risk & Compliance Reporter

A lightweight AI-enhanced microservice for ingesting trade data (Kafka), performing risk scoring, and auto-generating daily compliance reports using GPT-4.

## 💼 Stack
- FastAPI + Python
- SQLite / OracleDB
- Kafka (simulated)
- OpenAI API + LangChain (optional)

## 🚀 How It Works
1. Kafka receives trade events
2. Consumer processes events → risk score → store to DB
3. Scheduler triggers GPT to summarize report daily
4. Report available via API or frontend dashboard

## 📄 API Endpoint

- `GET /report/daily` → latest AI-generated report
