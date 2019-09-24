from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Account(models.Model):
    STOCK = '01'
    DERIVATIVE = '03'
    CATEGORY_CHOICES = [
        (STOCK, 'Stock'),
        (DERIVATIVE, 'Derivative')
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    number = models.CharField(max_length=11)
    category = models.CharField(max_length=2, choices=CATEGORY_CHOICES)
    password = models.CharField(max_length=128)
    fund = models.DecimalField(max_digits=10, decimal_places=0)
    is_active = models.BooleanField(default=True)
    date_bound = models.DateField(default=timezone.now)

    def __str__(self):
        return f'{self.number}-{self.category}'
