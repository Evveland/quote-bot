import os, logging, random
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

load_dotenv()
logging.basicConfig(level=logging.INFO)
QUOTES = ["Stay hungry.", "Just keep swimming.", "Carpe diem."]

async def any_text(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Echo: " + update.message.text)

app = ApplicationBuilder().token(os.getenv("BOT_TOKEN")).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, any_text))

if __name__ == "__main__":
    app.run_polling()
