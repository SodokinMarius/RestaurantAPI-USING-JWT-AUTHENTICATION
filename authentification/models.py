from django.db import models
from django.contrib.auth.models import AbstractUser,AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import UserManager
from django.contrib.auth.base_user import BaseUserManager

from rest_framework_simplejwt.tokens import RefreshToken  #for double keys creating

class CustomUserManager(BaseUserManager):
    def create_user(self,name, username, password=None):
        
        if username is None:
            raise TypeError('Users must have a name.')
            
        if username is None:
            raise TypeError('Users must have a username.')
             
        user = self.model(name=name,username=username)
        
        user.set_password(password)

        user.save(using=self._db)

        return user

    def create_superuser(self,username, password,name="default"):
        if not username:
            raise ValueError("User must have an username")
        if not password:
            raise ValueError("User must have a password")
        if not name:
            raise ValueError("User must have a full name")


        user=self.create_user(name,username,password)
        user.admin = True
        user.staff = True
        user.active = True
        user.save(using=self._db)
        return user



class User(AbstractBaseUser,PermissionsMixin):
    name=models.CharField(max_length=100)
    username=models.CharField(max_length=255,unique=True)
    is_verified = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    objects = CustomUserManager()

    USERNAME_FIELD="username"
    
    def __str__(self):
        return f'{self.username} | {self.password}'

  
    def create_jwt_pair_for_user(self):
        refresh=RefreshToken.for_user(self)
        tokens={"access":str(refresh.access_token),"refresh":str(refresh)}
        return tokens
    
        