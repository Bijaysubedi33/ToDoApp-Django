from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from .models import Tasks

# Create your views here.


class TaskList(ListView):
    model = Tasks
    context_object_name = 'TasksList'


class TaskDetails(DetailView):
    model = Tasks
    context_object_name = 'TaskDetails'
    template_name = 'mytodoapp/task.html'
