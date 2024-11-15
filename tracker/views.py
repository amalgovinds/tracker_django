from django.core import serializers
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404
from django.views import generic
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status
from .models import Task, SubTask, Date
from .serializers import TaskSerializer

class TaskList(generics.ListCreateAPIView):
    """
    List All Tasks or Create a new Task.
    """
    queryset = Task.objects.order_by("date_created")
    serializer_class = TaskSerializer

class TaskDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a Task instance.
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer



# Create your views here.

# def index(request):
#     task_list = Task.objects.order_by("date_created")
#     subtask_list = SubTask.objects.order_by("date_created")
#     #date_list = Date.objects.filter(parent_subtask=subtask_list)
#     data = serializers.serialize('json', subtask_list)
#     return HttpResponse(data, content_type='application/json')
