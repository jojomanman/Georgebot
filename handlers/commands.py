from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import ContextTypes
import logging
from datetime import datetime
from db.database import log_message, log_response
import subprocess
import os

logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        await update.message.reply_text("Bot started! Send a message.")
        response_timestamp = datetime.utcnow().isoformat()
        try:
            log_response(update.effective_chat.id, update.effective_user.id, "Bot started! Send a message.", response_timestamp)
        except Exception as log_e:
            logger.error(f"Error logging response in start: {log_e}")
    except Exception as e:
        logger.error(f"Error in start command: {e}")

async def run_script(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Usage: /run_script <script_name.py>")
        return
    script_name = context.args[0]
    script_path = os.path.join('scripts', script_name)
    if not os.path.exists(script_path) or not script_path.endswith('.py'):
        await update.message.reply_text("Invalid or unauthorized script.")
        return
    try:
        chat_id = update.effective_chat.id
        user_id = update.effective_user.id
        timestamp = datetime.utcnow().isoformat()
        log_message(chat_id, user_id, f"/run_script {script_name}", timestamp)  # Log command
        result = subprocess.run(['python', script_path], capture_output=True, text=True, timeout=30)
        output = result.stdout + result.stderr
        response_text = f"Script output:\n{output}" if output else "Script executed successfully."
        await update.message.reply_text(response_text)
        log_response(chat_id, user_id, response_text, datetime.utcnow().isoformat())
    except Exception as e:
        error_msg = f"Error: {str(e)}"
        await update.message.reply_text(error_msg)
        log_response(chat_id, user_id, error_msg, datetime.utcnow().isoformat())
        logger.error(f"Error in run_script: {e}")

async def share_location(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[KeyboardButton("Share Location", request_location=True)]]
    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True, resize_keyboard=True)
    await update.message.reply_text("Please share your location:", reply_markup=reply_markup)