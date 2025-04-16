import os
from fastapi import FastAPI, Query
from fastapi.responses import FileResponse
from app.report_generator import get_today_trades, generate_report
from app.pdf_generator import generate_pdf


app = FastAPI()

@app.get("/")
def home():
    return {"msg": "Welcome to AI Risk Reporter API 🎯"}

@app.get("/report/today")
def get_today_report(dry_run: bool = Query(True, description="Enable dry run to avoid GPT billing")):
    trades = get_today_trades()
    report = generate_report(trades, dry_run=dry_run)

    return {
        "date": trades[0]["timestamp"].split("T")[0] if trades else None,
        "trade_count": len(trades),
        "dry_run": dry_run,
        "report": report
    }
@app.get("/report/pdf")
def download_report_as_pdf(dry_run: bool = Query(True)):
    print("🚀 /report/pdf called with dry_run =", dry_run)
    trades = get_today_trades()
    print(f"📦 Found {len(trades)} trades")
    report = generate_report(trades, dry_run=dry_run)
    print("🧾 Report generated")
    filepath = generate_pdf(report)
    print("📄 PDF saved to", filepath)
    return FileResponse(filepath, media_type='application/pdf', filename=os.path.basename(filepath))
