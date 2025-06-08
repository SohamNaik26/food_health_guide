from django.db import models
from django.conf import settings

# Create your models here.

class DietPlan(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='diet_plans')
    name = models.CharField(max_length=100)
    description = models.TextField()
    calories_per_day = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.name}"

class ExercisePlan(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='exercise_plans')
    name = models.CharField(max_length=100)
    description = models.TextField()
    duration_per_day = models.PositiveIntegerField(help_text='Duration in minutes')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.name}"
