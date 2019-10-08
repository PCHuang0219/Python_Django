from django.db import models

# Create your models here.
class Task(models.Model):
    task_name = models.CharField(max_length=20)
    task_desc = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now=True)
#    completed = models.Boo

    def __str__(self):
        return "%s" %self.task_name

