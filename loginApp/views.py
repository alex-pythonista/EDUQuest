from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from .models import Student

# Create your views here.

@login_required
def home(request):
    return HttpResponse('Home page')


def register(request):

    registered = False

    if request.method == 'POST':
        fullname = request.POST['fullname']
        username = request.POST['username']
        department = request.POST['department']
        semester = request.POST['semester']
        student_id = request.POST['student_id']
        address = request.POST['address']
        email = request.POST['email']
        password = request.POST['password']
        
        user_obj = User(username=username, email=email)
        user_obj.set_password(password)
        user_obj.save()

        student_obj = Student(
            user = user_obj,
            fullname = fullname,
            department = department,
            semester = semester,
            student_id = student_id,
            address = address,
        )
        student_obj.save()

        return HttpResponseRedirect(reverse('loginApp:login'))

    else:    
        context = {}
        template_name = 'loginApp/register.html'
        return render(request, template_name, context)

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('loginApp:home'))
             
        else:
            return HttpResponse("invalid login information!")

    else:
        context = {}
        template_name = 'loginApp/login.html'
        return render(request, template_name, context)


@login_required 
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('loginApp:login'))