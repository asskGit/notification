from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model


class User(AbstractUser):
    email = models.EmailField(unique=True)
    notifications = models.JSONField(default=list, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Transaction(models.Model):
    STATUS_CHOICES = (
        ('В ожидании', 'В ожидании'),
        ('Не оплачен', 'Не оплачен'),
        ('Оплачен', 'Оплачен')
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='transactions')
    amount = models.IntegerField(verbose_name='Сумма оплаты')
    status = models.CharField(choices=STATUS_CHOICES, max_length=40, verbose_name="Статус")
    date_transfer = models.DateField(verbose_name='Дата перевода', null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.user}'

    class Meta:
        verbose_name = 'Транзакция'
        verbose_name_plural = 'Транзакции'
