from django.conf.urls import include, url
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    url(r'^project/$', views.ProjectListView.as_view(), name='project-list'),
    url(r'^project/(?P<pk>[0-9]+)/$', views.ProjectDetailView.as_view(), name='project-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'html'])
#TODO: add i18n_patterns
#urlpatterns = i18n_patterns(urlpatterns)

