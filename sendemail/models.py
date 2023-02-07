from django.db import models



class OnetimePassword(models.Model):
    id = models.BigAutoField(primary_key=True)
    email = models.CharField(max_length=255)
    otp = models.CharField(max_length=4)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email