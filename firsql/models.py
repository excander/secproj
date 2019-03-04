from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    login = models.CharField(max_length=200)
    money_amount = models.IntegerField(default=0)
    card_number = models.CharField(max_length=16)
    status = models.BooleanField(default=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        db_table = "users"

class User_data(models.Model):
    user = models.OneToOneField(Profile, on_delete=models.CASCADE, primary_key = True)
    pwd = models.CharField(max_length=200)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


from django.contrib.auth.validators import ASCIIUsernameValidator

class CustomUser(User):
    username_validator = ASCIIUsernameValidator()

    class Meta:
        proxy = True  # If no new field is added.