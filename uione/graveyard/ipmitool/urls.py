from django.urls import include, path
from . import views

urlpatterns = [
    #path('', views.index, name='monitor_index'),

    #path('', views.index3, name='ipmitool_index'),
    path('', views.index4, name='ipmitool_index'),
]
