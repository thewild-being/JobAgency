import django as django
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


# Create your models here.
class Resume(models.Model):
    description = models.TextField(max_length=1024, null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # _________________MY MISTAKE
    # author = models.ForeignKey(django.contrib.auth.models.User)
    # author field is a foreign key linked to the django.contrib.auth.models.User model.
    """ to reference the ForeignKey(django.contrib.auth.User) you should import by writing "from django.conf import 
    settings" and then write "ForeignKey(settings.AUTH_USER_MODEL, ...)" for author. """

