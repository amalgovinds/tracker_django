from django.shortcuts import render
from rest_framework import viewsets
from todo.models import Task
from todo.serializers import TaskSerializer

# Create your views here.


class TaskViewSet(viewsets.ModelViewSet):
    """
    This ViewSet automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """

    queryset = Task.objects.all()
    serializer_class = TaskSerializer
