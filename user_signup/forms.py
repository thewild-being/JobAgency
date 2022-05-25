# from django.contrib.auth.models import User
# from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from django.views.generic import CreateView
# from django.contrib.auth.views import LoginView, LogoutView

# ⛩ not sure if this file is useful for hyperskill
# this py file is used to edit the models in the pre-defined apps in django.
# In pratica andimo a scrivere qua manualmente i forms da poi importare nelle views con
# from . import forms e poi usare forms.SignupForm al posto di usare le pre-defined forms


# User.objects.create_user(  # is this the right way to do it?
#     username='usual_user', email='user_login@example.com', password='NotSecRetAtAll'
# )
#
#
# class SignupForm(User.objects.create_user()):
#     email = forms.EmailField()
#
#     class Meta:  # smanettaci qua
#         model = User
#         fields = ["username", "email", "password"]  # specify the order in which the fields show up
