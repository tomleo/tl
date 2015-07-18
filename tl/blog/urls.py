from django.conf.urls import include, url

urlpatterns = [
    url(r'^$', 'blog.views.home'),
]
