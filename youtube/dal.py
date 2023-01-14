from youtube import models

def get_paginated_youtube_videos(limit, offset, timestamp_before):
    return list(
        models.YoutubeVideos.objects.filter(
            published_at__lte=timestamp_before
        ).order_by('-published_at')[offset: limit].values('title', 'description', 'thumbnail_data', 'video_id')
    )
 
def get_searched_youtube_videos(title, description):
    queryset = models.YoutubeVideos.objects.all()
    if title:
        queryset = queryset.filter(title__icontains=title)
    if description:
        queryset = queryset.filter(description__icontains=description)
    data = queryset.values('title', 'description', 'thumbnail_data', 'video_id')
    return list(data)
