import os
from sec_edgar_downloader import Downloader
import requests

company_name = os.getenv("COMPANY_NAME")
email = os.getenv("SEC_EMAIL")
telegram_token = os.getenv("TELEGRAM_BOT_TOKEN")
chat_id = os.getenv("TELEGRAM_CHAT_ID")

dl = Downloader(company_name, email)

def main():
    cik = dl.lookup_cik("AAPL")
    filings = dl.get("4", cik)
    msg = f"AAPL insider trades: {len(filings)} Form 4s found."
    print(msg)

    url = f"https://api.telegram.org/bot{telegram_token}/sendMessage"
    payload = {"chat_id": chat_id, "text": msg}
    response = requests.post(url, json=payload)
    print("Telegram response:", response.text)

if __name__ == "__main__":
    main()