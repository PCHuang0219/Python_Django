from django.urls import include, path
from . import views

urlpatterns = [

    path('', views.index, name='dc_left_view'),
]