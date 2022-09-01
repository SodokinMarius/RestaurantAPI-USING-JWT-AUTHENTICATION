from rest_framework import generics, status 
from rest_framework.request import Request 
from .models import User 

from rest_framework.response import Response 
from rest_framework.views import APIView

from .serializers import SignUpSerializer,LoginSerializer,UserSerializer


from authentification import serializers


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
     
