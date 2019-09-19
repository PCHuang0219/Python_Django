"""pod_manager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
#from django.conf.urls import url
from django.urls import include, path
from rest_framework import routers

#from pod_manager.network.views import NodeViewSet
from django.contrib import admin
from application import views as application_views
from createform.views import createform


from pod_manager.tmsadmin import views as tmsadmin_view
#from pod_manager.as4610 import views as as4610_view
#from pod_manager.as5812 import views as as5812_view
#from pod_manager.sau5081 import views as sau5081_view
#from pod_manager.ansible import views as ansibleview
from pod_manager.components import views as components_view
from pod_manager.sonic import views as sonic_view
#from pod_manager.network import views as network_view
from pod_manager.personal_settings import views as personal_settings_view
#from pod_manager.search import views as search_view

from django.views.generic.base import TemplateView # 新增
from .views import register,permissin_denied

from django.contrib.auth import logout

router = routers.DefaultRouter()
# router.register(r'network', NodeViewSet)

from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.contrib.auth.views import PasswordResetView
from django.contrib.auth.views import PasswordResetCompleteView
from django.contrib.auth.views import PasswordResetConfirmView
from django.contrib.auth.views import PasswordResetDoneView
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.views import PasswordChangeDoneView
from django.conf.urls import handler404
from . import views



urlpatterns = [
    path('', application_views.mainpage),

    #path('search', application_views.search),

    # path('', TemplateView.as_view(template_name='home.html')), # 新增
    # path('accounts/',include('django.contrib.auth.urls')),s
    url(r'^accounts/register/$', register, name='register'),

    # login logout
    # url(r'^login/$',  LoginView.as_view(template_name='registration/login.html'), name='login'),
    # url(r'^logout/$', LogoutView.as_view(template_name='registration/logged_out.html'), name='logout'),
    # url(r'^password-change/$', PasswordChangeView.as_view(template_name='account/password_change_form.html'), name='password_change'),
    # url(r'^password-change/done/$', PasswordChangeDoneView.as_view(template_name='account/password_change_done.html'), name='password_change_done'),
    # url(r'^password-reset/$',
    #     PasswordResetView.as_view(template_name='account/password_reset_form.html'),
    #     name='password_reset'),
    # url(r'^password-reset/done/$',
    #     PasswordResetDoneView.as_view(),
    #     name='password_reset_done'),
    # url(r'^password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$',
    #     PasswordResetConfirmView.as_view(),
    #     name='password_reset_confirm'),
    # url(r'^password-reset/complete/$',
    #     PasswordResetCompleteView.as_view(),
    #     name='password_reset_complete'),
    url(r'^accounts/permission-denied/$', permissin_denied , name='permission-denied'),
    url(r'^accounts/login/$',  LoginView.as_view(template_name='registration/login.html'), name='login'),
    url(r'^accounts/logout/$', LogoutView.as_view(template_name='registration/logged_out.html'), name='logout'),
    url(r'^accounts/password-change/$', PasswordChangeView.as_view(template_name='account/password_change_form.html'), name='password_change'),
    url(r'^accounts/password-change/done/$', PasswordChangeDoneView.as_view(template_name='account/password_change_done.html'), name='password_change_done'),
    url(r'^accounts/password-reset/$',
        PasswordResetView.as_view(template_name='account/password_reset_form.html'),
        name='password_reset'),
    url(r'^accounts/password-reset/done/$',
        PasswordResetDoneView.as_view(template_name='account/password_reset_done.html'),
        name='password_reset_done'),
    url(r'^accounts/password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$',
        PasswordResetConfirmView.as_view(template_name='account/password_reset_confirm.html'),
        name='password_reset_confirm'),
    url(r'^accounts/password-reset/complete/$',
        PasswordResetCompleteView.as_view(template_name='account/password_reset_complete.html'),
        name='password_reset_complete'),
        
    # path('register/', register, name='register'),
    # path('login/', application_views.login),                          #
    path('overview/', application_views.overview),              # 2nd screen, 4 panels total, 2 X 2

    path('tmsadmin/', include('pod_manager.tmsadmin.urls')),                       # TMS setup screen, has 8 panels, (2 row and 4 columns)

    #path('as4610/', as4610_view.index),                         # as4610 screen
    #path('as5812/', as5812_view.index),
    #path('sau5081', sau5081_view.index),
    #path('ansible/', ansibleview.index),
    path('sonic/', sonic_view.index),
    
    # This is components view, 16 means show 16 racks
    # Components is a very complex operation,
    # Call index directly
    # path('components/', application_views.components),
    # path('components16/', application_views.components16),

    path('components/<int:level>', components_view.index),

    #path('system/', application_views.system),
    path('test/', include('pod_manager.test.urls')),      # standard path format
    #path('manage/', include('pod_manager.management.urls')),    # standard path format
    path('monitor/', include('pod_manager.monitor.urls')),      # standard path format

    #path('network/', include('pod_manager.network.urls')),     # standard path format
    path('setup/', include('pod_manager.podmsetup.urls')),      # standard path format
    #path('systems/', include('pod_manager.systems.urls')),      # standard path format

    #path('curlform/', include('pod_manager.curlform.urls')),
    #path('ipmitool/', include('pod_manager.ipmitool.urls')),
    path('sonic/', include('pod_manager.sonic.urls')),
    path('telco/', include('pod_manager.telco.urls')),
    path('dc/', include('pod_manager.data_center.urls')),
    path('project_management/', include('pod_manager.project_management.urls')),
    path('dms/', include('pod_manager.dms.urls')),
    #path('network/', include('pod_manager.network.urls')),
    path('personal_settings/',  include('pod_manager.personal_settings.urls')),
    path('page/', application_views.page),

    path('switches/', application_views.switches),
    path('racks/', application_views.racks),
    path('storage/', application_views.storage),
    path('nvme/', application_views.nvme),

    path('blades/', application_views.blades),
    path('createform/', createform),
    path('report_center', views.report_center),
    # Finally
    #path('redfish/v1/', include('pod_manager.atnurllib.urls')),

    url(r'^', include(router.urls)),
    # url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'social-auth/', include('social_django.urls', namespace='social'))
]
handler404 = views.page_not_found



#    url(r'^$', app_views.login),
#    url(r'^overview/$', app_views.overview),
#    url(r'^components/$', app_views.components),
#    url(r'^system/$', app_views.system),

#    url(r'^page/$', app_views.page),
#    url(r'^switches/$', app_views.switches),
#    url(r'^racks/$', app_views.racks),
#    url(r'^storage/$', app_views.storage),
#    url(r'^nvme/$', app_views.nvme),

#    url(r'^blades/$', app_views.blades),
#    url(r'^createnode/$', create_form),



