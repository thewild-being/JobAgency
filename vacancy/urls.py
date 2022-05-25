from django.urls import path
from . import views

urlpatterns = [
    path('', views.vacancy_view),
    path('/new', views.vacancy_create)  # new vacancies can be created at localhost:8000/vacancies/new -> CRUD
]
