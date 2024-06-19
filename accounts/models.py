from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
import datetime

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=12)
    address = models.CharField(max_length=200, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)

    def __str__(self):
        return self.username
    
def default_expires_at():
    return timezone.now() + datetime.timedelta(minutes=5)

class OTP(models.Model):
    email = models.EmailField()
    otp = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField(default=default_expires_at)

    @property
    def is_expired(self):
        return timezone.now() > self.expires_at
