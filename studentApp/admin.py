from django.contrib import admin
from .models import *

#Register your models here.

# student_models = [Building, Classroom, Department, Course, Instructor, 
#                 InstField, InstDegree, InstPublication, 
#                 Timeslot, Section, InstTeaches, StudentCourse, 
#                 Prereq, Route, Driver]

# for student_model in student_models: 
#     try: 
#         admin.site.register(student_model)
#     except: 
#         continue

admin.site.register(Building)
admin.site.register(Classroom)
admin.site.register(Department)
admin.site.register(Course)
admin.site.register(Instructor)
admin.site.register(InstField)
admin.site.register(InstDegree)
admin.site.register(InstPublication)
admin.site.register(Timeslot)
admin.site.register(Section)
admin.site.register(InstTeaches)
admin.site.register(StudentCourse)
admin.site.register(Prereq)
admin.site.register(Route)
admin.site.register(Driver)
