import unittest
from ..newsapi import fetch_latest_news
from unittest.mock import patch
import datetime


class TestNewsApi(unittest.TestCase):
    def test_emtpy_api_key_fails(self):
        with self.assertRaises(Exception) as context:
            fetch_latest_news("", ["keyword"], 10)
        self.assertTrue("API key not found!" in str(context.exception))

    def test_empty_keywords_fails(self):
        with self.assertRaises(Exception) as context:
            fetch_latest_news("apiKey", [], 10)
        self.assertTrue("News keywords not found!" in str(context.exception))

    def test_non_list_keywords_fails(self):
        with self.assertRaises(Exception) as context:
            fetch_latest_news("apiKey", "123", 10)
        self.assertTrue("News keywords should be a list!" in str(context.exception))

    def test_non_alpha_keywords_fails(self):
        with self.assertRaises(Exception) as context:
            fetch_latest_news("apiKey", ["123"], 10)
        self.assertTrue(
            "News keywords should only contain alphabetic characters!"
            in str(context.exception)
        )


class TestNewsApiMocked(unittest.TestCase):
    def setUp(self):
        self.mock_get_patcher = patch("requests.get")
        self.mock_get = self.mock_get_patcher.start()

    def tearDown(self):
        self.mock_get_patcher.stop()

    def test_mocked_news_api(self):
        keywords = ["keyword"]
        apiKey = "apiKey"
        lookback_days = 10

        self.mock_get.return_value.status_code = 200
        self.mock_get.return_value.json.return_value = {
            "articles": [
                {
                    "title": "title1",
                    "description": "description1",
                    "url": "url1",
                    "language": "en",
                    "date": "2020-01-01",
                },
                {
                    "title": "title2",
                    "description": "description2",
                    "url": "url2",
                    "language": "en",
                    "date": "2020-01-02",
                },
            ]
        }
        result = fetch_latest_news(apiKey, keywords, lookback_days)
        self.assertEqual(len(result), 2)
        self.mock_get.assert_called_once_with(
            "https://newsapi.org/v2/everything",
            params={
                "q": keywords,
                "from": (
                    datetime.datetime.now() - datetime.timedelta(days=lookback_days)
                ).strftime("%Y-%m-%d"),
                "sortBy": "publishedAt",
                "apiKey": apiKey,
            },
        )


if __name__ == "__main__":
    unittest.main()
