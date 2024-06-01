from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated

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




    def post(self, request):        
        response = self.service_class._create_user(request.data)
        return Response(response, status=response["status_code"])
    



class UserView(APIView):

    service_class = UserServices()
    permission_classes = [IsAuthenticated]

    def get(self, request):
        response = self.service_class._get_user(request.query_params)
        return Response(response, status=response["status_code"])
    
    def put(self, request):     
        response = self.service_class._update_user(request.data)   
        return Response(response, status=response["status_code"])