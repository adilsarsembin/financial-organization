from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField


class FinancialOrganization(models.Model):
    name = models.CharField(verbose_name=_('Название'), max_length=512)
    director_board_chairman = models.CharField(verbose_name=_('Председатель Совета директоров'), max_length=512, null=True, blank=True)
    management_board_chairman = models.CharField(verbose_name=_('Председатель Правления'), max_length=512, null=True, blank=True)
    directors_board = models.CharField(verbose_name=_('Совет директоров'), max_length=512, null=True, blank=True)
    management_board_members = models.CharField(verbose_name=_('Члены Правления'), max_length=512, null=True, blank=True)
    chief_accountant = models.CharField(verbose_name=_('Председатель Совета директоров'), max_length=512, null=True, blank=True)
    bin = models.CharField(verbose_name=_('БИН'), max_length=12)
    address = models.CharField(verbose_name=_('Адрес'), max_length=512, help_text=_('Город, улица, дом, квартира'), null=True, blank=True)
    phone_number = PhoneNumberField(verbose_name=_('Телефон'), null=True, blank=True)
    email = models.EmailField(verbose_name=_('E-mail'), null=True, blank=True)
    url = models.URLField(verbose_name=_('Web-сайт'), null=True, blank=True)
    license = models.CharField(verbose_name=_('Лицензия'), max_length=512, null=True, blank=True)

    def __str__(self):
        return f'Финансовая организация {self.name}'


class FinancialOrganizationNews(models.Model):
    created_at = models.DateTimeField(_('Время создания'), auto_now_add=True, db_index=True)
    content = models.TextField(_('Контент'))
    title = models.CharField(_('Заголовок'), max_length=512)
    financial_organization = models.ForeignKey(
        verbose_name=_('Финансовая организация'),
        to=FinancialOrganization,
        on_delete=models.CASCADE,
        related_name='news',
    )

    def __str__(self):
        return f'Новость {self.financial_organization}'

    class Meta:
        ordering = ['-created_at']
