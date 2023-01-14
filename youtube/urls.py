
from django.urls import path
from youtube import views

urlpatterns = [
    path('videos/all', views.get_videos),
    path('videos/search', views.search_videos),
]
