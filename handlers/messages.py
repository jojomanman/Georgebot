from telegram import Update
from telegram.ext import ContextTypes
from db.database import log_message, log_response
from datetime import datetime
import logging

logger = logging.getLogger(__name__)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        chat_id = update.effective_chat.id
        user_id = update.effective_user.id
        text = update.message.text
        timestamp = update.message.date.isoformat()  # Telegram's UTC timestamp
        log_message(chat_id, user_id, text, timestamp)
        await update.message.reply_text(f"Echo: {text} (Timestamp: {timestamp})")  # Basic echo for testing
        response_timestamp = datetime.utcnow().isoformat()
        try:
            log_response(chat_id, user_id, f"Echo: {text} (Timestamp: {timestamp})", response_timestamp)
        except Exception as log_e:
            logger.error(f"Error logging response: {log_e}")
    except Exception as e:
        logger.error(f"Error handling message: {e}")
        await update.message.reply_text("Sorry, an error occurred.")