from __future__ import absolute_import

from django.conf.urls import include, url
from django.contrib import admin

from blog import urls as blog_urls
from project import urls as project_urls

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include(blog_urls)),
    url(r'', include(project_urls))
]
