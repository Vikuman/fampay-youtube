import enum

MAX_VIDEOS_PER_PAGE = 20

class SearchTag(enum.Enum):
    HOCKEY = 'hockey'
    FOOTBALL = 'football'
    ECONOMY = 'economy'
    INDIA = 'india'

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)
