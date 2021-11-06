from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse('Home page')


def login_page(request):
    context = {}
    template_name = 'loginApp/login.html'
    return render(request, template_name, context)

def register(request):
    context = {}
    template_name = 'loginApp/register.html'
    return render(request, template_name, context)