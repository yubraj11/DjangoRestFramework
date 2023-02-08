from django.db import models


class User(models.Model):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=16)
    email = models.CharField(max_length=255, null=True)
    phone = models.CharField(max_length=255)

    REQUIRED_FIELDS = ['username', 'password', 'email']
    
    def __str__(self):
        return self.username

