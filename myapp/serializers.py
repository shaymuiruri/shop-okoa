from rest_framework import serializers
from .models import User  # Import your model here

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'