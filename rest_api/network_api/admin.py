from django.contrib import admin
from network_api import models
# Register your models here.


class NetworkAdmin(admin.ModelAdmin):
    list_display = ['name', 'symbol', 'address']
    # list_filter = ['name', 'symbol']
    search_fields = ('name', 'symbol', 'address')


admin.site.register(models.Network, NetworkAdmin)

