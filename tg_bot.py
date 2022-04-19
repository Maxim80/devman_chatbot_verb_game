from telegram import Update
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext
from dialogflow_lib import detect_intent_text
from dotenv import load_dotenv
import os


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

    # Create the Updater and pass it your bot's token.
    updater = Updater(telegram_token)

    # Get the dispatcher to register handlers.
    dispatcher = updater.dispatcher

    # In response to the user's text message will return the intent from dialogflow.
    dispatcher.add_handler(MessageHandler(Filters.text, reply_to_user_message))

    # Start the bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
