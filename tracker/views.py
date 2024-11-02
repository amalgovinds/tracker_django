from django.core import serializers
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Task, SubTask, Date

# Create your views here.

def index(request):
    task_list = Task.objects.last()
    subtask_list = SubTask.objects.filter(parent_task=task_list).last()
    date_list = Date.objects.filter(parent_subtask=subtask_list)
    data = serializers.serialize('json', date_list)
    return HttpResponse(data, content_type='application/json')
