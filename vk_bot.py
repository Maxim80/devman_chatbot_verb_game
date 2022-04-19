from requests import session
from dialogflow_lib import detect_intent_text
from dotenv import load_dotenv
from vk_api.longpoll import VkLongPoll, VkEventType
import vk_api as vk
import random
import os


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
    vk_token = os.environ['VK_TOKEN'] or os.getenv('VK_TOKEN')
    dataflow_project_id = os.environ['DIALOGFLOW_PROJECT_ID'] or os.getenv('DIALOGFLOW_PROJECT_ID')
    vk_session = vk.VkApi(token=vk_token)
    vk_api = vk_session.get_api()
    longpoll = VkLongPoll(vk_session)
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            reply_to_user_message(event, vk_api, dataflow_project_id)


if __name__ == "__main__":
    main()
