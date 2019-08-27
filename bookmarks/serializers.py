from rest_framework import serializers

from bookmarks.models import Bookmark, Folder


class BookmarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookmark
        fields = ('id', 'url', 'folder')


class FolderSerializer(serializers.ModelSerializer):
    bookmarks = BookmarkSerializer(many=True,read_only=True)
    class Meta:
        model = Folder
        fields = ('id', 'name','bookmarks' )


class FolderListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Folder
        fields = ('id', 'name' )