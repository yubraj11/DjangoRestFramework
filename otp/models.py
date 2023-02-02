from django.db import models

# Create your models here.
class Otp(models.Model):
    id = models.BigAutoField(primary_key=True)
    email = models.CharField(max_length=255)
    otp = models.CharField(max_length=4)

