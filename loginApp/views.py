from django.shortcuts import render

# Create your views here.

def login_page(request):
    context = {}
    return render(request, 'loginApp/login.html', context)