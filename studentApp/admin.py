from django.contrib import admin
from .models import *

#Register your models here.

student_models = [Building, Classroom, Department, Course, Instructor, 
                InstField, InstDegree, InstPublication, 
                Timeslot, Section, InstTeaches, StudentCourse, 
                Prereq, Route, Driver]

for student_model in student_models: 
    try: 
        admin.site.register(student_model)
    except: 
        continue

