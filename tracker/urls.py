from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import TaskList, TaskDetails

urlpatterns = [
    path('tasks', TaskList.as_view(), name="tasks"),
    path('tasks/<int:pk>', TaskDetails.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)