import datetime
from datetime import timedelta
from typing import List
import requests


def fetch_latest_news(api_key: str, news_keywords: List[str], lookback_days=10):
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
    params = {
        "q": news_keywords,
        # this line is incorrect
        "from": (datetime.datetime.now() - datetime.timedelta(days=lookback_days)).strftime("%Y-%m-%d"),
        # "from": (datetime.now() - timedelta(days=lookback_days)).strftime("%Y-%m-%d"),
        "sortBy": "publishedAt",
        "apiKey": api_key,
    }
    response = requests.get(url, params=params)

    # verify response status code
    if response.status_code != 200:
        if response.status_code == 401:
            raise Exception("Invalid API key!")
        elif response.status_code == 429:
            raise Exception("API rate limit exceeded!")
        raise Exception("Error fetching news!")

    # return only english articles
    return [
        article
        for article in response.json()["articles"]
        if article["language"] == "en"
    ]
