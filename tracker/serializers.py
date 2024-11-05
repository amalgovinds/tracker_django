from .models import Task, SubTask, Date
from rest_framework import serializers

class DateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Date
        fields = ['date', 'status']

class SubTaskSerializer(serializers.ModelSerializer):
    dates = DateSerializer(many=True)
    class Meta:
        model = SubTask
        fields = ['subtask','date_created', 'dates']

class TaskSerializer(serializers.ModelSerializer):
    subtasks = SubTaskSerializer(many=True)
    class Meta:
        model = Task
        fields = ['task','date_created', 'subtasks']