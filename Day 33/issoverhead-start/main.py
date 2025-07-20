import requests
import datetime as dt
import smtplib
import schedule
import time

MY_LAT = 50.064651 # Your latitude
MY_LONG = 19.944981 # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

print(iss_latitude, iss_longitude)


def look_up():
    if 45 <= iss_latitude <= 55 and 14 <= iss_longitude <= 24:
        if hour_now >= sunset or hour_now <= sunrise:
            my_email = "mangeykyo@gmail.com"
            password = "gkwj bvke jwuy tpdi"

            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=my_email, password=password)
                connection.sendmail(
                    from_addr=my_email,
                    to_addrs="rohan_313@hotmail.com",
                    msg=f"Subject: You can see the ISS Overhead now."
                )
        print("done")
    else:
        print("Not yet")




#Your position is within +5 or -5 degrees of the ISS position.


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

date_time_now = dt.datetime.now()
time_now = date_time_now.time()
hour_now = time_now.hour
print(hour_now)
print(sunset)

schedule.every(60).seconds.do(look_up)

while True:
    schedule.run_pending()
    time.sleep(1)
#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



