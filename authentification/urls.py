
from django.contrib import admin
from django.urls import path,include
from rest_framework import authtoken
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from  .viewsets import SignupViewSet,LoginViewSet
from rest_framework.routers import SimpleRouter


router=SimpleRouter()

router.register('register',SignupViewSet,basename='user-register')
router.register('login',LoginViewSet,basename='user-login')
   

urlpatterns = [
    path('api_keys/',TokenObtainPairView.as_view(),name='api_keys'),

    path('',include(router.urls))
 
]