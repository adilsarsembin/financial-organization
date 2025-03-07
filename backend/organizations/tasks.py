from celery import shared_task
from django.db import transaction

from organizations.models import FinancialOrganization, FinancialOrganizationNews
from services.integrations.news import get_news

@shared_task
def update_news():
    """Task for news synchronization. Period is set up in Admin Page"""
    organizations = FinancialOrganization.objects.all()
    for organization in organizations:
        news = get_news(organization.name)
        with transaction.atomic():
            for article in news['articles']:
                FinancialOrganizationNews.objects.get_or_create(
                    title=article['title'],
                    financial_organization=organization,
                    defaults={
                        'content': article['description']
                    }
                )
