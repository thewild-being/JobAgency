from django.shortcuts import render
from django.contrib.auth.views import LogoutView


# Create your views here.
class Logout(LogoutView):
    pass  # this one does not need any info, we just inherit the LogoutView class
