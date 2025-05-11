from .models import Task, SubTask, Date
from rest_framework import serializers

class DateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Date
        fields = ['date']

class SubTaskSerializer(serializers.ModelSerializer):
    dates = DateSerializer(many=True, read_only=True)
    class Meta:
        model = SubTask
        fields = ['id', 'name', 'date_created', 'completed', 'dates'] 
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
    # def create(self, validated_data):
    #     subtasks_data = validated_data.pop('subtasks')
    #     task = Task.objects.create(**validated_data)
    #     for subtask_data in subtasks_data:
    #         SubTask.objects.create(task=task, **subtask_data)
    #     return task
    class Meta:
        model = Task
        fields = ['id', 'name', 'date_created', 'subtasks']
    def get_subtasks(self, task):
        subtasks = task.subtasks.order_by("completed")
        return SubTaskSerializer(subtasks, many=True).data