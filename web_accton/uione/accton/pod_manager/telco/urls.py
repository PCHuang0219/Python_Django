from django.urls import include, path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.index, name='telco'),
    path('vOLT_concepts',views.vOLT),
    path('roadm',views.radom),
    path('dcsg',views.DCSG),
    path('disaggrated_network_solution',views.DND),
    path('cpes',views.cpes),
    path('tip',views.tip),
]

