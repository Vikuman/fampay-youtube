import enum

MAX_VIDEOS_PER_PAGE = 20
YOUTUBE_SEARCH_API_V3 = 'https://www.googleapis.com/youtube/v3/search?key={api_key}'

class SearchTag(enum.Enum):
    HOCKEY = 'hockey'
    FOOTBALL = 'football'
    ECONOMY = 'economy'
    INDIA = 'india'

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)

class Platform(enum.Enum):
    YOUTUBE = 1

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)

YOUTUBE_REDIS_API_KEY_NAME = 'youtube_redis_api_key_name'