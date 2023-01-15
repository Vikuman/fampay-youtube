from django.db import models
from youtube import constants

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract=True
    

class YoutubeVideos(BaseModel):
    title = models.CharField(max_length=200, null=False)
    description = models.TextField(max_length=500, null=False)
    published_at = models.DateTimeField(null=False)
    thumbnail_data = models.JSONField(default={})
    video_id = models.CharField(max_length=200, null=False)
    search_tag = models.CharField(max_length=200, choices=constants.SearchTag.choices())

    class Meta:
        indexes = [
            models.Index(fields=['published_at']),
        ]


class ApiKeyInfo(BaseModel):
    platform = models.IntegerField(choices=constants.Platform.choices())
    api_key = models.CharField(max_length=200, null=False)
    is_active = models.BooleanField(default=True)
