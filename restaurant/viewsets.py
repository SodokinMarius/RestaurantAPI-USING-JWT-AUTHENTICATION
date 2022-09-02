from django.shortcuts import render
#--------- ViewSet import ------------------
from rest_framework import generics, status 
from rest_framework.request import Request 

from rest_framework.response import Response

from .models import Restaurant 
from .serializers import RestaurantSerializer

from rest_framework.views import APIView
from math import *
 
from django.http import Http404

from django.contrib.auth.models import User
from authentification.serializers import SignUpSerializer,UserSerializer
from django.contrib.auth import get_user_model

#imports for permissions
from rest_framework import permissions 
from rest_framework.authentication import TokenAuthentication
from rest_framework.viewsets import ModelViewSet

from .permissions import AuthorOrReadOnly,ReadOnly


class RestaurantViewSet(ModelViewSet):
    serializer_class = RestaurantSerializer
    queryset = Restaurant.objects.all()
    #la permission à exploiter pour l'authentification
    #authentication_classes = (TokenAuthentication,)

    permission_classes=[permissions.AllowAny] #l'utilisateur doit d'abord s'authentifier d'abord avant tout
    
    def list(self,request,*args,**kwargs):
         #Distance, d = (3963.0 * arccos[(sin(lat1) * sin(lat2)) + cos(lat1) * cos(lat2) * cos(long2 – long1)])*1.609344 
         #Les coordonnées rensignées par l'utilisateur
        longitude=float(request.GET.get("lng"))
        latitude=float(request.GET.get("lat"))
        
        nearbyRestaurants=[]
        restaurants = Restaurant.objects.all()

        #Recherche des restaurants
        for restaurant in restaurants:
            #les coordonnées du rectaurant en tour de parcours
            current_long=restaurant.lng
            current_lat=restaurant.lat
            distance=(3963.0 * acos((sin(latitude) * sin(current_lat)) + cos(latitude) * cos(current_lat) * cos(current_long - longitude)))*1.609344

            if distance<=3:
                nearbyRestaurants.append(restaurant)

        serializer=self.get_serializer(nearbyRestaurants,many=True)
        return Response(serializer.data)
        
    #Associons maintenant les Restaurants aux utilisateurs les ayant créer
    #Ce qui permet de savoir celui qui a fait une action donnée
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        
        
    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user) #Renvoyer uniquemenUser donnét les données d'un 