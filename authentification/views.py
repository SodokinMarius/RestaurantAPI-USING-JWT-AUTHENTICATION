from rest_framework import generics, status 
from rest_framework.request import Request 
from .models import User 

from rest_framework.response import Response 
from rest_framework.views import APIView

from .serializers import SignUpSerializer,LoginSerializer


from authentification import serializers


# For reviewing
'''from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.tokens import RefreshToken'''

 
class SignUpView(generics.GenericAPIView):
    serializer_class=SignUpSerializer

    permission_classes=[]

    
    def post(self,request:Request):
        data=request.data 

        serializer=self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            
            response={"message": "User created successfully", "data":serializer.data}

            return Response(data=response,status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    
class LoginView(generics.GenericAPIView):
    serializer_class=LoginSerializer

    permission_classes=[]

    def post(self,request:Request):
        serializer=self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data,status=status.HTTP_200_OK) 
     
        
'''token_param_config=openapi.Parameter('token',in_=openapi.IN_QUERY,description='Description',type=openapi.TYPE_STRING)

    @swagger_auto_schema(manual_parameters=[token_param_config])   
    def get(self,request:Request):
        content={"user":str(request.user), "auth":str(request.auth)}
        return Response(data=content,status=status.HTTP_200_OK)

'''
'''
class SignUpView(ModelViewSet, TokenObtainPairView):
    serializer_class = SignUpSerializer
    permission_classes = (AllowAny,)
    http_method_names = ['post']

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        res = {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }

        return Response({
            "user": serializer.data,
            "refresh": res["refresh"],
            "token": res["access"]
        },status=status.HTTP_201_CREATED)
                        
class LoginView(ModelViewSet, TokenObtainPairView):
    serializer_class = LoginSerializer
    permission_classes = (AllowAny,)
    http_method_names = ['post']

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])

        return Response(serializer.validated_data, status=status.HTTP_200_OK)
'''
