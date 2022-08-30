
from django.contrib import admin
from django.urls import path,include 
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken import views

#from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView



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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('authentification.urls')),
    path('',include('restaurant.urls')),
    path('api-auth/', include('rest_framework.urls')), #<---- Pour l'authentication
    #------- swagger urls -----------
    
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    
    # ------------ Spectaculor urls -----
    # YOUR PATTERNS
    #path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
     #Optional UI:
    #path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    #path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]

urlpatterns = format_suffix_patterns(urlpatterns)


#requiring login before all action with the API
urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]