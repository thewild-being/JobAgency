from django.shortcuts import render
from django.http import HttpResponse
from .models import Resume
from django.forms import ModelForm

# Create your views here.

resume = Resume.objects.all()


# Create your views here.
# very simple and unique view --> going for a fx based view here
# the fx return the template here
def resume_view(request):
    return render(request, 'resume.html', context={'resume': resume})


# The main requirement is that the handlers should receive only one POST parameter: description.
# That's enough to create a new item.
def resume_create(request):
    return render(request, 'resume_create.html', context={'resume': resume})
    # returns the form for creating a resume --> POST http method


# __________this is an alternative way to quickly create forms using the ready-to-use django forms
class ResumeForm(ModelForm):
    class Meta:
        model = Resume
        fields = "__all__"


form = ResumeForm()


def create_resume(request):
    return render(request, form)
