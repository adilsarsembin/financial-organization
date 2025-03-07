from rest_framework import serializers
from .models import FinancialOrganization, FinancialOrganizationNews


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinancialOrganizationNews
        fields = ['created_at', 'title', 'content']


class OrganizationSerializer(serializers.ModelSerializer):
    news = NewsSerializer(many=True, read_only=True)

    class Meta:
        model = FinancialOrganization
        fields = ['id', 'name', 'address', 'email', 'news']
