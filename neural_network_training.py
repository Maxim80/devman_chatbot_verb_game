from dialogflow_lib import create_intent
from dotenv import load_dotenv
import json
import os

def main() -> None:
    load_dotenv()
    project_id = os.environ['DIALOGFLOW_PROJECT_ID'] or os.getenv('DIALOGFLOW_PROJECT_ID')

    intents = ['Устройство на работу']

    with open('questions.json', 'r') as f:
        training_questions = json.load(f)

    for intent in intents:
        training_phrases_parts = training_questions[intent]['questions']
        message_text = training_questions[intent]['answer']
        create_intent(project_id, intent, training_phrases_parts, [message_text])


if __name__ == '__main__':
    main()
