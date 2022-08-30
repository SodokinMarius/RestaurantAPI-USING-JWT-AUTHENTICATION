from rest_framework import serializers

from .models import Restaurant

class RestaurantSerializer(serializers.ModelSerializer):
    
    owner = serializers.ReadOnlyField(source='owner.username') #l'objectif est d'associer le user à l'action
    class Meta:
        model=Restaurant
        fields=('id','name','description','lng','lat','created_at','updated_date','owner')  #Ajoutons le owner aux champs de serialization
        read_only_fields=('id','created_at','updated_date')
        lookup_field = "id"