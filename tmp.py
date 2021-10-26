import sys, os
from flask import Flask, request, make_response, jsonify
from flask_cors import CORS, cross_origin

import dialogflow
from google.api_core.exceptions import InvalidArgument
from google.protobuf.json_format import MessageToDict

DIALOGFLOW_PROJECT_ID = os.environ['GOOGLE_CLOUD_PROJECT'] # Ensure GCP Project ID is set
client = dialogflow.AgentsClient()
parent = client.project_path(DIALOGFLOW_PROJECT_ID)
details = client.get_agent(parent)
print(MessageToDict(details))

text_data = "Helqwelo"

session_id = "alsdlasdoqwlelasd"
language_code = "en"

session_client = dialogflow.SessionsClient()
session = session_client.session_path(
    DIALOGFLOW_PROJECT_ID, session_id)
text_input = dialogflow.types.TextInput(
    text=text_data, language_code=language_code)
query_input = dialogflow.types.QueryInput(text=text_input)
   
response = session_client.detect_intent(
	session=session, query_input=query_input)

print(MessageToDict(response))


