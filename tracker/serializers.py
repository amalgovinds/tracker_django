from .models import Task, SubTask, Date
from rest_framework import serializers

class DateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Date
        fields = ['id', 'date', 'parent_subtask', 'status']

class SubTaskSerializer(serializers.ModelSerializer):
    dates = DateSerializer(many=True, read_only=True)
    class Meta:
        model = SubTask
        fields = ['id', 'subtask', 'parent_task', 'date_created', 'completed', 'dates'] 
    """ Create a Wriatble nested Serializer (Future Scope)"""
    # def create(self, validated_data):
    #     date_data = validated_data.pop('dates')
    #     subtask = SubTask.objects.create(**validated_data)
    #     for d_data in date_data:
    #         Date.objects.create(subtask=subtask, **d_data)
    #     return subtask

class TaskSerializer(serializers.ModelSerializer):
    # subtasks = SubTaskSerializer(many=True, read_only=True)
    #SerializerMethodField is read_only by default
    subtasks = serializers.SerializerMethodField()
    class Meta:
        model = Task
        fields = ['id', 'task', 'date_created', 'subtasks']
    def get_subtasks(self, task):
        subtasks = task.subtasks.order_by("completed")
        return SubTaskSerializer(subtasks, many=True).data