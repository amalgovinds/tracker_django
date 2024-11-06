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
        fields = ['subtask','date_created', 'completed', 'dates']

class TaskSerializer(serializers.ModelSerializer):
    #subtasks = SubTaskSerializer(many=True)
    subtasks = serializers.SerializerMethodField()
    class Meta:
        model = Task
        fields = ['task','date_created', 'subtasks']
    def get_subtasks(self, task):
        subtasks = task.subtasks.order_by("completed")
        return SubTaskSerializer(subtasks, many=True).data