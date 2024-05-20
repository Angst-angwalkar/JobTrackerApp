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

    def create(self, user_name: str, first_name: str, last_name: str,
               email: str, mobile: str, **extra_fields) -> dict:
        if not user_name or user_name == "": 
            raise ValidationError("user_name cannot be empty.")
        if (not email or email == "") and (not mobile or mobile == ""):
            raise ValidationError("Either mobile or email is needed.")
        

        email_check = self.get_queryset().filter(email=email)
        if email_check.exists():
            raise ValidationError("This Email is already registered. Please login into the existing account or use a different account!")
        
        phone_check = self.get_queryset().filter(mobile=mobile)
        print(phone_check)
        if phone_check.exists():
            raise ValidationError("This Mobile is already registered. Please login into the existing account or use a different account!.")
        
        user_name_check = self.get_queryset().filter(user_name=user_name)
        if user_name_check.exists():
            raise ValidationError("User name already exists. Please choose a different username")
        

        email = self.normalize_email(email=email)

        password = self._pass_encryption(extra_fields.get('password'))


        print(password)

        user = self.model(
            email = email,
            password = password,
            user_name = user_name,
            first_name = first_name,
            mobile = mobile,
            is_active = False
        )

        user.save(using=self._db)
        return user


    def _pass_encryption(self, org_pass) -> str:
        byte_pass = org_pass.encode('utf-8')
        hash_pass = hashlib.sha256(byte_pass)
        return hash_pass.hexdigest()



class UserManagerQuery(models.Manager):
    def get_queryset(self):
        return super()
