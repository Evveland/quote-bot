import os, random, logging
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import (
    ApplicationBuilder, MessageHandler, ContextTypes, filters
)

load_dotenv()
QUOTES = [
    "The best time to plant a tree was 20 years ago. The second best time is now.",
    "Do one thing every day that scares you. —Eleanor Roosevelt",
    "Action is the foundational key to all success. —Pablo Picasso",
]

async def handle_webapp(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Replies with a random quote when WebApp sends 'quote'."""
    if update.message.web_app_data and update.message.web_app_data.data == "quote":
        await update.message.reply_text(random.choice(QUOTES))

async def fallback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Send /start and press *Inspire Me* in the menu.", parse_mode="Markdown")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Tap *Inspire Me* at the bottom‑left 🚀", parse_mode="Markdown")

logging.basicConfig(level=logging.INFO)
app = ApplicationBuilder().token(os.getenv("BOT_TOKEN")).build()
app.add_handler(MessageHandler(filters.StatusUpdate.WEB_APP_DATA, handle_webapp))
app.add_handler(MessageHandler(filters.COMMAND, start))
app.add_handler(MessageHandler(filters.TEXT, fallback))

if __name__ == "__main__":
    app.run_polling()
