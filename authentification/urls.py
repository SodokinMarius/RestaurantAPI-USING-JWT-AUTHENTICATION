
from posixpath import basename
from django.contrib import admin
from django.urls import path,include
from rest_framework import authtoken
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from authentification import views
from rest_framework.routers import DefaultRouter

'''router=DefaultRouter()
router.register('register/',views.SignUpView.as_view(),basename='user-register')
router.register('login/',views.LoginView.as_view(),basename='user-login')
router.register('api_keys/',TokenObtainPairView.as_view(),basename='api_keys')
'''
urlpatterns = [
    path('register/',views.SignUpView.as_view(),name='user-register'),
    path('login/',views.LoginView.as_view(),name='user-login'),
    path('api_keys/',TokenObtainPairView.as_view(),name='api_keys'),
    #path('api_token_refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    #path('',include(router.urls))
    ]

