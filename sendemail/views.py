from django.shortcuts import render
from rest_framework.response import Response
from .serializers import EmailSerializer, OTPSerializer, ValidateOtpSerializer, ForgetPasswordSerializer
from rest_framework import generics
from django.core.mail import send_mail
from decouple import config
import random
from django.contrib.auth.models import User
from .models import Otp
from django.contrib.auth.hashers import make_password


######change email id of sender in .env 

class SendEmail(generics.GenericAPIView):
    serializer_class = EmailSerializer
    def post(self, request):
        serializer = EmailSerializer(data=request.data)
        if serializer.is_valid():
            succ= send_mail(
                request.data.get('subject'),
                request.data.get('message'),
                config('EMAIL_HOST_USER'),
                [request.data.get('email')],
                fail_silently=False
            )
            if succ:
                return Response({
                    'status': 200,
                    'message': 'Mail Sent Successfully',
                })
        return Response({
            'status':400,
            'message': 'Couldnot send Email'
        })

class SendOTP(generics.GenericAPIView):
    serializer_class = OTPSerializer
    queryset = User.objects.all()
    def post(self,request):
        serializer = OTPSerializer(data=request.data)
        if serializer.is_valid():
            db = User.objects.filter(email=request.data.get('email')).first()
            if db:
                otp = random.randint(1000,9999)
                check = Otp.objects.filter(email=request.data.get('email')).first()
                if check:
                    check.otp = otp
                    check.save()
                else:
                    o = Otp(email=request.data.get('email'), otp=otp)
                    o.save()
                succ=send_mail(
                    'OTP Verification',
                    f'Your OTP code is: {otp}',
                    config('EMAIL_HOST_USER'),
                    [request.data.get('email')],
                    fail_silently=False
                )
                if succ:
                    return Response({
                        'status':200,
                        'message': 'OTP Sent'
                    })
        return Response({
            'status':400,
            'message': 'Couldnot send OTP'
        })

class validateOTP(generics.GenericAPIView):
    serializer_class = ValidateOtpSerializer

    def post(self, request):
        serializer = ValidateOtpSerializer(data=request.data)
        if serializer.is_valid():
            obj = Otp.objects.filter(email=request.data.get('email'), otp=request.data.get("otp")).first()
            if obj:
                return Response({
                    "status":200,
                    "message":"otp validated",
                    })
        return Response({
            "status": 400,
            "message": "Bad request"
        }, status=400)

class ForgetPassword(generics.GenericAPIView):
    serializer_class=ForgetPasswordSerializer
    def post(self, request):
        serializer = ForgetPasswordSerializer(data=request.data)
        if serializer.is_valid():
            db = User.objects.filter(email=request.data.get('email')).first()
            if db:
                obj = Otp.objects.filter(email=request.data.get('email'), otp=request.data.get('otp'))
                if obj:
                    newpassword = make_password(request.data.get('newpassword'))
                    db.password = newpassword
                    db.save()
                    return Response({
                        "status":200,
                        "message":"Password Updated Successfully"
                    },status=200)
        
        return Response({
            "status":400,
            "message":"Bad Request"
        },status=400)
# Create your views here.
