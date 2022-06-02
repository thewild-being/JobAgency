from django.urls import path
from . import views

urlpatterns = [
    path('', views.resume_view),
    path('new', views.resume_create)  # new resume can be created at localhost:8000/resume/new -> CRUD
]
