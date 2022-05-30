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


# __________this is a way to quickly create forms using the ready-to-use django forms
class ResumeForm(ModelForm):
    class Meta:
        model = Resume
        fields = "__all__"


form = ResumeForm()


def create_resume(request):
    return render(request, form)
