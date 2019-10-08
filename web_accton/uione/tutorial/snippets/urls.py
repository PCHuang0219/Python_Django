from django.conf.urls import include
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views

urlpatterns = [
    url(r'^snippets/$', views.SnippetList.as_view()),
    url(r'^snippets/(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view()),
    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),

    url(r'^api-auth/', include('rest_framework.urls')),
#    url(r'^', atnurllibviews.index),
]

urlpatterns = format_suffix_patterns(urlpatterns)


# Tutorial 3
#
#
# from django.conf.urls import url
# from rest_framework.urlpatterns import format_suffix_patterns
# from snippets import views
#
# urlpatterns = [
#     url(r'^snippets/$', views.SnippetList.as_view()),
#     url(r'^snippets/(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view()),
# ]
#
# urlpatterns = format_suffix_patterns(urlpatterns)


# Tutorial 1
#
# from django.conf.urls import url
# from rest_framework.urlpatterns import format_suffix_patterns
# from snippets import views
#
# urlpatterns = [
#     url(r'^snippets/$', views.snippet_list),
#     url(r'^snippets/(?P<pk>[0-9]+)/$', views.snippet_detail),
# ]
#
# urlpatterns = format_suffix_patterns(urlpatterns)

