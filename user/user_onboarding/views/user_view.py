from rest_framework.views import APIView
from rest_framework.decorators import api_view
from user_onboarding.serializers.user_serializer import UserCreateSerializer, UserResponseSerializer
from rest_framework.parsers import JSONParser
from rest_framework.response import Response


class UserCreateView(APIView):
    """
    View for User Creation and basic user apis
    """

    parser_classes = [JSONParser]
    serializer_class = UserCreateSerializer
    response_serializer_class = UserResponseSerializer



    def post(self, request):

        response = {}

        user = self.serializer_class(data = request.data)

        if user.is_valid():
            user = user.save()
            serializer = self.response_serializer_class(user)
            response["data"] = serializer.data
            response["message"] = "User Created Successfully"
            response["status_code"] = 200
        else:
            response["message"] = "User Creation Failed"
            response["data"] = user.errors
            response["status_code"] = 400
        
        return Response(response)
