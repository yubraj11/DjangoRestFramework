from django.contrib import admin
from django.urls import path , include
from rest_framework import routers
from account.views import Login, Register, TokenValidation
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path("login/", Login.as_view()),
    path("register/", Register.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('token/<str:token>',TokenValidation)

]
