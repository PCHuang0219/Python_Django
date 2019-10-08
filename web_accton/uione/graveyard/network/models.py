from django.db import models

# Create your models here.
class Node(models.Model):
    node_name = models.CharField(max_length=80)
    node_desc = models.CharField(max_length=400)
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s" % self.node_name


