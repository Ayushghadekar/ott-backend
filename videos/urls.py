from django.urls import path
from .views import VideoListView, TrendingVideosView, VideoDetailView, SearchVideoView, SaveWatchHistoryView, ContinueWatchingView

urlpatterns = [
    path('videos/', VideoListView.as_view()),
    path('trending/', TrendingVideosView.as_view()),
    path('videos/<int:video_id>/', VideoDetailView.as_view()),
    path('search/', SearchVideoView.as_view()),
    path('watch-history/', SaveWatchHistoryView.as_view()),
    path('continue-watching/<int:user_id>/', ContinueWatchingView.as_view()),
]