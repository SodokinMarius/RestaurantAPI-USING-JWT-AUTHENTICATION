
from django.contrib import admin
from django.urls import path,include

from .viewsets import RestaurantViewSet
from rest_framework.routers import SimpleRouter 


routeur=SimpleRouter()

routeur.register('restaurants/',RestaurantViewSet,basename='restaurants-list')

urlpatterns=[ 
            path('',include(routeur.urls)),
             
             ]

