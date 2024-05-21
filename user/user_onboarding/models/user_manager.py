from django.contrib.auth.models import BaseUserManager
from django.db.models.manager import BaseManager
from django.core.exceptions import ValidationError
from django.db import models
import hashlib, uuid

__all__ = ["UserManager"]


class UserManager(BaseUserManager, BaseManager):
    """
    Model manager utility for User Model.
    """

    def create(self, username: str, first_name: str, last_name: str,
               email: str, mobile: str, **extra_fields) -> dict:
        if not username or username == "": 
            raise ValidationError("username cannot be empty.")
        if (not email or email == "") and (not mobile or mobile == ""):
            raise ValidationError("Either mobile or email is needed.")

        username_check = self.get_queryset().filter(username=username)
        if username_check.exists():
            raise ValidationError("User name already exists. Please choose a different username")

        email_check = self.get_queryset().filter(email=email)
        if email_check.exists():
            raise ValidationError("This Email is already registered. Please login into the existing account or use a different account!")
        
        phone_check = self.get_queryset().filter(mobile=mobile)

        if phone_check.exists():
            raise ValidationError("This Mobile is already registered. Please login into the existing account or use a different account!.")
        

        email = self.normalize_email(email=email)

        password = self._pass_encryption(extra_fields.get('password'))


        user = self.model(
            email = email,
            password = password,
            username = username,
            first_name = first_name,
            last_name = last_name,
            mobile = mobile,
            **extra_fields
        )

        user.save(using=self._db)
        return user


    def _pass_encryption(self, org_pass) -> str:
        byte_pass = org_pass.encode('utf-8')
        hash_pass = hashlib.sha256(byte_pass)
        return hash_pass.hexdigest()
    


    def _get_user_details(self, param_dict: dict = None) -> dict:
        print(param_dict)
        if not param_dict:
            return {}
        return self.get_queryset().filter(**param_dict).first()


class UserManagerQuery(models.Manager):
    def get_queryset(self):
        return super()
