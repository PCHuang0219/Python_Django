from django.urls import include, path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.index, name='sonic'),
    path('get/personal_picture/',views.get_personal_image),

    path('save/personal_picture/',views.save_personal_image),
    path('save/changeDB/',views.save_user_information),
    path('getInfoByUser/',views.get_user_data),
]