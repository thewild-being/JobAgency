from django.urls import path
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    path('', views.Signup.as_view())
    # path('signup/', RedirectView.as_view(url='/signup'))
]
