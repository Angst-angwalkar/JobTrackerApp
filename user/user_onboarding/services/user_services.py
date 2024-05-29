from user_onboarding.serializers.user_serializer import UserCreateSerializer, UserResponseSerializer
from rest_framework.parsers import JSONParser
from user_onboarding.models.user_model import User




class UserServices:


    parser_classes = [JSONParser]
    create_serializer_class = UserCreateSerializer
    response_serializer_class = UserResponseSerializer


    def _get_user(self, request):
        """
        Function to fetch a single user based on the passed parameter.
        The parameters can be one of the following:
        1. user_id
        2. email
        3. username
        4. mobile

        Any other parameter cannot be excepted and the function will return status 401.
        If user details are not found, return status 404. 
        """

        response = {}
        user_id = request.get("user_id", None)
        username = request.get("username", None)
        email = request.get("email", None)
        mobile = request.get("mobile", None)

        param_dict = None
        if user_id:
            param_dict = {"user_id": user_id}
        elif username:            
            param_dict = {"username": username}
        elif email:
            param_dict = {"email": email}
        elif mobile:
            param_dict = {"mobile": mobile}
        

        if not param_dict:
            response["data"] = []
            response["message"] = "No valid paramter found for user."
            response["status_code"] = 401
            return response

        user = User.objects._get_user_details(param_dict)

        if user is not None and user != {}:
            serializer_class = self.response_serializer_class(user)
            response["data"] = serializer_class.data
            response["message"] = "OK"
            response["status_code"] = 200
        else:
            response["data"] = None
            response["message"] = f"User with {next(iter(param_dict.keys()))}: {next(iter(param_dict.values()))} does not exist!"
            response["status_code"] = 404
        return response

    


    def _create_user(self, request):
        response = {}

        user = self.create_serializer_class(data = request)

        if user.is_valid():
            try:
                user = user.save()
            except Exception as err:
                response["data"] = []
                response["message"] = err.args[0]
                response["status_code"] = 400
                return response
            
            serializer = self.response_serializer_class(user)
            response["data"] = serializer.data
            response["message"] = "User Created Successfully"
            response["status_code"] = 200
        else:
            response["message"] = "User Creation Failed"
            response["data"] = user.errors
            response["status_code"] = 400
        
        return response
    


    def _update_user(self, request):
        pass





    def _delete_user(self, request):
        pass