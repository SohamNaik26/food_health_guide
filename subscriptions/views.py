from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Subscription
from .serializers import SubscriptionSerializer

# Create your views here.

class SubscriptionViewSet(viewsets.ModelViewSet):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    permission_classes = [permissions.IsAuthenticated]
