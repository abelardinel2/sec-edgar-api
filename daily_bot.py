
import os
from datetime import datetime
from sec_edgar_downloader import Downloader
from telegram import Bot

COMPANY_NAME = os.getenv("COMPANY_NAME")
SEC_EMAIL = os.getenv("SEC_EMAIL")
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

dl = Downloader(company_name=COMPANY_NAME, email_address=SEC_EMAIL)

# Download filings for AAPL as example
filings = dl.get("4", "AAPL")
print(f"Downloaded filings: {filings}")

# Send Telegram message
bot = Bot(token=TELEGRAM_BOT_TOKEN)
bot.send_message(
    chat_id=TELEGRAM_CHAT_ID,
    text=f"✅ Insider flow summary for {datetime.now().strftime('%Y-%m-%d')}\nFilings downloaded: {filings}"
)
