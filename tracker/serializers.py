from .models import Task, SubTask, Date
from rest_framework import serializers

#Nested serializer for read_only
class DateReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Date
        fields = ['id', 'date']

class SubTaskReadSerializer(serializers.ModelSerializer):
    dates = DateReadSerializer(many=True, required=False)
    class Meta:
        model = SubTask
        fields = ['id', 'name', 'date_created', 'completed', 'task', 'dates'] 

class TaskReadSerializer(serializers.ModelSerializer):
    subtasks = SubTaskReadSerializer(many=True, read_only=True)
    class Meta:
        model = Task
        fields = ['id', 'name', 'date_created', 'subtasks']
    def get_subtasks(self, task):
        subtasks = task.subtasks.order_by("completed")
        return SubTaskReadSerializer(subtasks, many=True).data
    
#Flat serializer for write_only
class DateWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Date
        fields = ['id', 'subtask', 'date', 'status']

class SubTaskWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubTask
        fields = ['id', 'task', 'name', 'date_created', 'completed']

class TaskWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'name', 'date_created']
