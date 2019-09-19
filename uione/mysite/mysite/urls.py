"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf.urls import include, url
from django.urls import path

# this is for 2.0
#from django.urls import path, include

from django.contrib import admin
from rest_framework import routers
from TaskApp.views import TaskViewSet

router = routers.DefaultRouter()
router.register(r'task',TaskViewSet)

urlpatterns = [
#    url(r'^$', include(router.urls)),
    #path('admin/', admin.site.urls),

    url(r'^', include(router.urls)),
    #url(r'^admin/', include(admin.site.urls)),

#    This one OK
#    path('', include(router.urls)),

#    This one doesn't work
#    path('admin/', include(admin.site.urls)),



]
