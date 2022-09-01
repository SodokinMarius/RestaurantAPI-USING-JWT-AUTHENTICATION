import os

from django.conf import settings

import pytest 
from django.urls import reverse

from rest_framework.test import APIClient
from authentification.models import User 
from restaurant.models import Restaurant 

DEFAULT_ENGINE="django.db.backends.postgresql_psycopg2"

#fonction definissant les infos de la BD

@pytest.fixture(scope="session")
def django_db_setup():
    settings.DATABASES['default']={
        "ENGINE":os.environ.get("DB_TEST_ENGINE",DEFAULT_ENGINE),
       
        "HOST":os.environ.get("DB_TEST_HOST"),    
        "NAME":os.environ.get("DB_TEST_NAME"),
        "PORT":os.environ.get("DB_TEST_PORT"),

        "USER":os.environ.get("DB_TEST_USER"),
        "PASSWORD":os.environ.get("DB_TEST_PASSWORD"),
        'ATOMIC_REQUESTS': True,
    }
    

@pytest.fixture
def user():
     return User.objects.create(name="SOSOKIN Yao Marius",username="SODYAM",password="sodyam@9050")

@pytest.fixture
def client():
    return APIClient()

@pytest.fixture
def user_data():
    user_data={
            "name":"SODOKIN Yao Marius",
            "username":"SODYAM",
            "password":"sodyam@9050"
        }
    return user_data

@pytest.fixture
def login_url():
    return reverse('user-login')

@pytest.fixture
def register_url():
    return reverse('user-register')

@pytest.fixture
def  restaurant():
    return Restaurant.objects.create(name="FROM YOU",description="Nous aimons la qualite",lng=500,lat=800)

@pytest.fixture
def restaurant_url():
    
    return reverse('restaurants-list')
    