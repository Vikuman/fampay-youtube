import enum
from django.utils import timezone

MAX_VIDEOS_PER_PAGE = 20
YOUTUBE_SEARCH_API_V3 = 'https://www.googleapis.com/youtube/v3/search?key={api_key}'

class SearchTag(enum.Enum):
    HOCKEY = 'hockey'
    FOOTBALL = 'football'
    ECONOMY = 'economy'
    INDIA = 'india'

    @classmethod
    def choices(cls):
        return tuple((i.value, i.name) for i in cls)

class Platform(enum.Enum):
    YOUTUBE = 1

    @classmethod
    def choices(cls):
        return tuple((i.value, i.name) for i in cls)

KEY_NAME_REDIS_YOUTUBE_LAST_PUBLISHED_TIME = 'redis_youtube_last_published_time'
DEFAULT_LAST_PUBLISHED_DATETIME = timezone.now() - timezone.timedelta(days=1)
