from youtube import dal
from datetime import datetime
import redis
from django.conf import settings
from youtube import constants

def get_paginated_youtube_videos(limit, offset, timestamp_before):
    timestamp_before = datetime.fromtimestamp(timestamp_before)
    return dal.get_paginated_youtube_videos(limit, offset, timestamp_before)

def get_searched_youtube_videos(title, description):
    title = title.lower()
    description = description.lower()
    return dal.get_searched_youtube_videos(title, description)
    
def get_last_published_date(search_tag):
    # we can implement singleton pattern for below skipping for now
    # TODO: VIKAS BANSAL
    # redis_instance = redis.StrictRedis(
    #     host=settings.REDIS_HOST,
    #     port=settings.REDIS_PORT,db=0
    # )

    # taking data from cache
    # last_published_datetime = redis_instance.get(constants.KEY_NAME_REDIS_YOUTUBE_LAST_PUBLISHED_TIME)
    # if not last_published_datetime:
    last_published_datetime = dal.get_last_published_date(search_tag)
        # redis_instance.set(constants.KEY_NAME_REDIS_YOUTUBE_LAST_PUBLISHED_TIME, last_published_datetime)
    return last_published_datetime

def get_active_youtube_api_keys():
    return dal.get_active_api_keys(constants.Platform.YOUTUBE.value)
