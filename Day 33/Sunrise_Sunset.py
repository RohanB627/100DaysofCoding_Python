import requests
import datetime as dt


MY_LAT = 50.064651
MY_LONG = 19.944981

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}


response = requests.get(url = "https://api.sunrise-sunset.org/json", params= parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split('T')[1].split("+")[0])
sunset = int(data["results"]["sunset"].split('T')[1].split("+")[0])

time_now = dt.datetime.now().time()

print(time_now)
