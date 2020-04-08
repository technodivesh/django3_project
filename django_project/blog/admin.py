from django.contrib import admin
from .models import Post

admin.site.register(Post)

from django.contrib.auth.models import Group
# admin.site.unregister(Group)

# admin.site.site_header = "DataFlair Django Tutorials"

