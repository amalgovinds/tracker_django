from django.db import models

# Create your models here.
class Task(models.Model):
    task_name = models.CharField(max_length=200)

    def __str__(self):
        return self.task_name

class SubTask(models.Model):
    parent_task = models.ForeignKey(Task, on_delete=models.CASCADE)
    subtask_name = models.CharField(max_length=200)

    def __str__(self):
        return self.subtask_name

class Date(models.Model):
    parent_subtask = models.ForeignKey(SubTask, on_delete=models.CASCADE)
    date = models.DateTimeField("Date of Execution")
    status = models.BooleanField()

    def __str__(self):
        return str(self.date.date())