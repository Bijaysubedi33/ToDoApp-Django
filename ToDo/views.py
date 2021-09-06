from .models import Tasks
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
# Create your views here.


class TaskLogin(LoginView):
    template_name = 'ToDo/login.html'
    fields = '__all__'
    redirect_authenticated_user = False

    def get_success_url(self):
        return reverse_lazy('tasks')


class TaskList(LoginRequiredMixin, ListView):
    model = Tasks
    context_object_name = 'TasksList'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['TasksList'] = context['TasksList'].filter(
            user=self.request.user)
        context['count'] = context['TasksList'].filter(completed=False).count()
        return context


class TaskDetails(LoginRequiredMixin, DetailView):
    model = Tasks
    context_object_name = 'TaskDetails'
    template_name = 'ToDo/task.html'


class TaskCreate(LoginRequiredMixin, CreateView):
    model = Tasks
    fields = '__all__'
    success_url = reverse_lazy('tasks')


class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Tasks
    fields = '__all__'
    success_url = reverse_lazy('tasks')


class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Tasks
    context_object_name = 'TaskDelete'
    success_url = reverse_lazy('tasks')
