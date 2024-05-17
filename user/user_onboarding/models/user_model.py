from django.db import models
import datetime
import uuid


class UserModel(models.Model):

    user_id = models.IntegerField(unique=True, primary_key=True, default=uuid.uuid4()[3:9])
    user_name = models.TextField()
    first_name = models.TextField()
    last_name = models.TextField()
    email = models.TextField()
    mobile = models.TextField()
    is_active = models.BooleanField(default=False)
    creation_on = models.DateTimeField(default=datetime.datetime.now())
    deactivation_on = models.DateTimeField(null=True)
    updated_on = models.DateTimeField(null=True)
    password = models.TextField()



    class Meta:
        verbose_name = 'UserModel'
        fields = ["user_id", "user_name", "first_name", "last_name", "email", "mobile", "is_active", "creation_on", "deactivation_on"]