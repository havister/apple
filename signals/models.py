from django.db import models
from django.utils import timezone


class Signal(models.Model):
    name = models.CharField(max_length=20)
    creator = models.CharField(max_length=20)
    is_active = models.BooleanField(default=True)
    date_created = models.DateField(default=timezone.now)

    def __str__(self):
        return self.name
