from requests import session
from dialogflow_lib import detect_intent_text
from dotenv import load_dotenv
from vk_api.longpoll import VkLongPoll, VkEventType
from logging_handlers import TelegramLogsHandler
import vk_api as vk
import logging
import random
import os


logger = logging.getLogger(__file__)


def reply_to_user_message(event, vk_api, dataflow_project_id):
    user_message_text = event.text
    session_id = event.user_id
    intent_text, is_fallback = detect_intent_text(dataflow_project_id, session_id, user_message_text)
    if not is_fallback:
        vk_api.messages.send(
            user_id=event.user_id,
            message=intent_text,
            random_id=random.randint(1,1000)
        )


def main():
    load_dotenv()
    vk_token = os.getenv('VK_TOKEN')
    telegram_token = os.getenv('TELERGAM_TOKEN')
    admin_chat_token = os.getenv('ADMIN_CHAT_ID')
    dataflow_project_id = os.getenv('DIALOGFLOW_PROJECT_ID')

    logging.basicConfig(level=logging.DEBUG)
    logger.addHandler(TelegramLogsHandler(telegram_token, admin_chat_token))

    try:
        vk_session = vk.VkApi(token=vk_token)
        vk_api = vk_session.get_api()
        longpoll = VkLongPoll(vk_session)
        for event in longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                reply_to_user_message(event, vk_api, dataflow_project_id)
    except Exception as err:
        logger.exception(err)


if __name__ == "__main__":
    main()
