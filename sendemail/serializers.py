from rest_framework import serializers
from account.models import User

class EmailSerializer(serializers.Serializer):
    subject = serializers.CharField(required=True)
    email = serializers.CharField(required=True)
    message = serializers.CharField(required=True)


class OTPSerializer(serializers.Serializer):
    email = serializers.CharField(required=True)
