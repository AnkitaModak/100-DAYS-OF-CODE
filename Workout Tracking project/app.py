from datetime import datetime
import requests
import config
APP_ID = config.api_id
API_KEY = config.api_key
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = config.sheet_endpoint
YOUR_USERNAME = config.auth_username
YOUR_PASSWORD = config.auth_password
weight = config.your_weight
height = config.your_height
age = config.your_age
exercise_headers = {
    "Content-Type": "application/json",
    "x-app-id" : APP_ID,
    "x-app-key" : API_KEY,
}
exercise_text = input("Tell me which exercises you did: ")
exercise_params = {
    "query" : exercise_text,
    "weight_kg" : config.weight,
    "height_cm" : config.height,
    "age" : config.age
}
response = requests.post(url= exercise_endpoint , json= exercise_params , headers= exercise_headers)
response.raise_for_status()
result = response.json()
today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")
for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    #sheet_response = requests.post(sheety_endpoint, json=sheet_inputs)
    auth_inputs =(YOUR_USERNAME,YOUR_PASSWORD)
    sheet_response = requests.post(url=sheety_endpoint,json=sheet_inputs,auth= auth_inputs)
