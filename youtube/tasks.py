from celery import shared_task
from youtube import constants
from youtube import private
import requests
from youtube import models
from datetime import datetime
from youtube import dal
from django.utils import timezone

def _get_iso_format_date(datetime_field):
    if not datetime_field:
        return (timezone.now().replace(tzinfo=None)).isoformat("T") + "Z"
    return (datetime_field.replace(tzinfo=None)).isoformat("T") + "Z"

def _format_video_reponse_data(items, data, search_tag):
    for item in items:
        snippet = item['snippet']
        data.append(
            models.YoutubeVideos(   
                video_id=item['id']['videoId'],
                title=snippet['title'].lower(),
                description=snippet['description'].lower(),
                published_at=datetime.strptime(
                    snippet['publishedAt'], '%Y-%m-%dT%H:%M:%SZ'
                ).utcnow().replace(microsecond=0),
                thumbnail_data=snippet['thumbnails'],
                search_tag=search_tag
            )
        )


@shared_task(bind=True)
def fetch_youtube_videos(self):
    api_keys = private.get_active_youtube_api_keys()
    if not api_keys:
        print("No active youtube api key left, please add active api key")
        return
    expired_api_keys = []
    page_token = None

    # latest published date of youtube video which we have
    search_tag = constants.SearchTag.FOOTBALL.value
    current_last_published_date = _get_iso_format_date(private.get_last_published_date(search_tag))
    data_exists = True
    videos_data = []
    for api_key in api_keys:
        url = constants.YOUTUBE_SEARCH_API_V3.format(api_key=api_key)
        params = {
            'part': 'id,snippet',
            'type': 'video',
            'order': 'date',
            'q': search_tag,
            'publishedAfter': current_last_published_date,
        }
        while data_exists:
            if page_token:
                params['pageToken'] = page_token
            videos_response = requests.get(url=url, params=params)
            if videos_response.status_code == 403:
                expired_api_keys.append(api_key)
                break
            elif videos_response.status_code == 200:
                videos_response = videos_response.json()
                results_per_page = videos_response.get('pageInfo', {}).get('resultsPerPage', 0)
                page_token = videos_response.get('nextPageToken', '')
                if results_per_page <= 0:
                    data_exists = False
                    break
                _format_video_reponse_data(videos_response.get('items', []), videos_data, search_tag)
                if not page_token:
                    data_exists = False
                    break
            else:
                # Logging whatever went wrong
                print("something went wrong!!")
                data_exists = True
                break

    dal.bulk_create_youtube_videos(videos_data)
    dal.bulk_expire_api_key(expired_api_keys)
