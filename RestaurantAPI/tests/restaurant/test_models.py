import pytest

from restaurant.models  import Restaurant
from authentification.models import User

#Test that verify a restaurant creating
@pytest.mark.django_db #<--------  Important pour donner accès à la BD 
def test_restaurant_model():
    owner=User.objects.get(id=1)
    restaurant=Restaurant(1,name="Nouveau R",description="A new", lng=500,lat=500,owner=owner)
    restaurant.save()
    assert restaurant.name=="Nouveau R"
    assert restaurant.description=="A new"
    assert restaurant.lng==500
    assert restaurant.lat==500
    assert str(restaurant)==restaurant.name
    
    
  
