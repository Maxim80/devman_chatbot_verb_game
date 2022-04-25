from dialogflow_lib import create_intent
from dotenv import load_dotenv
import json
import os

def main() -> None:
    load_dotenv()
    project_id = os.getenv('DIALOGFLOW_PROJECT_ID')

    with open('questions.json', 'r') as f:
        training_questions = json.load(f)

    for intent, questions in training_questions.items():
        training_phrases_parts = questions['questions']
        message_text = questions['answer']
        create_intent(project_id, intent, training_phrases_parts, [message_text])


if __name__ == '__main__':
    main()
