import logging
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from config import BOT_TOKEN
from handlers.commands import start, run_script, share_location
from handlers.messages import handle_message
from handlers.location import handle_location

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Application.builder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("run_script", run_script))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

app.add_handler(CommandHandler("share_location", share_location))
app.add_handler(MessageHandler(filters.LOCATION, handle_location))

if __name__ == '__main__':
    logger.info("Starting bot...")
    app.run_polling(allowed_updates=['message', 'callback_query'])