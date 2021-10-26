import json
import copy

v3_json = json.load(open('data/v3.json'))
print(v3_json)

v2_reponse = {
  "responseId": "36d68aed-9e55-4a04-93e2-615d80742518-cad07fe1",
  "queryResult": {
    "queryText": "Hello",
    "action": "input.welcome",
    "parameters": {},
    "allRequiredParamsPresent": True,
    "fulfillmentText": "Good day! What can I do for you today?",
    "fulfillmentMessages": [{
      "text": {
        "text": ["Good day! What can I do for you today?"]
      }
    }],
    "intent": {
      "name": "projects/optimum-pier-326005/agent/intents/7c8ff205-06f6-4ce2-96f7-b07225e7957d",
      "displayName": "Default Welcome Intent"
    },
    "intentDetectionConfidence": 1.0,
    "languageCode": "en"
  }
}

def v3_to_v2(data):
    response = copy.deepcopy(v2_reponse)
    response["queryResult"]["queryText"] = v3_json["text"]
    
    response["queryResult"]["parameters"] = v3_json["parameters"]

    response["queryResult"]["fulfillmentText"] = v3_json["responseMessages"][0]["text"]["text"]

    response["queryResult"]["fulfillmentMessages"] = v3_json["responseMessages"]

    response["queryResult"]["intent"] =  v3_json["intent"]
    
    response["queryResult"]["languageCode"] = v3_json["languageCode"]

    response["queryResult"]["intentDetectionConfidence"] = v3_json["intentDetectionConfidence"]

    return response

print(v3_to_v2(v3_json))