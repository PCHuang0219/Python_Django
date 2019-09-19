from django.conf.urls import url
from django.conf.urls import path
from polls import views


urlpatterns = [
    # not sure where this line comes from, below this
    # line is the one from Django sample
    #url(r'^$', views.post_list, name = 'post_list'),

    path('', views.index, name='index'),
]
