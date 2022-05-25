from django.shortcuts import render
from django.http import HttpResponse
from .models import Vacancy

vacancy = Vacancy.objects.all()  # here we put the model in a variable to connect w the template


# Create your views here.
# very simple and unique view --> going for a fx based view here
# the fx returns the template here

def vacancy_view(request):
    return render(request, 'vacancy.html', context={'vacancy': vacancy})
    # poi per aggiornare vacancies, serve una nuova fx tipo questa per aggiornare un child block per la form


# The main requirement is that the handlers should receive only one POST parameter: description.
# That's enough to create a new item.
def vacancy_create(request):  # CRUD HERE
    return render(request, 'vacancy_create.html')  # returns the form for creating a resume --> POST http method
