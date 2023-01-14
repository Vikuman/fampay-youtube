from youtube import dal
from datetime import datetime

def get_paginated_youtube_videos(limit, offset, timestamp_before):
    timestamp_before = datetime.fromtimestamp(timestamp_before)
    return dal.get_paginated_youtube_videos(limit, offset, timestamp_before)

def get_searched_youtube_videos(title, description):
    title = title.lower()
    description = description.lower()
    return dal.get_searched_youtube_videos(title, description)
    