from django.contrib import admin
from .models import DietPlan, ExercisePlan

@admin.register(DietPlan)
class DietPlanAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'calories_per_day', 'created_at')

@admin.register(ExercisePlan)
class ExercisePlanAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'duration_per_day', 'created_at')
