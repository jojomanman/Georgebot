from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import ContextTypes, MessageHandler, filters
from db.database import log_location
from datetime import datetime

async def handle_location(update: Update, context: ContextTypes.DEFAULT_TYPE):
    location = update.message.location
    chat_id = update.effective_chat.id
    user_id = update.effective_user.id
    timestamp = update.message.date.isoformat()
    try:
        log_location(chat_id, user_id, location.latitude, location.longitude, timestamp)
        await update.message.reply_text(f"Location received: Latitude {location.latitude}, Longitude {location.longitude}")
    except Exception as e:
        await update.message.reply_text(f"Error logging location: {str(e)}")