
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.validators import ValidationError

from restaurant.models import Restaurant
from .models import User
from django.contrib import auth
#from django.contrib.auth.models import User 
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from rest_framework.exceptions import AuthenticationFailed


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




class LoginSerializer(serializers.ModelSerializer):
    name=serializers.CharField(max_length=100,read_only=True)
    username=serializers.CharField(max_length=50)
    password=serializers.CharField(max_length=50,write_only=True)
    tokens=serializers.SerializerMethodField()
    
    def get_tokens(self, object):
        user = User.objects.get(username=object['username'])
        
        return {
            'refresh': user.create_jwt_pair_for_user()['refresh'],
            'access': user.create_jwt_pair_for_user()['access']
        }
        
    class Meta:
        model=User
        fields=('id','name','username','password','tokens')
        read_only_fields=('id','name','tokens',)
    
    def validate(self, attrs):
        username=attrs.get('username','')
        password=attrs.get('password','')
        user=auth.authenticate(username=username,password=password)

        if user is None :
            raise AuthenticationFailed('Invalid credentials, please try again !')
        
        if not user.is_active:
            raise AuthenticationFailed("This account is disabled, contact admin !")
        if not user.is_verified:
            raise AuthenticationFailed("Username is not verified !")


    #tokens creating
        self.tokens= {
            'refresh':user.create_jwt_pair_for_user()['refresh'],
            'access': user.create_jwt_pair_for_user()['access']
        }
        user.tokens=self.tokens

        return {
                "username":user.username,
                "password":user.password,
                "tokens":user.tokens
            }
            
        return super().validate(attrs)

