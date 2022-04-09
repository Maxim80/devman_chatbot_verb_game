from google.cloud import dialogflow
import os


def detect_intent_text(session_id, text, language_code='ru'):
    """Returns the result of detect intent with texts as inputs.
    Using the same `session_id` between requests allows continuation
    of the conversation."""
    project_id = os.environ['DIALOGFLOW_PROJECT_ID'] or os.getenv('DIALOGFLOW_PROJECT_ID')
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(project_id, session_id)
    text_input = dialogflow.TextInput(text=text, language_code=language_code)
    query_input = dialogflow.QueryInput(text=text_input)
    response = session_client.detect_intent(
        request={"session": session, "query_input": query_input}
    )
    fulfillment = response.query_result.fulfillment_text
    return fulfillment
