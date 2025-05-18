from django.core import serializers
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404
from django.views import generic
from rest_framework.views import APIView
from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics, status, viewsets
from .models import Task, SubTask, Date
from .serializers import TaskSerializer, SubTaskSerializer, DateSerializer

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'tasks': reverse('tasks', request=request, format=format),
        'subtasks': reverse('subtasks', request=request, format=format),
        'dates': reverse('dates', request=request, format=format)
    })

class TaskViewSet(viewsets.ModelViewSet):
    """
    This ViewSet automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Task.objects.order_by("date_created")
    serializer_class = TaskSerializer

class SubTaskViewSet(viewsets.ModelViewSet):
    """
    This ViewSet automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = SubTask.objects.order_by("date_created")
    serializer_class = SubTaskSerializer

class DateViewSet(viewsets.ModelViewSet):
    """
    This ViewSet automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Date.objects.order_by("date")
    serializer_class = DateSerializer

# Create your views here.

# def index(request):
#     task_list = Task.objects.order_by("date_created")
#     subtask_list = SubTask.objects.order_by("date_created")
#     #date_list = Date.objects.filter(parent_subtask=subtask_list)
#     data = serializers.serialize('json', subtask_list)
#     return HttpResponse(data, content_type='application/json')
