from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import DietPlan, ExercisePlan
from .serializers import DietPlanSerializer, ExercisePlanSerializer

# Create your views here.

class DietPlanViewSet(viewsets.ModelViewSet):
    queryset = DietPlan.objects.all()
    serializer_class = DietPlanSerializer
    permission_classes = [permissions.IsAuthenticated]

class ExercisePlanViewSet(viewsets.ModelViewSet):
    queryset = ExercisePlan.objects.all()
    serializer_class = ExercisePlanSerializer
    permission_classes = [permissions.IsAuthenticated]
