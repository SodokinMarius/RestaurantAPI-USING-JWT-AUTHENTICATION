from restaurant.serializers import RestaurantSerializer
from rest_framework import status 

def test_restaurant_serializer_validation():
    valid_serializer_data={
         'name':"Nouveau R",
         'description':"combat",
         'lng': "500",
         'lat':"560",   
     }
     
    serializer=RestaurantSerializer(data=valid_serializer_data)
    assert serializer.is_valid()
    assert serializer.data==valid_serializer_data
    assert serializer.errors=={}


def test_creating_invalid_restaurant_serializer():
    invalid_serializer_data={
         "name":"Nouveau",
         "description":"combat",
         "lng":700  
         }
     
    serializer=RestaurantSerializer(data=invalid_serializer_data)
    assert not serializer.is_valid()
    assert serializer.validated_data=={}
    assert serializer.data==invalid_serializer_data
    assert serializer.errors == {"lat": ["This field is required."]}

    assert 'This field is required.'in serializer.errors['lat']

    

   