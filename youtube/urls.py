
from django.urls import path
from youtube import views

urlpatterns = [
    path('videos/all', views.get_videos),
]
