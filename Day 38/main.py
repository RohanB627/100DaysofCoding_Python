import requests
import os
from datetime import datetime


# os.environ["APP_ID"] = "787220d2"
# os.environ["API_KEY"]= "bc72af9a5ecc1b906661d2dd0a69691d"
# os.environ["SHEETY_USERNAME"] = "ade22c44fe541633fdf41ed511e7ee30"
# os.environ["PROJECT_NAME"] = "workoutTracking"
# os.environ["SHEET_NAME"] = "workouts"


# os.environ["nutri_endpoint"] = "https://trackapi.nutritionix.com/v2/natural/exercise"
# os.environ["sheety_endpoint"] = ("https://api.sheety.co/")

headers = {
    "x-app-id": os.environ.get("APP_ID"),
    "x-app-key": os.environ.get("API_KEY")
}

parameters = {
    "query": input("Tell me what exercise you did and the duration: "),
}

headers_auth = {
    "Authorization": "Basic Um9uNjoxMjM0NTY="
}

items = []
response = requests.post(url=os.environ.get("NUTRI_ENDPOINT"), json=parameters,headers=headers)

data = response.json()["exercises"][0]
date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")
print(data)

body = {
    "workout": {
        "date": date,
        "time": now_time,
        "exercise": data['user_input'].title(),
        "duration": data['duration_min'],
        "calories": data['nf_calories'],
    }
}

response_to_excel = requests.post(url=f"{os.environ.get('SHEETY_ENDPOINT')}/{os.environ.get('SHEETY_USERNAME')}/{os.environ.get('PROJECT_NAME')}/{os.environ.get('SHEET_NAME')}", json=body, headers= headers_auth)
print(response_to_excel.text)

