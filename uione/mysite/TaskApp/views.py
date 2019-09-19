from django.shortcuts import render
from .models import Task
from .Serializers import TaskSerializer
from rest_framework import viewsets
from .Serializers import TaskSerializer
from rest_framework import filters

# Create your views here.
# class TaskViewSet(viewsets):
#     queryset = Task.objects.all()   # We use Filters for ordering so remove
#                                     # order by part
#     serializer_class = TaskSerializer
#     filter_backends = (filters.DjangoFilterBackend,filters.orderingFilter,filters.SearchFilter,)
#     filter_field = ('completed',)
#     ordering = ('-date_created',)
#     search_fields = ('task_name')   # here we use Model Field for searching

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('-date_created')
    serializer_class = TaskSerializer

# class DueTaskViewSet(viewsets.ModelViewSet):
#     queryset = Task.objects.all().order_by('-date_created').filter(completed=False)
#     serializer_class = TaskSerializer

# class CompletedTaskViewSet(viewsets.ModelViewSet):
#     queryset = Task.objects.all().order_by('-date_created').filter(completed=True)
