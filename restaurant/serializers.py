from dataclasses import fields
from rest_framework import serializers

from .models import Restaurant
from authentification.models import User

class RestaurantSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(queryset=User.objects.all()) #<----------champ ajouté

    #owner = serializers.ReadOnlyField(source='owner.username') #l'objectif est d'associer le user à l'action
    class Meta:
        model=Restaurant
        fields=('pk','name','description','lng','lat','created_at','updated_date','owner')  #Ajoutons le owner aux champs de serialization
        read_only_fields=('pk','created_at','updated_date','owner')
        #lookup_field = "pk"