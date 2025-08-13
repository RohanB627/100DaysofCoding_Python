from calendar import weekday

import requests
import datetime as date
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "interval": "60min",
    "outputsize": "compact",
    "apikey": "TECLCJRSF49MMKZQ"
}

account_sid = "AC0975011a55cd11fd59633c616a43bc74"
auth_token = "afc8b9c397640304a908ae40471de684"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

url = 'https://www.alphavantage.co/query?'
r = requests.get(url, params= stock_parameters)
data = r.json()["Time Series (Daily)"]
print(data)

data_list = [value for (key,value) in data.items()]
yesterday = data_list[1]["4. close"]
day_before_yesterday = data_list[2]["1. open"]
print(yesterday, day_before_yesterday)

parameters = {
    "q": COMPANY_NAME,
    "from": yesterday,
    "to": day_before_yesterday,
    "apiKey": "0c1f5b28e8db4d88b3ad22ffd3706a17",
}


percentage = float((float(yesterday) - float(day_before_yesterday)) / float(day_before_yesterday) * 100)

client = Client(account_sid, auth_token)
if percentage >= 1:
    news_url = "https://newsapi.org/v2/everything?"
    news_r = requests.get(news_url, params= parameters)
    news_data = news_r.json()
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_="whatsapp:+14155238886",
        body=f"{STOCK}: {round(percentage, 2)}🔺 \nHeadline: {news_data['articles'][0]['title']}\n\nBrief: {news_data['articles'][0]['description']}\n{news_data['articles'][0]['url']}\n\nHeadline: {news_data['articles'][1]['title']}\n\nBrief: {news_data['articles'][1]['description']}\n{news_data['articles'][1]['url']}\n\nHeadline: {news_data['articles'][2]['title']}\n\nBrief: {news_data['articles'][2]['description']}\n{news_data['articles'][2]['url']}",
        to="whatsapp:+48662879440",
    )
    print(message.status)

else:
    news_api_key = "0c1f5b28e8db4d88b3ad22ffd3706a17"
    news_url = f"https://newsapi.org/v2/everything?q={COMPANY_NAME}&from=2025-08-05&to=2025-08-05&sortBy=popularity&apiKey=0c1f5b28e8db4d88b3ad22ffd3706a17"
    news_r = requests.get(news_url)
    news_data = news_r.json()
    message = client.messages.create(
        from_="whatsapp:+14155238886",
        body=f"{STOCK}: {round(percentage, 2)}🔻 \nHeadline:{news_data['articles'][0]['title']}\n\nBrief: {news_data['articles'][0]['description']}\n{news_data['articles'][0]['url']}\n\nHeadline: {news_data['articles'][1]['title']}\n\nBrief: {news_data['articles'][1]['description']}\n{news_data['articles'][1]['url']}\n\nHeadline: {news_data['articles'][2]['title']}\n\nBrief: {news_data['articles'][2]['description']}\n{news_data['articles'][2]['url']}",
        to="whatsapp:+48662879440",
    )
    print(message.status)



#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

