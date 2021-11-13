from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def dev_page(request):
    context = {}
    template_name = 'dev.html'
    return render(request, template_name, context)

def home_view(request, *args, **kwargs): 
    return HttpResponse("<h1>Landing Page</h1>")
    # return render(request, "home.html", {})

def profile_view(request, *args, **kwargs): 
    return HttpResponse("<h1>Student Profile</h1>") 
    #return render(request, "profile.html", {})

def catalog_view(request,*args, **kwargs): 
    return HttpResponse("<h1>Course Catalog</h1>") 

def routine_view(request,*args, **kwargs): 
    return HttpResponse("<h1>Personalized Routine</h1>") 
    #return render(request, "routine.html", {})

def schedule_checker_view(request,*args, **kwargs): 
    return HttpResponse("<h1>Schedule Checker</h1>") 

def progress_view(request,*args, **kwargs): 
    return HttpResponse("<h1>Course Progress</h1>") 

def instructor_view(request,*args, **kwargs): 
    return HttpResponse("<h1>Instructor Profile</h1>") 

def finances_view(request,*args, **kwargs): 
    return HttpResponse("<h1>Finances</h1>")
    
def forum_view(request,*args, **kwargs): 
    return HttpResponse("<h1>Discussion Forum</h1>") 

def bus_schedule_view(request,*args, **kwargs): 
    return HttpResponse("<h1>Bus Schedule</h1>") 
    #return render(request, "bus_schedule.html", {})