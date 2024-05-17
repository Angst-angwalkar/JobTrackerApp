from rest_framework.views import APIView
from rest_framework.decorators import api_view
from user_onboarding.models.user_model import UserModel
from user_onboarding.serializers.user_serializer import UserCreateSerializer
from rest_framework.parsers import JSONParser


class UserCreateView(APIView):
    """
    View for User Creation and basic user apis
    """

    parser_classes = [JSONParser]
    serializer_class = UserCreateSerializer



    def post(self, request):

        response = {}

        user = self.serializer_class(data = request.data)

        if user.is_valid():
            user.save()
            response["data"] = user.data
            response["message"] = "User Created Successfully"
            response["status_code"] = 200
        else:
            response["message"] = "User Creation Failed"
            response["data"] = user.errors
            response["status_code"] = 400
        
        return response
