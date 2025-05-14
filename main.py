import os, logging, random
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

load_dotenv()
logging.basicConfig(level=logging.INFO)
QUOTES = ["Stay hungry.", "Just keep swimming.", "Carpe diem."]

async def quote_handler(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    if update.message.web_app_data and update.message.web_app_data.data == "quote":
        await update.message.reply_text(random.choice(QUOTES))

app.add_handler(MessageHandler(filters.StatusUpdate.WEB_APP_DATA, quote_handler))


app = ApplicationBuilder().token(os.getenv("BOT_TOKEN")).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, any_text))

if __name__ == "__main__":
    app.run_polling()
