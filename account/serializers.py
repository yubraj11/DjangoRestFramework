from rest_framework import serializers
from account.models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required = True)
    class Meta:
        model = User
        fields = ['id','username','password', 'email']


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required = True)
    password = serializers.CharField(required = True)
    



