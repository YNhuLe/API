# 🚀 Tesla Stock and News Notifier 📰 😎

#### Welcome to the Tesla stock and News Notifier! This little project is all about tracking Tesla's stock prices 
#### and getting the latest news delivered straight to your inbox. Because who does not want to stay updated with the latest
#### Elon Musk adventures? 🤓

### What Does It Do? 🤔

1. Tracks Tesla stock's price
2. Fetches the Latest Tesla News 📰
3. Send Email Alerts 📨

## How It Works? 
1. Stock Prices: We check Tesla's stock prices using the Alpha Vantage API
2. News: If there's a significant price change, we fetch the latest news from the News API.
3. Email Alert: We send you a neat email with the top 3 news articles if something big happens.

## Setup 🛠️
### Prerequisites
* Python 3.8+ 🐍
* requests library: Install it using pip install requests
* smtplib: Comes with Python's standard library
* Environment variables for your API keys

### Environment Variables 🌐
Make sure you set the following environment variables:

* OPEN_STOCK_API_KEY: Your Alpha Vantage API key
* OPEN_NEWS_API_KEY: Your News API key
* MY_EMAIL: Your Gmail address
* PASSWORD: Your Gmail password (consider using app-specific passwords for better security)

## Run the Script ▶️
Run the script to check Tesla's stock prices, fetch the latest news, and receive email alerts:

`python script.py`
