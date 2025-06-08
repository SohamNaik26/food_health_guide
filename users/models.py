from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
    gender = models.CharField(max_length=10, null=True, blank=True)
    height = models.FloatField(null=True, blank=True, help_text='Height in cm')
    weight = models.FloatField(null=True, blank=True, help_text='Weight in kg')
    health_conditions = models.TextField(null=True, blank=True)
    activity_level = models.CharField(max_length=50, null=True, blank=True)
    dietary_preferences = models.TextField(null=True, blank=True)
