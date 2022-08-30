from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from ..authentification.models import User

from RestaurantAPI import settings

User=get_user_model()

def create_jwt_pair_for_user(user:User):
    refresh=RefreshToken.for_user(user)
    tokens={"access":str(refresh.access_token),"refresh":str(refresh)}
    return tokens