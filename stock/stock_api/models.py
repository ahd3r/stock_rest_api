from django.db import models
from django.conf import settings

class StockModel(models.Model):
    name=models.CharField(max_length=50)
    market_place=models.ForeignKey('MarketPlaceModel', on_delete=models.CASCADE, blank=True, null=True)
    price=models.IntegerField()
    grow_price=models.IntegerField()
    image=models.ImageField(upload_to='stock/', null=True, blank=True)
    created=models.DateTimeField(auto_now_add=True)
    modified=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class MarketPlaceModel(models.Model):
    name=models.CharField(max_length=50)
    description=models.TextField()

    def __str__(self):
        return self.name
