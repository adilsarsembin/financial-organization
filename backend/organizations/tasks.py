from celery import shared_task
import requests
from django.conf import settings
from .models import FinancialOrganization, FinancialOrganizationNews


@shared_task
def update_news():
    organizations = FinancialOrganization.objects.all()
    for org in organizations:
        try:
            response = requests.get(
                f'https://newsapi.org/v2/everything?q={org.name}&apiKey={settings.NEWS_API_KEY}'
            )
            response.raise_for_status()
            news_data = response.json().get('articles', [])
            for news_item in news_data:
                if not FinancialOrganizationNews.objects.filter(organization=org, url=news_item['url']).exists():
                    FinancialOrganizationNews.objects.create(
                        organization=org,
                        title=news_item['title'],
                        summary=news_item['description'] or '',
                        url=news_item['url'],
                        published_date=news_item['publishedAt']
                    )
        except requests.RequestException as e:
            print(f"Error fetching news for {org.name}: {e}")
