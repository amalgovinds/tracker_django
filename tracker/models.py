from django.db import models

# Create your models here.
#Date used to order Task and SubTask models by creation
class Task(models.Model):
    task_name = models.CharField(max_length=200)
    date_created = models.DateTimeField("Date of Creation")

    def __str__(self):
        return self.task_name

class SubTask(models.Model):
    parent_task = models.ForeignKey(Task, related_name="sub_task", on_delete=models.CASCADE)
    subtask_name = models.CharField(max_length=200)
    date_created = models.DateTimeField("Date of Creation")

    def __str__(self):
        return self.subtask_name

class Date(models.Model):
    parent_subtask = models.ForeignKey(SubTask, related_name="date", on_delete=models.CASCADE)
    date = models.DateTimeField("Date of Execution")
    status = models.BooleanField()

    def __str__(self):
        return str(self.date.date())