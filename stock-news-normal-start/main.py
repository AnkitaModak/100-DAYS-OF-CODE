import requests
from twilio.rest import Client
import config
from config import my_phone_num

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
STOCK_API_KEY= config.stock_api
NEWS_API_KEY = config.NEWS_API_KEY
account_sid = config.twilio_account_sid
auth_token = config.twilio_auth_token
twilio_phone_number = config.twilio_phone_num
my_phone_number = config.my_phone_num
stock_params = {
    "function" :"TIME_SERIES_DAILY",
    "symbol" : STOCK_NAME,
    "apikey" : STOCK_API_KEY,
}
response = requests.get(url = STOCK_ENDPOINT, params = stock_params)
response.raise_for_status()
data = response.json()["Time Series (Daily)"]
data_list = [value for (key,value) in data.items()]
yesterday_data = data_list[0]
yesterdays_closing_price = yesterday_data["4. close"]
print(yesterdays_closing_price)
day_before_yesterday_data = data_list[1]
day_before_yesterdays_closing_price = day_before_yesterday_data["4. close"]
print(day_before_yesterdays_closing_price)
difference = abs(float(yesterdays_closing_price) - float(day_before_yesterdays_closing_price))
print(difference)
diff_percent = (difference / float(yesterdays_closing_price)) * 100
print(diff_percent)
if diff_percent > 5:
    news_params = {
        "apikey" : NEWS_API_KEY,
        "qInTitle" : COMPANY_NAME,
    }
    news_response = requests.get(url = NEWS_ENDPOINT , params= news_params)
    articles = news_response.json()["articles"]
    three_articles = articles[:3]
    print(three_articles)


formatted_articles = [f"Headline: {article ["title"]}. \nBrief: {article["description"]}" for article in three_articles]

client = Client(account_sid, auth_token)


for article in formatted_articles:
    message = client.messages.create(
        body = article,
        to =    my_phone_number,
        from_= twilio_phone_number,
    )


