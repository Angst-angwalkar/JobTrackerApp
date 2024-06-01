from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from .user_manager import UserManager, UserManagerQuery
from django.db.models.functions import Lower
from django.utils import timezone
import datetime
import uuid





class Metadata(models.Model):
    type = models.TextField(default='')
    user_id = models.TextField()
    size = models.IntegerField(default=0)
    lastModifiedDate = models.DateTimeField(default=timezone.now())
    mimeType = models.TextField(default='')
    tempFilename = models.TextField(default='')
    orignalFilename = models.TextField(default='')

    class Meta:
        abstract = False
        ordering = ['-lastModifiedDate']

class ProfilePhoto(models.Model):
    _id = models.AutoField(primary_key=True, null=False)
    profile_url = models.TextField()
    metadata = models.ForeignKey(Metadata, on_delete=models.CASCADE)

    class Meta:
        abstract = False



class UserModel(AbstractBaseUser):
    _id = models.AutoField(primary_key=True, null=False)
    user_id = models.TextField(default=uuid.uuid4().hex[:12])
    username = models.TextField(unique=False)
    first_name = models.TextField()
    last_name = models.TextField()
    email = models.EmailField(max_length=254, unique=True)
    mobile = models.TextField()
    is_active = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    deactivated_on = models.DateTimeField(null=True)
    updated_on = models.DateTimeField(null=True)
    profile_photo = models.ForeignKey(ProfilePhoto, on_delete=models.CASCADE, null=True)
    password = models.TextField()

    objects = UserManager()

    USERNAME_FIELD = 'username'

    query = UserManagerQuery()

    class Meta:
        abstract = False






class User(UserModel):

    class Meta:
        verbose_name = ("user")
        abstract = False
        db_table = "user_model"
