from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import TaskList, TaskDetails, SubTaskList, SubTaskDetails, DateList, DateDetails
from . import views

urlpatterns = [
    path('tasks', TaskList.as_view(), name="tasks"),
    path('tasks/<int:pk>', TaskDetails.as_view()),
    path('tasks/subtasks', SubTaskList.as_view(), name="subtasks"),
    path('tasks/subtasks/<int:pk>', SubTaskDetails.as_view()),
    path('tasks/subtasks/dates', DateList.as_view(), name="dates"),
    path('tasks/subtasks/dates/<int:pk>', DateDetails.as_view()),
    path('', views.api_root),

]

urlpatterns = format_suffix_patterns(urlpatterns)