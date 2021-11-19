from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def dev_page(request):
    context = {}
    template_name = 'dev.html'
    return render(request, template_name, context)

def profile_view(request, *args, **kwargs): 
    context = {}
    template_name = 'studentApp/profile.html' 
    return render(request,template_name, context)

def catalog_view(request,*args, **kwargs):
    context = {}
    template_name = 'more_about_courses.html'
    # return HttpResponse("<h1>Course Catalog</h1>") 
    return render(request,template_name, context)

def routine_view(request,*args, **kwargs): 
    context = {}
    template_name = 'routineApp/routine.html'
    # return HttpResponse("<h1>Personalized Routine</h1>") 
    return render(request,template_name, context)

def schedule_checker_view(request,*args, **kwargs): 
    context = {}
    template_name = 'schedule_checker.html'
    return HttpResponse("<h1>Schedule Checker</h1>") 

def progress_view(request,*args, **kwargs): 
    context = {}
    template_name = 'progress.html'
    # return HttpResponse("<h1>Course Progress</h1>") 
    return render(request,template_name, context)

def instructor_view(request,*args, **kwargs): 
    context = {}
    template_name = 'instructor.html'
    #return HttpResponse("<h1>Instructor Profile</h1>") 
    return render(request,template_name, context)

def finances_view(request,*args, **kwargs): 
    context = {}
    template_name = 'finances.html'
    return HttpResponse("<h1>Finances</h1>")
    #return render(request,template_name, context)
        
def forum_view(request,*args, **kwargs): 
    context = {}
    template_name = 'forum.html'
    return HttpResponse("<h1>Discussion Forum</h1>") 
    #return render(request,template_name, context)

def bus_schedule_view(request,*args, **kwargs): 
    context = {}
    template_name = 'bus_schedule.html'
    # return HttpResponse("<h1>Bus Schedule</h1>") 
    return render(request,template_name, context)