import sys, os
from flask import Flask, request, make_response, jsonify
from flask_cors import CORS, cross_origin

import dialogflow
from google.api_core.exceptions import InvalidArgument
from google.protobuf.json_format import MessageToDict

from google.cloud.dialogflowcx_v3beta1.services.agents import AgentsClient
from google.cloud.dialogflowcx_v3beta1.services.sessions import SessionsClient
from google.cloud.dialogflowcx_v3beta1.types import session

from config import * 

DIALOGFLOW_PROJECT_ID = os.environ['GOOGLE_CLOUD_PROJECT'] # Ensure GCP Project ID is set
# os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "/home/user/Downloads/service_account_keys.json" #If local machine

language_code = "vi"

DOMAINS_ALLOWED = "*" # You can restrict only for your sites here
app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": DOMAINS_ALLOWED}})

@app.route('/')
def index():
    return 'The server is running... Yaayy!!!'

@app.route('/get_dialogflow_agent', methods=['GET'])
def get_dialogflow_account_details():
    client = dialogflow.AgentsClient()
    parent = client.project_path(DIALOGFLOW_PROJECT_ID)
    details = client.get_agent(parent)
    return make_response(jsonify(MessageToDict(details)))

@app.route('/detect_intent', methods=['POST'])
def get_response_for_query():
    input_ = request.get_json(force=True)
    text_data = input_["queryInput"]["text"]["text"]
    
    session_id = input_["session"]
    session_path = f"{agent}/sessions/{session_id}"

    session_client = SessionsClient(client_options=client_options)

    # session_client = dialogflow.SessionsClient()
    # session = session_client.session_path(
    #     DIALOGFLOW_PROJECT_ID, session_id)
    # text_input = dialogflow.types.TextInput(
    #     text=text_data, language_code=language_code)
    # query_input = dialogflow.types.QueryInput(text=text_input)
    text_input = session.TextInput(text=text_data)
    query_input = session.QueryInput(text=text_input, language_code=language_code)
    request = session.DetectIntentRequest(
        session=session_path, query_input=query_input
    )
    try:
        response = session_client.detect_intent(request=request)
    except InvalidArgument:
        raise

    return make_response(jsonify(MessageToDict(response)))

if __name__ == '__main__':
    # Run Flask server
    app.run(host="0.0.0.0", port=6006, debug=True)
