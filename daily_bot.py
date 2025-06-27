import os
from telegram_bot import send_telegram_message

def main():
    # Example logic
    filings_downloaded = 1295
    print(f"Downloaded filings: {filings_downloaded}")
    send_telegram_message(f"✅ Download complete! Filings downloaded: {filings_downloaded}")

if __name__ == "__main__":
    main()
