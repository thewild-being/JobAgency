from django.shortcuts import render
from django.http import HttpResponse  # solo per vedere se funziona il link
from django.contrib.auth.models import User
from . import home


# Create your views here.

def hello(request):
    return HttpResponse(
        "<h1>🚧 form in construction 👷🏽‍🚧</h1>"
    )


# when in doubt su come strutturare un piece of code: pensa ai design styles
def personal_profile_view(request):
    auth = request.user.is_authenticated  # or use a built-decorator to check for log in
    if auth:
        return render(request, "home.html")
    else:
        return HttpResponse(
            "<h2>To access your profile you need to <a href='signup/'>Sign up</a> and <a href='login/'>Log in</a></h2>"
        )

