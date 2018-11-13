from rest_framework import serializers
from .models import StockModel, MarketPlaceModel
from django.contrib.auth.models import User

class StockSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=StockModel
        fields=['url', 'name', 'price', 'grow_price', 'market_place', 'image', 'created']

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','email','first_name','last_name','is_active']

class MarketPlaceSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=MarketPlaceModel
        fields=['url','name','description']

class UserCreationFormSerializers(serializers.ModelSerializer):
    def create(self, validated_data):
        user=User.objects.create_user(username=validated_data['username'], password=validated_data['password'])
        user.save()
        return user

    class Meta:
        model=User
        fields=['username', 'password']
