import requests
from datetime import datetime
TOKEN = "sas54e5dfg7698ygj"
USERNAME = "anjali12"
pixel_endpoint = "https://pixe.la/v1/users"
GRAPH_ID = "anjaligraph23"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",

}

response = requests.post(url=pixel_endpoint, json=user_params)
print(response.text)
graph_endpoint = f"{pixel_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Coding Graph",
    "unit": "hours",
    "type": "float",
    "color": "ajisai",

}

header = {
    "X-USER-TOKEN": TOKEN
}
# response = requests.post(url=graph_endpoint, json=graph_config, headers=header)
# print(response.text)

today = datetime.now()

pixel_creation = f"{pixel_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

pixel_data = {
    "date" : today.strftime("%Y%m%d"),
    "quantity" : input("How many hours did you dedicated in coding?"),

}
# a = requests.post(url=pixel_creation, json=pixel_data,headers=header)
# print (a.text)

update_endpoint = f"{pixel_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

new_pixel_data = {
    "quantity": "4"
}
# b = requests.put(url=update_endpoint, json=new_pixel_data, headers=header)
# print(b.text)

delete_endpoint = f"{pixel_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

# c = requests.delete(url=delete_endpoint, headers=header)
# print(c.text)

