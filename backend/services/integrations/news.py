from newsapi import NewsApiClient

from django.conf import settings

from services.exceptions.news import NewsException


def get_news(title: str) -> dict:
    if not title:
        return {}

    newsapi = NewsApiClient(settings.NEWS_API_KEY)
    news_params = {'q': title, 'page_size': 20, 'page': 1, 'sort_by': 'publishedAt'}
    news = newsapi.get_everything(**news_params)
    if news['status'] == 'error':
        raise NewsException(news['message'])
    return news['articles']
