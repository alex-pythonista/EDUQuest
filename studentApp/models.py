from enum import unique
from django.db import models
from django.db.models.base import Model
from django.db.models.constraints import UniqueConstraint
from django.db.models.deletion import CASCADE, DO_NOTHING, SET_NULL
from loginApp.models import Student

# Create your models here.

class classroom(models.Model): 
    building = models.CharField(max_length=100, default='Main') 
    room_no = models.IntegerField(primary_key=True)
    capacity = models.IntegerField(null = True) 

    class Meta:
        unique_together = ('building', 'room_no',)

class department(models.Model): 
    dept_name = models.CharField(max_length=10, primary_key=True)
    building = models.CharField(max_length=100, default='Main') 

class course(models.Model):
    course_id = models.CharField(max_length=10, default='', primary_key=True)
    title = models.CharField(max_length=200, default='')
    credit = models.DecimalField(decimal_places=2, max_digits=3, default=3)
    dept_name = models.ForeignKey(department, on_delete = models.DO_NOTHING)

class instructor(models.Model): 
    inst_id = models.IntegerField(primary_key= True)
    inst_name = models.CharField(max_length=100, default='') 
    email = models.CharField(max_length=50, default='')
    designation = models.CharField(max_length=50, default='Lecturer')
    dept_name = models.ForeignKey(department, on_delete = models.DO_NOTHING)

class inst_field(models.Model): 
   inst_id = models.ForeignKey(instructor, on_delete = models.DO_NOTHING, primary_key=True)
   field_of_interest = models.CharField(max_length= 500)

   class Meta:
        unique_together = ('inst_id', 'field_of_interest',)

class inst_degree(models.Model):
    inst_id = models.ForeignKey(instructor, on_delete = models.DO_NOTHING, primary_key=True)
    degree_name = models.CharField(max_length=100)
    institution = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    year = models.IntegerField(max_length=4)

    class Meta:
        unique_together = ('inst_id', 'degree_name', 'institution', 'country', 'year',) 

class inst_publication(models.Model):
    inst_id = models.ForeignKey(instructor, on_delete = models.DO_NOTHING, primary_key=True)
    url = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    journal = models.CharField(max_length=200)
    year = models.IntegerField(max_length=4)

    class Meta: 
        unique_together = ('inst_id', 'url', 'title', 'journal', 'year',)

class timeslot(models.Model): 
    timeslot_id = models.CharField(max_length=5, primary_key=True, default= '')
    day = models.CharField(max_length=3, default='')
    start_time = models.TimeField(default='20:00')
    end_time = models.TimeField(default='20:00')

    class Meta: 
        unique_together = ('timeslot_id', 'day', 'start_time',)


class section(models.Model): 
    section_id = models.CharField(max_length=10, primary_key=True, default='')
    course_id  = models.ForeignKey(course, on_delete = models.DO_NOTHING)
    sem_code = models.CharField(max_length=5, default='')
    building = models.CharField(max_length=100, default='Main') 
    room_no = models.ForeignKey(classroom, on_delete=models.DO_NOTHING)
    timeslot_id = models.ForeignKey(timeslot, on_delete=models.DO_NOTHING)

    class Meta: 
        unique_together = ('course_id', 'section_id', 'sem_code',)

# class teaches(models.Model): 
#     inst_id = models.ForeignKey(instructor, on_delete = models.DO_NOTHING, primary_key=True) 
#     course_id = models.ForeignKey(course, on_delete = models.DO_NOTHING)
#     section_id = models.ForeignKey(section, on_delete= models.DO_NOTHING)
#     sem_code = models.ForeignKey(section, on_delete= models.DO_NOTHING)

#     class Meta: 
#         unique_together = ('inst_id', 'course_id', 'section_id', 'sem_code',)

# class takes(models.Model): 
#     student_id = models.ForeignKey(Student, on_delete=DO_NOTHING)
#     course_id = models.ForeignKey(course, on_delete = models.DO_NOTHING)
#     section_id = models.ForeignKey(section, on_delete= models.DO_NOTHING)
#     sem_code = models.ForeignKey(section, on_delete= models.DO_NOTHING)
#     ct1 = models.DecimalField(decimal_places=1, max_digits=3)
#     ct2 = models.DecimalField(decimal_places=1, max_digits=3)
#     mid = models.DecimalField(decimal_places=1, max_digits=3)
#     assignment = models.DecimalField(decimal_places=1, max_digits=3)

#     class Meta: 
#         unique_together = ('student_id', 'course_id', 'section_id', 'sem_code',)

# class prereq(models.Model): 
#     course_id = models.ForeignKey(course, on_delete = models.DO_NOTHING)
#     prereq_id = models.ForeignKey(course, on_delete = models.DO_NOTHING) 

#     class Meta: 
#         unique_together = ('course_id', 'prereq_id',)








   






