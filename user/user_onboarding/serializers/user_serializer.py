from rest_framework import serializers
from ..models.user_model import UserModel
import datetime
import uuid


class UserSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField()
    user_name = serializers.CharField()
    email = serializers.EmailField()
    creation_on = serializers.DateTimeField()
    deactivation_on = serializers.DateTimeField()
    updated_on = serializers.DateTimeField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()


    class Meta:
        model = UserModel


    def validate_user_name(self, value) -> str:
        if len(value) < 5 or len(value) > 15:
            raise serializers.ValidationError("Username cannot has to be between 8 to 15 characters!")
        return value
    


    def create(self, validated_data):
        return UserModel.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.user_name = validated_data.get('user_name', instance.user_name)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.updated_on = validated_data.get('updated_on', datetime.datetime.now())
        instance.mobile = validated_data.get('mobile', instance.mobile)
        instance.password = validated_data.get('password', instance.password)
        instance.save()
        return instance
    

    