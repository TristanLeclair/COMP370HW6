import datetime
from typing import List
import requests


def fetch_latest_news(
    api_key: str, news_keywords: List[str], lookback_days=10, quiet=False
):
    if not api_key:
        raise Exception("API key not found!")
    if not news_keywords:
        raise Exception("News keywords not found!")
    if not isinstance(news_keywords, list):
        raise Exception("News keywords should be a list!")
    # check that each string in news keywords does not contain non-alphabetic characters
    for keyword in news_keywords:
        if not keyword.isalpha():
            raise Exception("News keywords should only contain alphabetic characters!")
    if not lookback_days:
        raise Exception("Lookback days not found!")

    # query newsapi.org
    url = "https://newsapi.org/v2/everything"
    date = (datetime.datetime.now() - datetime.timedelta(days=lookback_days)).strftime(
        "%Y-%m-%d"
    )
    params = {
        "q": news_keywords,
        "from": date,
        "sortBy": "publishedAt",
        "apiKey": api_key,
        "language": "en",
    }

    if not quiet:
        print(f"Fetching news for {news_keywords}... with dates {date} days back")

    response = requests.get(url, params=params)

    # verify response status code
    if response.status_code != 200:
        if response.status_code == 401:
            raise Exception("Invalid API key!")
        elif response.status_code == 429:
            raise Exception("API rate limit exceeded!")
        raise Exception("Error fetching news!")

    # verify response content
    if not response.json()["status"] == "ok":
        raise Exception("Error fetching news!")

    articles = response.json()["articles"]

    clean_articles = clean_data(articles, lookback_days)

    return clean_articles


def clean_data(data, lookback_days):
    # check that data is no more farther than lookback_days
    date = (datetime.datetime.now() - datetime.timedelta(days=lookback_days)).strftime(
        "%Y-%m-%d"
    )
    for article in data:
        if article["publishedAt"] < date:
            # remove article
            data.remove(article)

    return data
