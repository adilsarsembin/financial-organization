from rest_framework import viewsets
from .models import FinancialOrganization
from .serializers import OrganizationSerializer


class OrganizationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = FinancialOrganization.objects.prefetch_related('news')
    serializer_class = OrganizationSerializer
