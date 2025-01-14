from rest_framework import serializers
from ..models.user_model import User, Metadata, ProfilePhoto
import datetime





class MetadataSerializer(serializers.Serializer):
    type = serializers.CharField()
    user_id = serializers.CharField()
    size = serializers.IntegerField()
    lastModifiedDate = serializers.DateTimeField()
    mimeType = serializers.CharField()
    tempFilename = serializers.CharField()
    orignalFilename = serializers.CharField()

    class Meta:
        model = Metadata
        fields = '__all__'


class ProfilePictureSerializer(serializers.Serializer):
    _id = serializers.CharField()
    profile_url = serializers.CharField(required=False)

    class Meta:
        model = ProfilePhoto
        fields = '__all__'



class UserSerializer(serializers.ModelSerializer):
    profile_photo = serializers.ListSerializer(
        child = ProfilePictureSerializer(required = False),
        required = False, read_only = True
    )
    user_id = serializers.CharField(required=False)
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)
    username = serializers.CharField(required=False)
    email = serializers.EmailField(required=False)
    mobile = serializers.CharField(required=False)
    is_active = serializers.BooleanField(required=False)
    class Meta:
        model = User
        fields = "__all__"




class UserCreateSerializer(UserSerializer):

    class Meta:
        model = User
        fields = "__all__"


    def validate_user_name(self, value) -> str:
        if len(value) < 5 or len(value) > 20:
            raise serializers.ValidationError("Username cannot has to be between 8 to 15 characters!")
        return value
    


class UserResponseSerializer(UserSerializer):

    class Meta:
        model = User
        exclude = ['password']




class LoginInputSerializer(serializers.Serializer):

    username = serializers.CharField(required=False)
    email = serializers.CharField(required=False)
    mobile = serializers.CharField(required=False)
    password = serializers.CharField(required=True)

    def validate(self, attrs):
        if attrs.get("username") is None:
            if attrs.get("email") is None:
                if attrs.get("mobile") is None:
                    raise serializers.ValidationError("Please provide either username, email or mobile!")
        return attrs
    

class LoginOutputSerializer(UserSerializer):
    class Meta:
        model = User
        fields = ['_id','profile_photo','last_login','user_id','username', 
        'email','mobile','is_active']