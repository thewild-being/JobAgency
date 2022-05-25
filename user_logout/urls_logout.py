from django.urls import path
from . import views

urlpatterns = [
    path('', views.Logout.as_view()),
]
