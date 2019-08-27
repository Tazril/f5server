from typing import Any

from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.
from rest_framework.request import Request
from rest_framework.response import Response

from bookmarks.models import *
from bookmarks.serializers import *


class BookmarkViewSet(viewsets.ModelViewSet):
    queryset = Bookmark.objects.all()
    serializer_class = BookmarkSerializer


class FolderViewSet(viewsets.ModelViewSet):
    queryset = Folder.objects.all()
    serializer_class = FolderSerializer

    def list(self, request: Request, *args: Any, **kwargs: Any):
        queryset = Folder.objects.all()
        serializer = FolderListSerializer(queryset, many=True)
        return Response(serializer.data)

'''
cd..
test\Scripts\activate
cd f5server
'''