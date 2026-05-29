from User.models import CustomUser
from rest_framework import serializers


class RegisterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields="__all__"
    def create(self, validated_data):
        user= CustomUser(
            phone_number=validated_data['phone_number'],
            username=validated_data['username'],
        )
        return user