from django.db import models

# Create your models here.
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
