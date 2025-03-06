from django.contrib import admin

from .models import FinancialOrganization, FinancialOrganizationNews

admin.site.register(FinancialOrganization)
admin.site.register(FinancialOrganizationNews)
