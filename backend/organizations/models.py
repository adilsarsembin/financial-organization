from django.db import models


class FinancialOrganization(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    license_number = models.CharField(max_length=50, blank=True)
    category = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name


class FinancialOrganizationNews(models.Model):
    organization = models.ForeignKey(FinancialOrganization, related_name='news', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    summary = models.TextField()
    url = models.URLField(unique=True)
    published_date = models.DateTimeField()

    def __str__(self):
        return self.title
