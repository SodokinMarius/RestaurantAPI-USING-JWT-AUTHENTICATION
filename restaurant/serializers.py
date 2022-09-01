from rest_framework import serializers

from .models import Restaurant
from authentification.models import User

class RestaurantSerializer(serializers.ModelSerializer):
    
    owner = serializers.ReadOnlyField(source='Restaurant.owner.username') #l'objectif est d'associer le user à l'action
    class Meta:
        model=Restaurant
        fields=('pk','name','description','lng','lat','created_at','updated_date','owner')  #Ajoutons le owner aux champs de serialization
        read_only_fields=('id','created_at','updated_date',)
        lookup_field = "pk"