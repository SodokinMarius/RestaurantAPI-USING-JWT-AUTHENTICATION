
from django.contrib import admin
from django.urls import path,include 
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.urlpatterns import format_suffix_patterns

from authentification.viewsets import LoginViewSet,UserViewSet,SignupViewSet
from rest_framework.routers import SimpleRouter


from rest_framework.authtoken import views


schema_view = get_schema_view(
   openapi.Info(
      title="Restaurant API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@restaurant.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)



router=SimpleRouter()


router.register('user',UserViewSet,basename='users') #<---- Users Urls


urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('user_auth/', views.obtain_auth_token),  #<-- endpoint utilisé enfin pour le token authentication

    path('',include('authentification.urls')),   # <----- authentification urls
    
    
    path('',include(router.urls)),    # <--------- main app Urls
    

    path('',include('restaurant.urls')),   #<------ Restaurants urls
    
    #------- swagger urls -----------
    
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    
]

urlpatterns = format_suffix_patterns(urlpatterns)


#requiring login before all action with the API
urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]