import requests
from datetime import datetime
import config
pixela_endpoint ="https://pixe.la/v1/users"
USERNAME = config.YOUR_USERNAME
TOKEN = config.YOUR_TOKEN
GRAPHID = config.YOUR_GRAPHID
TODAY = datetime.now().strftime("%Y%m%d")
YESTERDAY = datetime(year=2025 , month= 5 , day= 23).strftime("%Y%m%d")
Delete_day = datetime(year=2025 , month= 5 , day= 22).strftime("%Y%m%d")
user_params = {
    "token" : TOKEN,
    "username" : USERNAME,
    "agreeTermsOfService" : "yes" ,
    "notMinor" : "yes",
}
#to create user
# response =requests.post(url = pixela_endpoint , json= user_params)
# print(response.text)
graph_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs"

graph_params = {
    "id": GRAPHID,
    "name": "Coding graph",
    "unit": "minute" ,
    "type": "int",
    "color": "sora",
}
headers = {
    "X-USER-TOKEN" : TOKEN
}
# to Create a graph definition
# response = requests.post(url = graph_endpoint ,json=graph_params, headers= headers )
# print(response.text)
pixelhabit_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPHID}"
pixelhabit_params = {
    "date" : TODAY,
    "quantity" : input("how many minutes did you code today?"),
}
#Post value to the graph
response = requests.post(url = pixelhabit_endpoint , json= pixelhabit_params , headers= headers)
print(response.text)
pixelupdate_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPHID}/{YESTERDAY}"
update_params ={
    "quantity" : "98",
}
#update a pixel
# response = requests.put(url=pixelupdate_endpoint , json=update_params,headers=headers)
# print(response.text)
delete_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPHID}/{Delete_day}"

#delete a pixel
# response = requests.delete(url = delete_endpoint , headers= headers)
# print(response.text)