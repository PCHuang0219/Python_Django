from django.urls import include, path
from . import views
from pod_manager.monitor.dc_main import views as dc_main_view
from pod_manager.monitor.dc_left import views as dc_left_view
from pod_manager.monitor.dc_back import views as dc_back_view
from pod_manager.monitor.dc_right import views as dc_right_view


urlpatterns = [
    #path('', views.index, name='monitor_index'),

    # This is short cut, for step one
    # You don't need to create anothere url file
    # but you need to do import, do you remember the format?
    path('', views.index, name='monitor_index'),
    path('dc_main/', dc_main_view.index),
    path('dc_left/', dc_left_view.index),
    path('dc_back/', dc_back_view.index),
    path('dc_right/', dc_right_view.index),

    # This is the right way
    #path('', views.index, name='monitor_index'),
    #path('dc_main/', include('pod_manager.monitor.dc_main.urls')),
    #path('dc_left/', include('pod_manager.monitor.dc_left.urls')),
    #path('dc_back/', include('pod_manager.monitor.dc_back.urls')),
    #path('dc_right/', include('pod_manager.monitor.dc_right.urls')),

]
