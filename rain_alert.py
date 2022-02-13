import requests
from twilio.rest import Client

account_sid = "ACf3be8e59b84f09db3f3ecedc27c276b8"
auth_token = "8786a9a35f37c1ad63812a20b74da388"


parameters = {
    "lat": 3.595196,
    "lon": -98.672226,
    "exclude": "current,minutely,daily",
    "appid": "7dae409ebd817f4aa771a9c8753473c9",
    "lang": "id"
}


res = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=parameters)
res.raise_for_status()
data = res.json()
"""data_slice berfungsi untuk mengambil list data dari 0 - 11"""
data_slice = data["hourly"][:12]

will_rain = False

for hour_data in data_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="Hai, sepertinya hari ini akan hujan, sediakan payung yaaa ☔",
        from_="+12817617124",
        to="+6282284081638"
    )
    print(message.status)

