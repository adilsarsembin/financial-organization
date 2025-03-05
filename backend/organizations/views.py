from rest_framework import viewsets
from .models import FinancialOrganization, FinancialOrganizationNews
from .serializers import OrganizationSerializer, NewsSerializer


class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = FinancialOrganization.objects.all()
    serializer_class = OrganizationSerializer


class NewsViewSet(viewsets.ModelViewSet):
    queryset = FinancialOrganizationNews.objects.all()
    serializer_class = NewsSerializer
