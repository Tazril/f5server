from django.contrib import admin
from bookmarks.models import *
# Register your models here.

admin.site.register(Bookmark)
admin.site.register(Folder)