from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.contrib.auth.models import User
from loginApp.models import *
from .models import *

from .forms import *

# Create your views here.

def forum(request):

    questions = Question.objects.all()
    form = QuestionForm()
    student = Student.objects.get(user=request.user)
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.student = student
            question.save()
            return HttpResponseRedirect(reverse('forumApp:forum'))

    context = {'questions': questions, 'form': form}
    template_name = 'forumApp/questions.html'
    return render(request, template_name, context)

def discussion_view(request, pk):

    question = Question.objects.get(pk=pk)
    replies = Reply.objects.filter(question=question)
    form = ReplyForm()
    student = Student.objects.get(user=request.user)
    if request.method == 'POST':
        form = ReplyForm(request.POST)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.student = student
            reply.question = question
            reply.save()
            return HttpResponseRedirect(reverse('forumApp:discussion', kwargs={'pk':pk}))

    context = {'replies': replies, 'question': question, 'form': form}
    template_name = 'forumApp/discussion.html'
    return render(request, template_name, context)