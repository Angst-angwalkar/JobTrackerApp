from rest_framework.decorators import api_view, authentication_classes
from rest_framework.response import Response
from rest_framework.views import APIView
from ..serializers.user_serializer import LoginInputSerializer, LoginOutputSerializer
from ..services.auth_services import AuthServices



class LoginView(APIView):

    service_class = AuthServices()


    def post(self, request):
        return Response(self.service_class.login(request))