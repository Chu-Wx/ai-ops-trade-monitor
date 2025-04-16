import sqlite3
from datetime import datetime
import os
from dotenv import load_dotenv
from openai import OpenAI

# 加载 .env 文件
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# 初始化 OpenAI 客户端
client = OpenAI(api_key=api_key)

def get_today_trades():
    conn = sqlite3.connect("trades.db")
    cursor = conn.cursor()

    today = datetime.today().strftime('%Y-%m-%d')
    cursor.execute("SELECT * FROM trades WHERE timestamp LIKE ?", (f"{today}%",))
    rows = cursor.fetchall()
    conn.close()

    trades = []
    for row in rows:
        trades.append({
            "trade_id": row[0],
            "symbol": row[1],
            "amount": row[2],
            "price": row[3],
            "timestamp": row[4],
            "risk_level": row[5],
        })
    return trades

def generate_report(trades: list, dry_run=True) -> str:
    if not trades:
        return "No trades found for today."

    if dry_run:
        return f"""🧪 [Dry Run Mode]
共有 {len(trades)} 笔交易。
其中高风险交易 {sum(t['amount'] > 50000 for t in trades)} 笔。
总交易金额为 ${sum(t['amount'] for t in trades):,.2f}。
（此为模拟报告，未调用 GPT）"""

    # 实际调用 GPT
    summary_prompt = f"""
你是一名金融风控分析员。以下是今天的交易记录：

{trades}

请生成一份简洁的合规与风险摘要报告，包含：
1. 交易数量
2. 高风险交易概览（金额大于 $50,000）
3. 总交易金额
4. 一句话风险总结
    """

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "你是经验丰富的风控合规分析师"},
            {"role": "user", "content": summary_prompt}
        ]
    )

    return response.choices[0].message.content


if __name__ == "__main__":
    trades = get_today_trades()
    report = generate_report(trades, dry_run=True)  # ← 开启 Dry Run
    print("\n📄 今日风控报告摘要：\n")
    print(report)