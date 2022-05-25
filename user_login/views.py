from django.shortcuts import render
from django.contrib.auth.views import LoginView


# or django.contrib.auth.forms.AuthenticationForm as login handler


# we inherit the User class in the user_login app --> better to use class based views than fx based views
class Login(LoginView):
    redirect_authenticated_user = True  # if login successful, redirect to menu page
    success_url = "/"
    template_name = 'login.html'

# per assicurarti che il log in sia efficace devi guardare nel db
