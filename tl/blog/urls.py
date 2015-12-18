from __future__ import absolute_import

from django.conf.urls import include, url
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    url(r'^$', 'blog.views.home'),
    url(r'^posts/$', views.PostListView.as_view(), name='post-list'),
    url(r'^posts/(?P<pk>[0-9]+)/$', views.PostDetailView.as_view(), name='post-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'html'])
#TODO: add i18n_patterns
#urlpatterns = i18n_patterns(urlpatterns)
