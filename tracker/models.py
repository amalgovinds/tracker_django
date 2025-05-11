from django.db import models

# Create your models here.
#Date used to order Task and SubTask models by creation
class Task(models.Model):
    name = models.CharField(max_length=200)
    date_created = models.DateTimeField("Date of Creation", null=True, blank=True)

    def __str__(self):
        return self.name

class SubTask(models.Model):
    task = models.ForeignKey(Task, related_name="subtasks", on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    date_created = models.DateTimeField("Date of Creation", null=True, blank=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Date(models.Model):
    subtask = models.ManyToManyField(SubTask, related_name="dates")
    date = models.DateTimeField("Date of Execution")
    status = models.BooleanField(default=True)

    def __str__(self):
        return str(self.date.date())