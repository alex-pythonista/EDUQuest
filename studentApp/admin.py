from django.contrib import admin
from .models import *

# Register your models here.
student_models = [classroom, department, course, instructor, inst_field, inst_degree, inst_publication,
                timeslot, section]

for student_model in student_models: 
    admin.site.register(student_model)


