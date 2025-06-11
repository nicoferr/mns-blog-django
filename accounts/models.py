from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True, verbose_name='Avatar')
    phone = models.CharField(max_length=15, null=True, blank=True, verbose_name='Téléphone')
    address = models.TextField(null=True, blank=True, verbose_name="Adresse")
    latitude = models.FloatField(null=True, blank=True, verbose_name='Latitude')
    longitude = models.FloatField(null=True, blank=True, verbose_name='Longitude')

    def __str__(self):
        return f'Profile of {self.user.username}'