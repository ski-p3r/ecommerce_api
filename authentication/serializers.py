from rest_framework import serializers
from .models import User

class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    username = serializers.CharField(read_only=True)
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password')

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)