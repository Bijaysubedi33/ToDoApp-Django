from django.shortcuts import redirect
from django.utils.module_loading import import_string
from .models import Tasks
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.contrib.auth.password_validation import validate_password
# Create your views here.


class TaskLogin(LoginView):
    template_name = 'ToDo/login.html'
    fields = '__all__'
    redirect_authenticated_user = False

    def get_success_url(self):
        return reverse_lazy('tasks')


class UserRegisterPage(FormView):
    template_name = 'ToDo/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(UserRegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            redirect('tasks')
        return super(UserRegisterPage, self).get(*args, **kwargs)


class TaskList(LoginRequiredMixin, ListView):
    model = Tasks
    context_object_name = 'TasksList'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['TasksList'] = context['TasksList'].filter(
            user=self.request.user)
        context['count'] = context['TasksList'].filter(completed=False).count()
        search_input = self.request.GET.get('search-value') or ''
        if search_input:
            context['TasksList'] = context['TasksList'].filter(
                title__icontains=search_input)
        context['search_input'] = search_input

        return context


class TaskDetails(LoginRequiredMixin, DetailView):
    model = Tasks
    context_object_name = 'TaskDetails'
    template_name = 'ToDo/task.html'


class TaskCreate(LoginRequiredMixin, CreateView):
    model = Tasks
    fields = ['title', 'description']
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)


class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Tasks
    fields = ['title', 'description', 'completed']
    success_url = reverse_lazy('tasks')


class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Tasks
    context_object_name = 'TaskDelete'
    success_url = reverse_lazy('tasks')
