from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING, related_name='student_user')
    fullname = models.CharField(max_length=200)
    department = models.CharField(max_length=100)
    semester = models.CharField(max_length=50)
    student_id = models.CharField(max_length=9)
    address = models.CharField(max_length=500)

    def __str__(self):
        return self.fullname + " " + self.student_id
