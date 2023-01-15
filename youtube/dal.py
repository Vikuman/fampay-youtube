from youtube import models
import typing
from youtube import constants

def get_paginated_youtube_videos(limit: int, offset: int, timestamp_before: int) -> typing.List[typing.Dict]:
    return list(
        models.YoutubeVideos.objects.filter(
            published_at__lte=timestamp_before
        ).order_by('-published_at')[offset: limit].values('title', 'description', 'thumbnail_data', 'video_id')
    )
 
def get_searched_youtube_videos(title: str, description: str) -> typing.List[typing.Dict]:
    queryset = models.YoutubeVideos.objects.all()
    if title:
        queryset = queryset.filter(title__icontains=title)
    if description:
        queryset = queryset.filter(description__icontains=description)
    data = queryset.values('title', 'description', 'thumbnail_data', 'video_id')
    return list(data)

def get_active_api_keys(platform: int) -> typing.List[typing.Dict]:
    return list(models.ApiKeyInfo.objects.filter(platform=platform, is_active=True).values_list('api_key', flat=True))

def get_last_published_date(search_tag):
    youtube_video = models.YoutubeVideos.objects.filter(
        search_tag=search_tag
    ).order_by('published_at').last()
    if not youtube_video:
        return constants.DEFAULT_LAST_PUBLISHED_DATETIME
    return youtube_video.published_at

def bulk_create_youtube_videos(data):
    models.YoutubeVideos.objects.bulk_create(data)

def bulk_expire_api_key(expired_keys):
    models.ApiKeyInfo.objects.filter(api_key__in=expired_keys).update(is_active=False)
