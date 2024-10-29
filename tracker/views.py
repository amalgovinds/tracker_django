from django.core import serializers
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Task, SubTask, Date

# Create your views here.

def index(request):
    task_list = Task.objects.all()
    data = serializers.serialize('json', task_list)
    return HttpResponse(data, content_type='application/json')
