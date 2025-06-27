
import os
from sec_edgar_downloader import Downloader
from telegram_bot import send_telegram_message
from datetime import datetime

company_name = os.getenv("COMPANY_NAME")
email = os.getenv("SEC_EMAIL")

dl = Downloader(company_name, email)

# Example tickers
tickers = ["AAPL", "META", "TSLA", "MSFT"]

summaries = []
total_filings = 0

for ticker in tickers:
    filings = dl.get("4", ticker)
    summaries.append(f"• {ticker}: {len(filings)} Form 4s")
    total_filings += len(filings)

# Simple bias logic (placeholder)
bias = "👀 Neutral"
if total_filings > 20:
    bias = "💣 Heavy Insider Activity"

today = datetime.now().strftime("%Y-%m-%d")

message = (
    f"📊 *Insider Flow Summary – {today}*

"
    + "\n".join(summaries) + "\n\n"
    f"🧮 *Total Form 4s:* {total_filings}\n"
    f"{bias}"
)

send_telegram_message(message, parse_mode="Markdown")
