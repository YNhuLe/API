import requests
import smtplib

MY_EMAIL = "y1011996@gmail.com"
PASSWORD = "mrnyhpmwbekkwtpu"

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = "XPVMJQG949OF4ZSQ"
NEWS_API_KEY = "2a488ac1caf8409187780791a0453953"

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY
}
response = requests.get(STOCK_ENDPOINT, stock_params)
print(response.json())

data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]

# get yesterday's closing stock price
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
print(yesterday_closing_price)

# Get the day before yesterday's closing stock price
day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
print(day_before_yesterday_closing_price)

# Find the positive difference between 1 and 2
difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
print(abs(difference))

# percentage difference in price between closing price yesterday and closing price the day before
diff_percentage = (difference / float(yesterday_closing_price)) * 100
print(diff_percentage)

# if percentage is greater than 5, then Get news from the news api
if diff_percentage > 1:
    print("BIGGG NEWSSS")
    news_params = {
        "apiKey": NEWS_API_KEY,
        "q": COMPANY_NAME
    }
else:
    news_params = {
        "apiKey": NEWS_API_KEY,
        "q": COMPANY_NAME
    }

news_response = requests.get(NEWS_ENDPOINT, params=news_params)
print(news_response.json())
articles = news_response.json()["articles"]

# use the slice operator in python to create a list of first 3 articles
three_articles = articles[:3]
print(three_articles)

formatted_articles = [f"Headline: {article['title']}. \n Brief: {article['description']}" for article in three_articles]

for article in formatted_articles:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="lenhuy10011996@gmail.com",
            msg=f"Subject: Stock news.\n\n This is the message:{article}"
        )
