from django.contrib import admin
from django.urls import path , include
from rest_framework import routers
from sendemail.views import SendEmail, SendOTP

urlpatterns = [
    path("sendemail/", SendEmail.as_view()),
    path("forgetpassword/", SendOTP.as_view()),

]