from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotAllowed, HttpResponseBadRequest, JsonResponse
from django.views.decorators.http import require_GET
from youtube import constants
from youtube import private
from django.utils import timezone


@require_GET
def get_videos(request):
    limit_str = request.GET.get('limit')
    offset_str = request.GET.get('offset')

    if not limit_str or not offset_str:
        return HttpResponseBadRequest('Data not valid!!')
    timestamp_before = request.GET.get('timestamp_before')

    # query params validation
    if not limit_str.isdigit() or not offset_str.isdigit():
        return HttpResponseBadRequest('Data not valid!!')

    if timestamp_before and not timestamp_before.isdigit():
        return HttpResponseBadRequest('Data not valid!!')

    if not timestamp_before:
        timestamp_before = int(timezone.now().timestamp())

    limit = int(limit_str)

    # Check so that we might not end up in fetching a lot of data for a single page won't be a good user experience too.
    if limit > constants.MAX_VIDEOS_PER_PAGE:
        return HttpResponseBadRequest('Videos per page limit exceeded!!')

    offset = int(offset_str)
    timestamp_before = int(timestamp_before)
    youtube_videos_data = private.get_paginated_youtube_videos(limit, offset, timestamp_before)
    return JsonResponse(
        {
            'timestamp_before': timestamp_before,
            'videos_data': youtube_videos_data
        }
    )

@require_GET
def search_videos(request):
    title = request.GET.get('title')
    description = request.GET.get('description')
    if not title and not description:
        return HttpResponse([])

    youtube_videos_data = private.get_searched_youtube_videos(title, description)

    return JsonResponse(
        {
            'videos_data': youtube_videos_data
        }
    )
