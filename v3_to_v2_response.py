import json
import copy
import pdb

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

def v3_to_v2(v3_json):
    response = copy.deepcopy(v2_reponse)
    response["responseId"] = v3_json["responseId"]

    response["queryResult"]["queryText"] = v3_json["queryResult"]["text"]
    
    response["queryResult"]["parameters"] = v3_json["queryResult"]["parameters"]

    response["queryResult"]["fulfillmentText"] = v3_json["queryResult"]["responseMessages"][0]["text"]["text"]

    response["queryResult"]["fulfillmentMessages"] = v3_json["queryResult"]["responseMessages"]

    try:
        response["queryResult"]["intent"] =  v3_json["queryResult"]["intent"]
    except:
        pass
        # continue
        # pdb.set_trace()
    
    response["queryResult"]["languageCode"] = v3_json["queryResult"]["languageCode"]

    response["queryResult"]["intentDetectionConfidence"] = v3_json["queryResult"]["intentDetectionConfidence"]

    return response

if __name__ == "__main__":
    v3_json = json.load(open('data/v3.json'))
    print(v3_json)
    print(v3_to_v2(v3_json))
