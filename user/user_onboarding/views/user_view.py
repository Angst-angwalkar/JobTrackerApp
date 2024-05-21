from rest_framework.views import APIView
from rest_framework.decorators import api_view

from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from ..models.user_model import User
from ..models.user_manager import UserManager
from ..services.user_services import UserServices


class UserCreateView(APIView):
    """
    View for User Creation and basic user apis
    Handles CRUD Operations for User.
    """

    service_class = UserServices()

    def get(self, request):
        return Response(self.service_class._get_user(request.query_params))


    def post(self, request):        
        return Response(self.service_class._create_user(request.data))
    

    def put(self, request):        
        return Response(self.service_class._update_user(request.data))
