from django.core import serializers
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views import generic
from .models import Task, SubTask, Date

class IndexView(generic.ListView):
    def get(self, request):
        task_list = Task.objects.order_by("date_created")
        data = serializers.serialize('json', task_list)
        return HttpResponse(data, content_type='application/json')


# Create your views here.

# def index(request):
#     task_list = Task.objects.order_by("date_created")
#     subtask_list = SubTask.objects.order_by("date_created")
#     #date_list = Date.objects.filter(parent_subtask=subtask_list)
#     data = serializers.serialize('json', subtask_list)
#     return HttpResponse(data, content_type='application/json')
