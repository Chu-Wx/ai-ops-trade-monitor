from fpdf import FPDF
import os
from datetime import datetime
import re

def clean_text_ascii(text: str) -> str:
    # 去除 emoji、中文等非 ASCII 字符
    return re.sub(r'[^\x00-\x7F]+', '', text)

def generate_pdf(report_text: str, date_str: str = None) -> str:
    date_str = date_str or datetime.today().strftime("%Y-%m-%d")
    filename = f"report_{date_str}.pdf"
    output_dir = "report_output"
    filepath = os.path.join(output_dir, filename)

    os.makedirs(output_dir, exist_ok=True)

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    cleaned = clean_text_ascii(report_text)

    for line in cleaned.split("\n"):
        pdf.multi_cell(0, 10, line)

    pdf.output(filepath)
    return filepath
