from django.db import models
from django.utils import timezone


class Expiration(models.Model):
    code = models.CharField(max_length=4, primary_key=True)
    date_expired = models.DateField(default=timezone.now)

    def __str__(self):
        return self.code


class Asset(models.Model):
    # Market choices
    INDEX = 'I'
    STOCK = 'S'
    MARKET_CHOICES = [
        (INDEX, 'Index'),
        (STOCK, 'Stock'),
    ]
    market = models.CharField(max_length=2, choices=MARKET_CHOICES)
    code = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=20)
    has_future = models.BooleanField(default=False)
    has_option = models.BooleanField(default=False)
    is_kospi = models.BooleanField(default=False)
    is_kospi_200 = models.BooleanField(default=False)
    is_kospi_100 = models.BooleanField(default=False)
    is_kospi_50 = models.BooleanField(default=False)
    is_kosdaq = models.BooleanField(default=False)
    is_kosdaq_150 = models.BooleanField(default=False)
    is_primary = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Etf(models.Model):
    # Position choices
    UP = 'U'
    DOWN = 'D'
    DIRECTION_CHOICES = [
        (UP, 'Up'),
        (DOWN, 'Down'),
    ]
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    code = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=20)
    direction = models.CharField(max_length=1, choices=DIRECTION_CHOICES)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Future(models.Model):
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    code = models.CharField(max_length=20, unique=True)
    expiration = models.ForeignKey(Expiration, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        name = f'{self.asset} F {self.expiration}'
        return name
