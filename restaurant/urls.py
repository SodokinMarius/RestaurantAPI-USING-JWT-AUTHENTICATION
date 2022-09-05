
from django.contrib import admin
from django.urls import path,include

from .viewsets import RestaurantViewSet
from rest_framework.routers import SimpleRouter 


router=SimpleRouter()

router.register('restaurants',RestaurantViewSet,basename='restaurants-list')

urlpatterns=[ 
            path('',include(router.urls)),
             
             ]

