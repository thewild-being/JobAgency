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


# __________this is a way to quickly create forms using the ready-to-use django forms
class VacancyForm(ModelForm):
    class Meta:
        model = Vacancy
        fields = "__all__"


form = VacancyForm()


def create_vacancy(request):
    return render(request, form)
