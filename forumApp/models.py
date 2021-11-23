from django.contrib.auth.models import User
from django.db import models

from django.contrib.auth.models import User
from loginApp.models import Student

# Create your models here.

class Question(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='student_message')
    question = models.TextField()
    question_date = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-question_date']

    def __str__(self):
        return self.question

class Reply(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='q_reply')
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='user_reply')
    reply = models.TextField()
    reply_date = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-edited']

    def __str__(self):
        return self.reply[:50]