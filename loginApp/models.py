from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING, related_name='student_user')
    fullname = models.CharField(max_length=200, default='UNKNOWN')
    department = models.CharField(max_length=10, default='UNKNOWN')
    semester = models.CharField(max_length=50)
    student_id = models.CharField(max_length=10, primary_key=True)
    address = models.CharField(max_length=500, default='UNKNOWN')
    cgpa = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
    credit_taken = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True) 
    credit_completed = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='student_profile', blank=True, null=True)

    def __str__(self):
        return self.student_id
