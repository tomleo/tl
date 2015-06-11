from __future__ import absolute_import

from django.contrib import admin

from .models import Post

admin.site.register(Post)