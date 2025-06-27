import os
from sec_edgar_downloader import Downloader
from telegram import Bot
from datetime import datetime

COMPANY_NAME = os.getenv("COMPANY_NAME")
SEC_EMAIL = os.getenv("SEC_EMAIL")
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def main():
    print(f"Running for {COMPANY_NAME} / {SEC_EMAIL}")
    dl = Downloader(company_name=COMPANY_NAME, email_address=SEC_EMAIL)
    filings = dl.get("4", "AAPL")
    print(f"Downloaded filings: {len(filings)}")

    bot = Bot(token=TELEGRAM_BOT_TOKEN)
    try:
        bot.send_message(
            chat_id=TELEGRAM_CHAT_ID,
            text=f"✅ Insider flow summary for {datetime.now().strftime('%Y-%m-%d')}.\nFilings downloaded: {len(filings)}"
        )
        print("Telegram message sent ✅")
    except Exception as e:
        print(f"Telegram failed: {e}")

if __name__ == "__main__":
    main()