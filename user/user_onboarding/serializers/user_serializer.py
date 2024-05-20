from rest_framework import serializers
from ..models.user_model import User
import datetime
import hashlib



class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"


class UserCreateSerializer(UserSerializer):

    class Meta:
        model = User
        fields = "__all__"


    def validate_user_name(self, value) -> str:
        if len(value) < 5 or len(value) > 15:
            raise serializers.ValidationError("Username cannot has to be between 8 to 15 characters!")
        return value
    


class UserResponseSerializer(UserSerializer):

    class Meta:
        model = User
        exclude = ['password']