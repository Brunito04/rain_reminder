import requests
import json
import os
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "69f04e4613056b159c2761a9d9e664d2"
account_sid = "AC6a8da8ea9b4ab655976521c069af9171"
auth_token = "39f0b96936f9fa4cb9382a6b2e925106"

My_LAT = -34.603683
MY_LNG = -58.381557

parameters = {
    "lat": My_LAT,
    "lon": MY_LNG,
    "appid": api_key,
    "exclude": "current,minute,daily"
}

response = requests.get(OWM_Endpoint, params=parameters)
response.raise_for_status()

# To see json file in console
weather_data = response.json()

weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an umbrella.",
        from_="+19256607171",
        to="+541131145270"
    )
    print(message.status)

#print(weather_data["hourly"][0]["weather"][0]["id"])

