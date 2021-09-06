from django.urls import path
from .views import TaskDetails, TaskList


urlpatterns = [
    path('', TaskList.as_view(), name="tasks"),
    path('task/<int:pk>', TaskDetails.as_view(), name="task")
]
