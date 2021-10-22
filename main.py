import requests
import os
import twilio.rest

OWM_Endpoint = 'https://api.openweathermap.org/data/2.5/onecall'
api_key = '61bf5cd9baba6edb8c61e47d25b8b970'

account_sid = 'AC6cdb74ca9a930b2fa5cc25eecc340b4a'
auth_token = '47cc90d361deb988c397ba52775bef16'

parameters = {
    'lat': 47.658779,
    'lon': -117.426048,
    'appid': api_key,
    'exclude': 'current,minutely,daily'
}

response = requests.get(url=OWM_Endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()
twelve_hours = weather_data['hourly'][:12]

will_rain = False

for data in twelve_hours:
    weather_code = data['weather'][0]['id']
    if int(weather_code) < 700:
        will_rain = True
              
if will_rain:
    client = twilio.rest.Client(account_sid, auth_token)
    message = client.messages \
        .create(
            body="It's going to rain today. Remember to bring an ☂️",
            from_='+12183221257',
            to='+12816308839'
        )
    print(message.status)
