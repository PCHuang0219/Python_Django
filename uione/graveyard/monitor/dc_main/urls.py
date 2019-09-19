from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.index, name='dc_main_view'),
]
