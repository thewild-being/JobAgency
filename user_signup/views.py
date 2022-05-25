from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView


# we inherit the views from CreateView and the form from UserCreationForm
# --> better to use class based views than fx based views

class Signup(CreateView):
    form_class = UserCreationForm
    success_url = '/login/'  # this the url where the user_login is redirected once signed up
    template_name = 'signup.html'
    # any methods here? --> where are these saved tho? --> these are saved automatically to the default app models
    # no need to specify
