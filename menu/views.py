from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
# very simple and unique view --> going for a fx based view here, w/o templates

def welcoming(request):
    return HttpResponse(
        '''<h2>Welcome to HyperJob!</h2>
        <div></div>
        <a href="/login">Login</a>
        <div></div>
        <a href="/logout">Logout</a>
        <div></div>
        <a href="/signup">Sign Up</a>
        <div></div>
        <a href="/vacancies">Vacancies</a>
        <div></div>
        <a href="/resumes">Resumes</a>
        <div></div>
        <a href="/home">Personal Profile</a>'''
        )

