from django.db import models


# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=200)
    date_created = models.DateTimeField("Date of Creation", null=True, blank=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.name
