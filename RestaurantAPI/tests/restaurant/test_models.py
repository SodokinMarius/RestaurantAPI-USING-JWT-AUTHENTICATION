import pytest

from restaurant.models  import Restaurant

#Test that verify a restaurant creating
@pytest.mark.django_db #<--------  Important pour donner accès à la BD 
def test_restaurant_model():
    restaurant=Restaurant(name="Nouveau R",description="A new", lng=500,lat=500)
    restaurant.save()
    assert restaurant.name=="Nouveau R"
    assert restaurant.description=="A new"
    assert restaurant.lng==500
    assert restaurant.lat==500
    assert str(restaurant)==restaurant.name
    
    
  
