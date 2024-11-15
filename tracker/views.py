from django.core import serializers
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404
from django.views import generic
from .models import Task, SubTask, Date
from .serializers import TaskSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class TaskList(APIView):
    """
    List All Tasks or Create a new Task.
    """
    def get(self, request):
        task_list = Task.objects.order_by("date_created")
        serializer = TaskSerializer(task_list, many=True)
        #data = serializers.serialize('json', task_list)
        return Response(serializer.data)
    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TaskDetails(APIView):
    """
    Retrieve, update or delete a Task instance.
    """
    def get_object(self, pk):
        try:
            return Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None):
        task = self.get_object(pk)
        serializer = TaskSerializer(task)
        return Response(serializer.data)    
    
    def put(self, request, pk, format=None):
        task = self.get_object(pk)
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        task = self.get_object(pk)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



# Create your views here.

# def index(request):
#     task_list = Task.objects.order_by("date_created")
#     subtask_list = SubTask.objects.order_by("date_created")
#     #date_list = Date.objects.filter(parent_subtask=subtask_list)
#     data = serializers.serialize('json', subtask_list)
#     return HttpResponse(data, content_type='application/json')
