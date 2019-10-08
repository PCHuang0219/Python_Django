from django.urls import include, path
from . import views

# urlpatterns = [
#     path('', views.index, name='network_view'),
# ]

urlpatterns = [
    path('', views.index, name='network_index'),
    path('command/', views.command)
    #path('', views.NodeViewSet, name='network_view'),
]
