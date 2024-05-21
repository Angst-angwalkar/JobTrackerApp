from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from .user_manager import UserManager, UserManagerQuery
import datetime
import uuid


class UserModel(AbstractBaseUser):
    _id = models.AutoField(primary_key=True, null=False)
    user_id = models.TextField(default=uuid.uuid4().hex[:12])
    username = models.TextField()
    first_name = models.TextField()
    last_name = models.TextField()
    email = models.TextField()
    mobile = models.TextField()
    is_active = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    deactivated_on = models.DateTimeField(null=True)
    updated_on = models.DateTimeField(null=True)
    password = models.TextField()

    objects = UserManager()

    query = UserManagerQuery()

    class Meta:
        abstract = False


class User(UserModel):

    class Meta:
        verbose_name = ("user")
        abstract = False
        db_table = "user_model"

    