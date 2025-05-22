from twilio.rest import Client
import requests
import config
my_long = 82.549850
my_lat = 19.230400
api_key = config.OWM_api_key
account_sid = config.twilio_account_sid
auth_token = config.twilio_auth_token
twilio_phone_number = config.twilio_phone_num
my_phone_number = config.my_phone_num
parameters = {
        "lat": my_lat,
        "lon": my_long,
        "appid" : api_key,
        "cnt" : 4,
    }
response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
weather_data = response.json()
#id = weather_data["list"][0]["weather"][0]["id"]
will_rain = False
for hour_data in weather_data["list"]:
    id = hour_data["weather"][0]["id"]
    if id < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="Hey! Today it's going to rain! so don't forget to bring an umbrella!☔ ",
        from_=twilio_phone_number,
        to=my_phone_number
    )
    print(message.status)