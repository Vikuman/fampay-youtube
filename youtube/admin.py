from django.contrib import admin
from youtube import models

@admin.register(models.YoutubeVideos)
class YoutubeVideosAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'search_tag',
        'description',
        'published_at',
        'thumbnail_data',
        'video_id'
    ]
    list_filter = ['title', 'search_tag']

@admin.register(models.ApiKeyInfo)
class ApiKeyInfoAdmin(admin.ModelAdmin):
    list_display = [
        'platform',
        'api_key',
        'is_active'
    ]
    list_filter = ['platform', 'is_active']
