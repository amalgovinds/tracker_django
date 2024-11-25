from django.core import serializers
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404
from django.views import generic
from rest_framework.views import APIView
from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics, status
from .models import Task, SubTask, Date
from .serializers import TaskSerializer, SubTaskSerializer, DateSerializer

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'tasks': reverse('tasks', request=request, format=format),
        'subtasks': reverse('subtasks', request=request, format=format),
        'dates': reverse('dates', request=request, format=format)
    })

class TaskList(generics.ListCreateAPIView):
    """
    List All Tasks or Create a new Task.
    GET + POST
    """
    queryset = Task.objects.order_by("date_created")
    serializer_class = TaskSerializer

class TaskDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a Task instance.
    GET + UPDATE + DELETE
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class SubTaskList(generics.ListCreateAPIView):
    """
    List All Tasks or Create a new SubTask.
    GET + POST
    """
    queryset = SubTask.objects.order_by("date_created")
    serializer_class = SubTaskSerializer
    # def perform_create(self, serializer):
    #     print(self.request)
    #     serializer.save(task=self.request.task)

class SubTaskDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a SubTask instance.
    GET + UPDATE + DELETE
    """
    queryset = SubTask.objects.all()
    serializer_class = SubTaskSerializer

class DateList(generics.ListCreateAPIView):
    """
    List All Tasks or Create a new Date.
    GET + POST
    """
    queryset = Date.objects.order_by("date")
    serializer_class = DateSerializer
    # def perform_create(self, serializer):
    #     print(self.request)
    #     serializer.save(task=self.request.task)

class DateDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a Date instance.
    GET + UPDATE + DELETE
    """
    queryset = Date.objects.all()
    serializer_class = DateSerializer

# Create your views here.

# def index(request):
#     task_list = Task.objects.order_by("date_created")
#     subtask_list = SubTask.objects.order_by("date_created")
#     #date_list = Date.objects.filter(parent_subtask=subtask_list)
#     data = serializers.serialize('json', subtask_list)
#     return HttpResponse(data, content_type='application/json')
