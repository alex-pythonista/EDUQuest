from django.shortcuts import render

from django.contrib.auth.models import User
from loginApp.models import *
from .models import *

# Create your views here.

def forum(request):

    questions = Question.objects.all()

    context = {'questions': questions}
    template_name = 'forumApp/questions.html'
    return render(request, template_name, context)