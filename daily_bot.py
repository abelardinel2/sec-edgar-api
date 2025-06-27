import os
from telegram import Bot

company = os.getenv("COMPANY_NAME")
email = os.getenv("SEC_EMAIL")
bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
chat_id = os.getenv("TELEGRAM_CHAT_ID")

bot = Bot(token=bot_token)

message = f"✅ *Daily Bot Report*\nCompany: {company}\nEmail: {email}"
bot.send_message(chat_id=chat_id, text=message, parse_mode='Markdown')
print("Message sent!")