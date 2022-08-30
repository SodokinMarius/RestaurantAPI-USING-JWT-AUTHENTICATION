'''
@pytest.mark.django_db 
def test_user_register_normally(client):
    user_data={
            "name":"SODOKIN Yao Marius",
            "username":"SODYAM",
            "password":"sodyam@9050"
        }
    register_url=reverse('register')
    resp=client.post(register_url,user_data,format="json")
    client.assertEqual(resp.status_code,201)
        
    client.assertEqual(resp.data['name'],user_data['name'])
    client.assertEqual(resp.data['username'],user_data['username'])
    client.assertEqual(resp.data['password'],user_data['password'])


@pytest.mark.django_db 
def test_user_login_with_wrong_usename(client):
    register_url=reverse('register')
    login_url=reverse('login')
    user_data={
            "name":"SODOKIN Yao Marius",
            "username":"SODYAM",
            "password":"sodyam@9050"
        }
     
    client.post(register_url,user_data,format="json")
    resp=client.post(login_url,user_data,format="json")

    client.assertEqual(resp.status_code,401)

@pytest.mark.django_db    
def test_login_user_after_verifying(client):
    register_url=reverse('register')
    login_url=reverse('login')
    
    user_data={
            "name":"SODOKIN Yao Marius",
            "username":"SODYAM",
            "password":"sodyam@9050"
        }
    response=client.post(register_url,user_data,format="json")
    register_username=response.data["username"]
    user=User.objects.get(username=register_username)
    
    user.is_verified=True
    user.save()
    
    resp=client.post(login_url,user_data,format="json")

    client.assertEqual(resp.status_code,401)


  #================= Test relative to Restaurant ==================

@pytest.mark.django_db
def test_create_restaurant(client):
    url="restaurants"
    restaurants=Restaurant.objects.all()
    
    #Verifions qu'il n'y a aucun film enregistré
    assert len(restaurants)==0
    
    data={
        "name": "OUVERT",
        "description": "du nouveau",
        "lng": 300,
        "lat":520
    }
    
    response=client.post(url,data=data,content_type="application/json")
    
    #testons le retour de la requete
    
    assert response.status_code==status.HTTP_201_CREATED
    assert response.data["name"]=="OUVERT"
    
    #verifions que le nombre d'enregistrement est passé à 1
    restaurants=Restaurant.objects.all()
    
    assert len(restaurants)==1

#tests for getting a single movie

@pytest.mark.django_db
def test_create_restaurant_with_invalid_json(client):
    url="restaurants"    
    restaurants=Restaurant.objects.all()
    assert len(restaurants)==0
    
    response=client.post(url,content_type="application/json")
    
    assert response.status_code==status.HTTP_400_BAD_REQUEST
    restaurants=Restaurant.objects.all()
    
    assert len(restaurants)==0

@pytest.mark.django_db
def test_add_restaurant_invalid_json_keys(client):
    url="restaurants"    
    restaurants=Restaurant.objects.all()
    assert len(restaurants)==0
    data={ 
        "name": "PATIENCE",
        "description": "Fais comme chez toi",
        "lng":900,
        
        }

    content_type="applcation/json"
    
    response=client.post(url,data,content_type)
    
    assert response.status_code==status.HTTP_404_NOT_FOUND
    restaurants=Restaurant.objects.all()
    assert len(restaurants)==0

#Writing test for single restaurant
#Now we are going to use the fixture created for adding new movie
@pytest.mark.django_db
def test_get_single_restaurant(client):
    url="restaurants" 
    restaurant=Restaurant.objects.create(name="GOD BLESS",description="for fashion and actuality",lng=500,lat=400)
    response=client.get("{0}/{1}/".format(url,restaurant.id))
    assert response.status_code==status.HTTP_200_OK
    assert response.data["name"]=="GOD BLESS"
    
    
def test_get_single_restaurant_incorrect_id(client):
    url="restaurants"
    response=client.get(f"{url}/mauvais/")
    assert response.status_code==status.HTTP_404_NOT_FOUND
     
        '''