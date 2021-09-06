from django.urls import path
from .views import TaskDelete, TaskDetails, TaskList, TaskCreate, TaskUpdate, TaskLogin
from django.contrib.auth.views import LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin

urlpatterns = [
    path('login/', TaskLogin.as_view(), name="login"),
    path('logout/', LogoutView.as_view(next_page='login'), name="logout"),
    path('', TaskList.as_view(), name="tasks"),
    path('task/<int:pk>', TaskDetails.as_view(), name="task"),
    path('create-task/', TaskCreate.as_view(), name="create-task"),
    path('task-update/<int:pk>', TaskUpdate.as_view(), name="update-task"),
    path('task-delete/<int:pk>', TaskDelete.as_view(), name="delete-task"),



]
