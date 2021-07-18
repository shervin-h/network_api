from django.db import models


class Network(models.Model):
    chainId = models.IntegerField()
    symbol = models.CharField(max_length=100)
    name = models.CharField(max_length=300)
    decimals = models.IntegerField(null=True, blank=True)
    eip2612 = models.BooleanField(null=True, blank=True)
    address = models.TextField(max_length=300, null=True, blank=True)
    logoURI = models.TextField(null=True, blank=True)
    logo = models.TextField(null=True, blank=True)
    decimal = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return "<Network - Symbol: {} | Name: {}>".format(self.symbol, self.name)
