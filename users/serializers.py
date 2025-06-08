from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'age', 'gender', 'height', 'weight', 'health_conditions', 'activity_level', 'dietary_preferences'] 