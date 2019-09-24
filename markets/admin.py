from django.contrib import admin
from markets import models

admin.site.register(models.Expiration)
admin.site.register(models.Asset)
admin.site.register(models.Etf)
admin.site.register(models.Future)
