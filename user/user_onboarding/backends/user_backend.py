from django.conf import settings
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model
from django.db.models import Q
from django.core.exceptions import ValidationError
from django.db.models.functions import Lower
from django.db.models import CharField, TextField, EmailField
from django.contrib.auth.hashers import make_password, check_password
from bcrypt import checkpw

TextField.register_lookup(Lower)
EmailField.register_lookup(Lower)


USER = get_user_model()



# def filter_active(self):
#         return self.get_queryset().filter(expression)


class UserBackend(BaseBackend):
    """
    """

    def authenticate(self, request = None, username: str = None, password: str = None, email: str = None, mobile: str = None):

        if username is None or username == "":
            return None
        if password is None or password == "":
            return None
        
        # expression = (
        #     Q(is_active={"is_active": True}) | Q(deactivated_on__isnull=True)
        # )

        username = username.lower().strip()
        if USER.objects.filter(username__lower = username).exists():
            user = USER.objects.filter(username__lower = username).first()
            print("HERE RIGHT NOW")
            print(password)
            print(user.password)
            # if check_password(password, user.password):
                
            if user.check_password(password):
                return user
            else:
                raise ValidationError("Username and password don't match.")
            
        
        elif USER.objects.filter(email__lower = username).exists():
            user = USER.objects.filter(email__lower = username).first()#.filter(expression).first()
            # if check_password(password, user.password):
            if user.check_password(password):
                return user
            else:
                raise ValidationError("Email and password don't match.")
        
        elif USER.objects.filter(mobile__lower = username).exists():
            user = USER.objects.filter(mobile__iexact = username).first()#.filter(expression).first()
            print(user.get_username())
            # if check_password(password, user.password):
            if user.check_password(password):
                return user
            else:
                raise ValidationError("Mobile and password don't match.")



def default_user_authentication_rule(user):
    return user is not None and user.is_active