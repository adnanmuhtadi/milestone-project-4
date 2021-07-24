from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from django_countries.fields import CountryField


class UserProfile(models.Model):
    """
    A user profile model for to store delivery information and order history,
    with the user having a one to one relationship which specifics one user 
    can only have one profile
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_phone_number = models.CharField(max_length=20, null=True, blank=True)
    default_address_line1 = models.CharField(max_length=80, null=True, blank=True)
    default_address_line2 = models.CharField(max_length=80, null=True, blank=True)
    default_town_or_city = models.CharField(max_length=40, null=True, blank=True)
    default_county_state = models.CharField(max_length=80, null=True, blank=True)
    default_postcode = models.CharField(max_length=20, null=True, blank=True)
    default_country = CountryField(blank_label='Country *', null=True, blank=True)

    # Retuning the username
    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_update_user_profile(sender, instance, created, **kwargs):
    """
    Create a profile if user has not got one or update the user profile if the user has a profile 
    """
    if created:
        UserProfile.objects.create(user=instance)
    # For existing users, it will just save the profile
    instance.userprofile.save()