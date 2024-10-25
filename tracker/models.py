from django.db import models

# Create your models here.
class Task(models.Model):
    task_name = models.CharField(max_length=200)

class SubTask(models.Model):
    parent_task = models.ForeignKey(Task, on_delete=models.CASCADE)
    subtask_name = models.CharField(max_length=200)

class Date(models.Model):
    parent_subtask = models.ForeignKey(SubTask, on_delete=models.CASCADE)
    date = models.DateTimeField("Date of Execution")
    status = models.BooleanField()