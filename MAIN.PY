import requests
from datetime import datetime

USERNAME = "angela"
TOKEN = "hjkh34h3jk44h3jh4"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreetermsofservice":"yes",
    "notminor": "yes",
}

#response = requests.post(url=pixela_endpoint, json=user_params)
#print(response.text)
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "km",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

#response = requests.post(url=graph_endpoint, params=graph_config,headers=Headers)
#print(response.text)

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()
#print(today)

pixel_data = {
    "data": today.strftime("%y%m%d"),
    "quantity": input("how many kilometers did you cycle today"),
}

response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(response.text)

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%y%m%d')}"

new_pixel_data = {
    "quantity": "4.5"
}

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%y%m%d')}"
response = requests.delete(url=delete_endpoint, headers=headers)
print(response.text)
