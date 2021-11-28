from enum import unique
from django.db import models
from django.db.models.base import Model
from django.db.models.constraints import UniqueConstraint
from django.db.models.deletion import CASCADE, DO_NOTHING, SET_NULL
from loginApp.models import Student

# Create your models here.

class Building(models.Model):
    building_id = models.CharField(primary_key=True, max_length=10)
    building_name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        db_table = 'building'

class Classroom(models.Model):
    building_id = models.OneToOneField(Building, models.DO_NOTHING, primary_key=True, db_column='building_id')
    room_no = models.IntegerField()
    capacity = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'classroom'
        unique_together = (('building_id', 'room_no'),)

class Department(models.Model):
    dept_name = models.CharField(primary_key=True, max_length=50)
    building_id = models.ForeignKey(Building, models.DO_NOTHING, blank=True, null=True, db_column='building_id')

    class Meta:
        db_table = 'department'

class Course(models.Model):
    course_id = models.CharField(primary_key=True, max_length=8)
    title = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(max_length=500, blank=True, null=True)
    credits = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
    dept_name = models.ForeignKey('Department', models.DO_NOTHING, db_column='dept_name', blank=True, null=True)

    class Meta:
        db_table = 'course'

class Instructor(models.Model):
    inst_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    designation = models.CharField(max_length=100, blank=True, null=True)
    dept_name = models.ForeignKey(Department, models.DO_NOTHING, db_column='dept_name', blank=True, null=True)

    class Meta:
        db_table = 'instructor'

class InstField(models.Model):
    inst_id = models.OneToOneField('Instructor', models.DO_NOTHING, primary_key=True, db_column='inst_id')
    field_of_interest = models.CharField(max_length=50)

    class Meta:
        db_table = 'inst_field'
        unique_together = (('inst_id', 'field_of_interest'),)

class InstDegree(models.Model):
    inst_id = models.OneToOneField('Instructor', models.DO_NOTHING, primary_key=True, db_column='inst_id')
    degree_name = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    country = models.CharField(max_length=100)
    degree_year = models.CharField(max_length=4)

    class Meta:
        db_table = 'inst_degree'
        unique_together = (('inst_id', 'degree_name', 'institution', 'country', 'degree_year'),)

class InstPublication(models.Model):
    inst_id = models.ForeignKey('Instructor', models.DO_NOTHING, db_column='inst_id')
    url = models.CharField(max_length=500, blank=True, null=True)
    title = models.CharField(max_length=500, blank=True, null=True)
    journal = models.CharField(max_length=200, blank=True, null=True)
    publication_year = models.CharField(max_length=4, blank=True, null=True)

    class Meta:
        db_table = 'inst_publication'

class Timeslot(models.Model):
    timeslot_id = models.IntegerField(primary_key=True)
    day = models.CharField(max_length=5)
    start_time = models.TimeField()
    end_time = models.TimeField(blank=True, null=True)

    class Meta:
        db_table = 'timeslot'
        unique_together = (('timeslot_id', 'day', 'start_time'),)

class Section(models.Model):
    course_id = models.OneToOneField(Course, models.DO_NOTHING, primary_key=True, db_column='course_id')
    section_id = models.IntegerField()
    semester = models.CharField(max_length=6)
    section_year = models.CharField(max_length=4)
    building_id = models.ForeignKey(Classroom, models.DO_NOTHING, db_column='building_id', related_name='section_classroom_buildingno')
    room_no = models.ForeignKey(Classroom, models.DO_NOTHING, db_column='room_no', related_name='section_classroom_roomno')
    timeslot_id = models.IntegerField()

    class Meta:
        db_table = 'section'
        unique_together = (('course_id', 'section_id', 'semester', 'section_year'),)

class InstTeaches(models.Model):
    inst_id = models.OneToOneField('Instructor', models.DO_NOTHING, primary_key=True, db_column='inst_id')
    course_id = models.ForeignKey('Section', models.DO_NOTHING, db_column='course_id', related_name='instteaches_section_courseid')
    section_id = models.ForeignKey('Section', models.DO_NOTHING, db_column='section_id', related_name='instteaches_section_sectionid')
    semester = models.ForeignKey('Section', models.DO_NOTHING, db_column='semester', related_name='instteaches_section_semester')
    section_year = models.ForeignKey('Section', models.DO_NOTHING, db_column='section_year', related_name='instteaches_section_sectionyear')

    class Meta:
        db_table = 'inst_teaches'
        unique_together = (('inst_id', 'course_id', 'section_id', 'semester', 'section_year'),)

class StudentCourse(models.Model):
    student_id = models.OneToOneField(Student, models.DO_NOTHING, primary_key=True)
    course_id = models.ForeignKey(Section, models.DO_NOTHING, db_column='course_id', related_name='studentcourse_section_courseid')
    section_id = models.ForeignKey(Section, models.DO_NOTHING, db_column='section_id', related_name='studentcourse_section_sectionid')
    semester = models.ForeignKey(Section, models.DO_NOTHING, db_column='semester', related_name='studentcourse_section_semester')
    section_year = models.ForeignKey(Section, models.DO_NOTHING, db_column='section_year', related_name='studentcourse_section_sectionyear'), 
    ct_1 = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True),
    ct_2 = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True), 
    ct_3 = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True),
    quiz = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True), 
    assignment_1 = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True), 
    assignment_2 = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True), 
    mid = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True),  
    grade = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)

    class Meta:
        db_table = 'student_course'
        unique_together = (('student_id', 'course_id', 'section_id', 'semester',),)

class Prereq(models.Model):
    course_id = models.OneToOneField(Course, models.DO_NOTHING, primary_key=True, related_name='prereq_course_course')
    prereq_id = models.ForeignKey(Course, models.DO_NOTHING, related_name='prereq_course_prereq')

    class Meta:
        db_table = 'prereq'
        unique_together = (('course_id', 'prereq_id'),)

class Route(models.Model):
    route_id = models.IntegerField(primary_key=True)
    route_name = models.CharField(max_length=100, blank=True, null=True)
    timeslot_id = models.ForeignKey('Timeslot', models.DO_NOTHING, blank=True, null=True, db_column='timeslot_id')
    shuttle_id = models.CharField(max_length=5, blank=True, null=True)
    remark = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        db_table = 'route'

class Driver(models.Model):
    driver_id = models.IntegerField(primary_key=True)
    driver_name = models.CharField(max_length=100)
    route_id = models.ForeignKey('Route', models.DO_NOTHING, db_column='route_id')

    class Meta:
        db_table = 'driver'
        unique_together = (('driver_id', 'driver_name', 'route_id'),)