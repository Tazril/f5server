from django.urls import path, include
from rest_framework import routers

from bookmarks.views import *

router = routers.DefaultRouter()
router.register('folder',FolderViewSet)
router.register('bookmark',BookmarkViewSet)

urlpatterns = [
    path('',include(router.urls))
]