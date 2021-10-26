from google.cloud.dialogflowcx_v3beta1.services.agents import AgentsClient

project_id = "gde21-329909"

location_id = "asia-northeast1"

agent_id = "1191c7bd-2189-4261-b6c6-c2c29572eba4"

agent = f"projects/{project_id}/locations/{location_id}/agents/{agent_id}"

language_code = "vi"

client_options = None
agent_components = AgentsClient.parse_agent_path(agent)
location_id = agent_components["location"]

api_endpoint = f"{location_id}-dialogflow.googleapis.com:443"
print(f"API Endpoint: {api_endpoint}\n")
client_options = {"api_endpoint": api_endpoint}