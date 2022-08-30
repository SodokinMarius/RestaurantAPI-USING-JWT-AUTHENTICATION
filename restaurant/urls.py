
from django.contrib import admin
from django.urls import path,include

from . import views
from rest_framework.routers import DefaultRouter 

'''router=DefaultRouter()

router.register('restaurants/',views.RestaurantAPIView.as_view(),basename='restaurants')
router.register('restaurants/<int:pk>/',views.RestaurantDetail.as_view(),basename='single-restaurant')

urlpatterns = [
    path('',include(router.urls)),
]'''

urlpatterns=[ 
            path('restaurants/',views.RestaurantAPIView.as_view(),name='restaurants-list'),
            path('restaurants/<int:pk>/',views.RestaurantDetail.as_view(),name='single-restaurant'),
             
             #Urls pour obtenir la liste des utilisateurs
            #path('users/', views.UserList.as_view()),
            #path('users/<int:pk>/', views.UserDetail.as_view()),
             
             ]

#urlpatterns = format_suffix_patterns(urlpatterns)

