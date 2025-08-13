from django.db import models


# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=200, verbose_name="Task Name")
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Date of Creation"
    )
    is_completed = models.BooleanField(default=False, verbose_name="Completed Status")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Last Updated")

    def __str__(self):
        return self.name
