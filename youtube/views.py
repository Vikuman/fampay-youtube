from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotAllowed
from django.views.decorators.http import require_GET

# Create your views here.

@require_GET
def get_videos(request):
    limit = request.GET.get('limit')
    offset = request.GET.get('offset')
    data = {}
    return HttpResponse(data)

@require_GET
def search_video(request):
    if request.method == 'GET':
        title = request.GET.get('title')
        description = request.GET.get('description')
        data = {}
        return HttpResponse(data)
    return HttpResponseNotAllowed(['POST'])