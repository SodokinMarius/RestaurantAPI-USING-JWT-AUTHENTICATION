from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated,AllowAny
from .serializers import LoginSerializer, SignUpSerializer,UserSerializer
from .models import User 
from rest_framework.response import Response 
from rest_framework import  status 



class UserViewSet(ModelViewSet):
    http_method_names = ['get']
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)  #<------Pour le moment (pour d'abord tester les fonctionalités)
   
    def get_queryset(self):
        if self.request.user.is_superuser:
            return User.objects.all()

    def get_object(self):
        lookup_field_value = self.kwargs[self.lookup_field]

        user = User.objects.get(lookup_field_value)
        self.check_object_permissions(self.request, user)

        return user


class LoginViewSet(ModelViewSet):
    
    permission_classes=[AllowAny] #<--------- Pour le moment
    serializer_class=LoginSerializer 
    
    def create(self, request, *args, **kwargs):
        serializer=self.get_serializer(data=request.data)
        
        if serializer.is_valid() :
            response={"message": "User connected successfully. ","data":serializer.validated_data}
            return Response(data=response,status=status.HTTP_200_OK)
        return  Response(data=serializer.errors,status_code=status.HTTP_400_BAD_REQUEST)
        
    
   
class SignupViewSet(ModelViewSet):
    
    serializer_class = SignUpSerializer
    permission_classes = (AllowAny,)
    http_method_names = ['post']

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        serializer.is_valid(raise_exception=True)  #New Correction from here
        serializer.save()
        response={"message": "User created successfully. ","data":serializer.validated_data}
        return Response(data=response,status=status.HTTP_200_OK)

        
        
         
       

        
            