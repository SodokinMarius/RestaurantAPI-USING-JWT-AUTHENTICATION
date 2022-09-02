
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.validators import ValidationError

from restaurant.models import Restaurant
from .models import User
from django.contrib import auth
#from django.contrib.auth.models import User 
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from rest_framework.exceptions import AuthenticationFailed

from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.settings import api_settings
from django.contrib.auth.models import update_last_login
from django.core.exceptions import ObjectDoesNotExist


class UserSerializer(serializers.ModelSerializer):
    restaurants=serializers.PrimaryKeyRelatedField(many=True,queryset=Restaurant.objects.all())  #<-- Gerer en retour la relation
    class Meta:
        model=User
        fields=['id','name','username','password','is_verified','is_active','is_staff','created_at','updated_at','restaurants']
        read_only_fields=('is_verified','is_active','is_staff','created_at','updated_at')
        lookup_field="username"
        
    
class SignUpSerializer(serializers.ModelSerializer):

    class Meta:
        model=User 
        fields=['name','username','password','is_verified','is_active','is_staff','created_at','updated_at']
        read_only_fields=('is_verified','is_active','is_staff','created_at','updated_at')
    
    def create(self,validated_data):
        try:
            user=User.objects.get(username=validated_data['username'])
        except User.DoesNotExist:
            user=User.objects.create_user(**validated_data)
       
        return user


class LoginSerializer(TokenObtainPairSerializer):
    serializer_class=UserSerializer
    def validate(self, attrs):
        user_data= super().validate(attrs)

        token_refresh = self.get_token(self.user)

        user_data['user'] = self.serializer_class(self.user).data
        user_data['refresh'] = str(token_refresh)
        user_data['access'] = str(token_refresh.access_token)

        if api_settings.UPDATE_LAST_LOGIN:
            update_last_login(None, self.user)

        return user_data



