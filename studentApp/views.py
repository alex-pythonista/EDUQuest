from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django import forms 
from loginApp.models import Student
from .models import *
#Create your views here.

class Discount(forms.Form):
    checkbox1 = forms.BooleanField(required=False)
    checkbox2 = forms.BooleanField(required=False)
    checkbox3 = forms.BooleanField(required=False)

def dev_page(request):
    context = {}
    template_name = 'dev.html'
    return render(request, template_name, context)


@login_required
def profile_view(request):
    studentProfile = Student.objects.get(user=request.user)
    courseEnrolled = StudentCourse.objects.filter(student_id=studentProfile.student_id, status='E')
    courseInfo = Course.objects.all()
    context = {'student': studentProfile, 'enrolled': courseEnrolled, 'courses': courseInfo}
    template_name = 'studentApp/profile.html' 
    return render(request, template_name, context)

@login_required
def more_about_courses_view(request,*args, **kwargs):
    studentProfile = Student.objects.get(user=request.user)
    courseCompleted = StudentCourse.objects.filter(student_id=studentProfile.student_id, status='C')
    courseNotComplete = StudentCourse.objects.filter(student_id=studentProfile.student_id, status='N')
    context = {'student': studentProfile, 'completed': courseCompleted, 'notcompleted': courseNotComplete}
    template_name = 'more_about_courses.html'
    # return HttpResponse("<h1>Course Catalog</h1>") 
    return render(request,template_name, context)

@login_required
def routine_view(request,*args, **kwargs): 
    context = {}
    studentProfile = Student.objects.get(user=request.user) 
    if studentProfile.fullname == 'Mostafijur Rahman': 
        template_name = 'routineApp/routine_2.html'
    elif studentProfile.fullname == 'Shanjeev Kumar Roy': 
        template_name = 'routineApp/routine_3.html'
    else: 
        template_name = 'routineApp/routine.html'
    #return HttpResponse("<h1>Personalized Routine</h1>") 
    return render(request,template_name, context)

@login_required
def schedule_checker_view(request,*args, **kwargs): 
    context = {}
    template_name = 'schedule_checker.html'
    return render(request,template_name, context)

@login_required
def progress_view(request,*args, **kwargs): 
    context = {}
    template_name = 'progress.html'
    # return HttpResponse("<h1>Course Progress</h1>") 
    return render(request,template_name, context)

@login_required
def instructor_view(request,*args, **kwargs): 
    instructors_all = Instructor.objects.all()
    context = {'instructors': instructors_all}
    template_name = 'instructor.html'
    #return HttpResponse("<h1>Instructor Profile</h1>") 
    return render(request,template_name, context)

@login_required
def finances_view(request,*args, **kwargs): 
    context = {}
    studentProfile = Student.objects.get(user=request.user)
    context['student'] = studentProfile
    
    form = Discount(request.POST or None)
    if request.method == "POST": 

        if request.POST.get("checkbox1"): 
            multiplier = 0.41
            context['BOT'] = multiplier
        else: 
            multiplier = 0
            context['BOT'] = multiplier

        if request.POST.get("checkbox2"): 
            disc = 5000
            context['Zarin'] = disc
        else: 
            disc = 0
            context['Zarin'] = disc

        if request.POST.get("checkbox3"):
            multiplier = 0.1
            context['Early'] = multiplier
        else: 
            multiplier = 0
            context['Early'] = multiplier

        if request.POST.get(None): 
            context['BOT'] = 0
            context['Zarin'] = 0
            context['Early'] = 0
        
    template_name = 'finances.html'
    #return HttpResponse("<h1>Finances</h1>")
    return render(request,template_name, context)
        
        
@login_required       
def bus_schedule_view(request,*args, **kwargs):
    busRoute = Route.objects.all()
    driverRoute = Driver.objects.all()
    context = {'route': busRoute, 'driver': driverRoute} 
    template_name = 'bus_schedule.html'
    return render(request,template_name, context)


@login_required
def course_catalog_view(request,*args, **kwargs):
    context = {}
    template_name = 'course_catalog.html'
    #return HttpResponse("<h1>Course Catalog</h1>") 
    return render(request,template_name, context)