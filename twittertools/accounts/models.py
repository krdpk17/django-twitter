from django.db import models
from django.contrib.auth.models import User
#from django.dispatch import receiver
#from django.db.models.signals import post_save

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=50, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    twitter_consumer_key = models.CharField(max_length=300, blank=True)
    twitter_consumer_secret = models.CharField(max_length=300, blank=True)
    twitter_user_key = models.CharField(max_length=300, blank=True)
    twitter_user_secret = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return self.user.username 
    

# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)

# @receiver(post_save, sender=User, dispatch_uid='save_new_user_profile')
# def save_profile(sender, instance, created, **kwargs):
#     user = instance
#     if created:
#         profile = Profile(user=user)
#         profile.save()
# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, created, **kwargs):
#     instance.profile.save()