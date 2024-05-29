from ..serializers.user_serializer import (
    LoginInputSerializer, 
    LoginOutputSerializer
)
from ..backends.user_backend import UserBackend
from rest_framework_simplejwt.tokens import RefreshToken
from django.core.exceptions import ValidationError



class AuthServices():

    input_serializer_class = LoginInputSerializer
    output_serializer_class = LoginOutputSerializer
    

    def login(self, request):
       
        request_data = self.input_serializer_class(data=request.data)
        response = {}        
        if not request_data.is_valid():
            response["data"] = request_data.errors
            response["message"] = request_data.error_messages
            response["status"] = 252
            return response
        try:
            auth = UserBackend()
            user = auth.authenticate(**request_data.validated_data)
            if user is not None:
                token = RefreshToken.for_user(user)

                token_data = {
                    'refresh': str(token),
                    'access': str(token.access_token),
                }

                serializer = self.output_serializer_class(user)
                user_data = serializer.data
                user_data.update(token_data)

                response["data"] = user_data
                response["message"] = "Logged in successfully"
                response["status"] = 200
                return response
            else:
                response["data"] = []
                response["message"] = "User not found!"
                response["status"] = 404
                return response
            
        except ValidationError as ex:
            response["data"] = []
            response["message"] = ex
            response["status"] = 409
            return response