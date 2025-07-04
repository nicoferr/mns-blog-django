from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from .models import Profile

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    print(f'Bienvenue à notre nouvel utilisateur : { instance.username }')
    if created :
        profile = Profile(user=instance)
        profile.save()