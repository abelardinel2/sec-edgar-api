
import os
from datetime import datetime
import telegram

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

bot = telegram.Bot(token=TELEGRAM_BOT_TOKEN)

# Example summary generation
today = datetime.today().strftime("%Y-%m-%d")
summary = f"📊 *Insider Flow Summary – {today}*"

bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=summary, parse_mode="Markdown")
