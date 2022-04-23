from telegram import Update
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext
from dialogflow_lib import detect_intent_text
from dotenv import load_dotenv
from logging_handlers import TelegramLogsHandler
import logging
import os


logger = logging.getLogger(__file__)


def reply_to_user_message(update: Update, context: CallbackContext) -> None:
    """Answer to user text message."""

    project_id = os.environ['DIALOGFLOW_PROJECT_ID'] or os.getenv('DIALOGFLOW_PROJECT_ID')
    user_message_text = update.message.text
    session_id = update.message.chat_id
    intent_text, _ = detect_intent_text(project_id, session_id, user_message_text)
    update.message.reply_text(intent_text)


def main() -> None:
    """Start the bot."""

    load_dotenv()
    telegram_token = os.environ['TELERGAM_TOKEN'] or os.getenv('TELERGAM_TOKEN')
    admin_chat_token = os.environ['ADMIN_CHAT_ID'] or os.getenv('ADMIN_CHAT_ID')

    logging.basicConfig(level=logging.DEBUG)
    logger.addHandler(TelegramLogsHandler(telegram_token, admin_chat_token))

    try:
        updater = Updater(telegram_token)
        dispatcher = updater.dispatcher
        dispatcher.add_handler(MessageHandler(Filters.text, reply_to_user_message))
        updater.start_polling()
        updater.idle()
    except Exception as err:
        logger.exception(err)


if __name__ == '__main__':
    main()
