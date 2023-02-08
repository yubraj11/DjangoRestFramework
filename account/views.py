from django.shortcuts import render
from .serializers import UserSerializer, LoginSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.core.mail import send_mail
from decouple import config

class Login(generics.GenericAPIView):
    
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = LoginSerializer(data = request.data)
        if serializer.is_valid():
            user = authenticate(username = request.data.get("username"), password = request.data.get("password"))
            if user:
                refresh_token = RefreshToken.for_user(user)
                return Response({
                    'refresh': str(refresh_token),
                    'access': str(refresh_token.access_token),
                })
        
        return Response({
            'status':401,
            'message':'invalid Username or Password',
        }, status=401)



class Register(generics.GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request):
        data = request.data
        serializer = UserSerializer(data = data)
        if serializer.is_valid():
            link = "www.google.com"
            succ =  send_mail(
                "Validate Your User Account",
                f"Please follow the link to validate your account {link}",
                config('EMAIL_HOST_USER'),
                [request.data.get('email')],
                fail_silently=False
            )
            if succ:
                serializer.save()
                return Response({
                    "message":"User Created"
                },status=200)

        return Response({
            "message":"error occured"
        }, status=400)

            