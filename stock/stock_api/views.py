from django.shortcuts import render

from rest_framework import viewsets, filters
from .models import StockModel, MarketPlaceModel
from .serializers import StockSerializers, UserSerializers, MarketPlaceSerializers, UserCreationFormSerializers
from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny

class StockView(viewsets.ModelViewSet):
    queryset=StockModel.objects.all().order_by('-id')
    serializer_class=StockSerializers
    filter_backends = (filters.SearchFilter,DjangoFilterBackend)
    filter_fields=('name', 'price', 'grow_price', 'market_place', 'created',)
    search_fields=('name',)

class UserView(viewsets.ReadOnlyModelViewSet):
    queryset=User.objects.all().order_by('username')
    serializer_class=UserSerializers

class MarketPlaceView(viewsets.ModelViewSet):
    queryset=MarketPlaceModel.objects.all().order_by('-id')
    serializer_class=MarketPlaceSerializers

class UserCreationView(CreateAPIView):
    model=User
    permission_classes = (AllowAny,)
    serializer_class = UserCreationFormSerializers
