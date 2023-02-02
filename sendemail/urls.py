from django.contrib import admin
from django.urls import path , include
from rest_framework import routers
from sendemail.views import SendEmail, SendOTP, validateOTP, ForgetPassword

urlpatterns = [
    path("sendemail/", SendEmail.as_view()),
    path("sendotp/", SendOTP.as_view()),
    path("validateotp/",validateOTP.as_view()),
    path("forgetpassword/", ForgetPassword.as_view())

]