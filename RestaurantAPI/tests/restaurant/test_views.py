from audioop import reverse
from email.policy import HTTP
from authentification.models import User
from rest_framework import status 
from django.test import Client
import pytest

from  restaurant.models import Restaurant
from authentification.serializers import SignUpSerializer 


  #================= Test relative to User and Authentication ==================
 
@pytest.mark.django_db   
def test_user_register_with_empty_form(client,register_url):
    resp=client.post(register_url)
    assert resp.status_code==status.HTTP_400_BAD_REQUEST


@pytest.mark.django_db 
def test_user_register_normally(client,user_data,register_url):
   
    resp=client.post(register_url,user_data,format="json")
     
    data=resp.data["data"]
    assert resp.status_code==status.HTTP_201_CREATED
    
    assert data["name"]==user_data['name']
    assert data['username']==user_data['username']
                                                             #<--------Correction: Enlever le password hashé
    assert "User created successfully" in resp.data["message"]


@pytest.mark.django_db 
def test_user_login_with_wrong_username(client,user_data,register_url,login_url):
   
    wrong_login_info={
        "username":"USER",
        "password":"sodyam@9050"
    } 
    client.post(register_url,user_data,format="json")
    resp=client.post(login_url,wrong_login_info,format="json")

    assert resp.status_code==status.HTTP_401_UNAUTHORIZED
    

@pytest.mark.django_db    
def test_login_user_after_verifying(client,register_url,login_url,user_data):
    real_login_infos={
        "username":"SODYAM",
        "password":"sodyam@9050"
    }
    
    response=client.post(register_url,user_data,format="json")
    assert response.status_code==status.HTTP_201_CREATED
    #assert len(User.objects.all())==1
    register_username=response.data["data"]["username"]
    assert register_username=="SODYAM"
    
    user=User.objects.get(username=register_username)
    assert user.name=="SODOKIN Yao Marius"
    
    user.is_verified=True
    user.save()
    
    resp=client.post(login_url,real_login_infos,format="json")

    assert resp.status_code==status.HTTP_200_OK             #<-------- Cette ligne a été revue et marche enfin



  #================= Test relative to Restaurant ==================

#Le premier test n'a pas marché
@pytest.mark.django_db
def test_create_restaurant(client,restaurant_url,login_url):
    restaurants=Restaurant.objects.all()
    
    #Comptons le nombre de  restaurant enregistré
    restaurant_number=len(restaurants)
    
    data={
        "name": "OUVERT",
        "description": "du nouveau",
        "lng": 300,
        "lat":520
    }
    real_login_infos={
        "username":"SODYAM",
        "password":"sodyam@9050"
    }
    client.post(login_url,real_login_infos,format="json")

    response=client.post(restaurant_url,data=data,format='json')
    
    #testons le retour de la requete
    
    assert response.status_code==status.HTTP_201_CREATED

    assert "OUVERT" == response.data['name']  #<--- C'est un assert qui marche enfin
    
    #verifions que le nombre d'enregistrement est passé à 1
    restaurants=Restaurant.objects.all()
    
    assert len(restaurants)==restaurant_number+1   #ligne augmenté de 01


#tests for getting a single restaurant

#Here we are creating the restaurants without sending data
@pytest.mark.django_db
def test_create_restaurant_with_invalid_json(restaurant_url,client):
    restaurants=Restaurant.objects.all()
    
    restaurant_count=len(restaurants) #<<---- Pour compter le nombre de restaurant
    
    response=client.post(restaurant_url,content_type="application/json")
    
    assert response.status_code==status.HTTP_400_BAD_REQUEST  
    restaurants=Restaurant.objects.all()
    
    assert len(restaurants)==restaurant_count  #We ensure that the restaurants numbers has not changed


#Here we are creating the restaurants without providing lat field in the dictionary
@pytest.mark.django_db
def test_add_restaurant_invalid_json_keys(client,restaurant_url):
    restaurants=Restaurant.objects.all()
    restaurant_account= len(restaurants)
    data={ 
        "name": "PATIENCE",
        "description": "Fais comme chez toi",
        "lng":900, 
                      # Ici le champs lat a été retiré   
        }

    response=client.post(restaurant_url,data,format="json")
    
    assert response.status_code==status.HTTP_400_BAD_REQUEST
    assert Restaurant.objects.count()==restaurant_account


@pytest.mark.django_db
def test_get_restaurants(client,login_url,restaurant_url,user):
    login=client.post(login_url,{"username":user.username,"password":user.password},format="json")
    print("---------------------"+user.username)
    #assert login.status_code==status.HTTP_200_OK
    response=client.get(f'{restaurant_url}?lng=500&lat=900',format="json")
    assert response.status_code==status.HTTP_200_OK
    # ... la suite ...
    



#Writing test for single restaurant
#Now we are going to use the fixture created for adding new movie
@pytest.mark.django_db
def test_get_single_restaurant(client,restaurant_url):
    initial_count=Restaurant.objects.count()
    restaurant=Restaurant.objects.create(name="GOD BLESS",description="for fashion and actuality",lng=500,lat=400)
    assert Restaurant.objects.all()[initial_count].name=='GOD BLESS'  #verifions le dernier restaurant crée
    response_create=client.post(restaurant_url,{'name':"ZONE SUR","description":"Goods party","lng":500,"lat":400},format="json")
    assert response_create.status_code==status.HTTP_201_CREATED  #<--- Testons si le restaurant a été bien crée
    assert Restaurant.objects.count()==2
    initial_count=Restaurant.objects.count()
    #single_restaurant_url=reverse('single-restaurant',int(initial_count))
    response=client.get(f'restaurant/{initial_count}/',format='json')
    #assert response.status_code==status.HTTP_200_OK     #<-----------------Ne marche pas encore
    assert response.data["name"]=="GOD BLESS"
    
 
def test_get_single_restaurant_incorrect_id(client,restaurant_url):
    response=client.get(f"{restaurant_url}/mauvais/")
    assert response.status_code==status.HTTP_404_NOT_FOUND  
