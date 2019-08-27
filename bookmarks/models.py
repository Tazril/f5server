from django.db import models


# Create your models here.

class Folder(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name

class Bookmark(models.Model):
    url = models.URLField(unique=True)
    folder = models.ForeignKey(Folder, null=True, related_name='bookmarks',on_delete=models.CASCADE)

    def __str__(self):
        return self.url

    class Meta:
        unique_together = ('url','folder',)
