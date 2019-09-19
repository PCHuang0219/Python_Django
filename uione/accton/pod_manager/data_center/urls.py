from django.urls import include, path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.index, name='sonic'),
    path('image/',views.post_personal_image),
]

