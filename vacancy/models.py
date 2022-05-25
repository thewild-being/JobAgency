import django as django
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


# Create your models here.
class Vacancy(models.Model):
    description = models.TextField(max_length=1024, null=True)
    # author field is a foreign key linked to the django.contrib.auth.models.User model.
    # author = models.ForeignKey(User, on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
