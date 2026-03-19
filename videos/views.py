from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Video,WatchHistory
from .serializer import VideoSerializer,WatchHistorySerializer
from django.contrib.auth.models import User

class VideoListView(APIView):
    def get(self, request):
        videos = Video.objects.all()
        serializer = VideoSerializer(videos, many=True)
        return Response(serializer.data)


class TrendingVideosView(APIView):
    def get(self, request):
        videos = Video.objects.filter(is_trending=True)
        serializer = VideoSerializer(videos, many=True)
        return Response(serializer.data)
    
class VideoDetailView(APIView):
    def get(self, request, video_id):
        try:
            video = Video.objects.get(id=video_id)
            serializer = VideoSerializer(video)
            return Response(serializer.data)
        except Video.DoesNotExist:
            return Response({"error": "Video not found"}, status=404)
        
class SearchVideoView(APIView):
    def get(self, request):
        query = request.GET.get('q', '')
        videos = Video.objects.filter(title__icontains=query)
        serializer = VideoSerializer(videos, many=True)
        return Response(serializer.data)
    
class SaveWatchHistoryView(APIView):
    def post(self, request):
        user_id = request.data.get("user_id")
        video_id = request.data.get("video_id")
        watched_seconds = request.data.get("watched_seconds", 0)

        try:
            user = User.objects.get(id=user_id)
            video = Video.objects.get(id=video_id)

            obj, created = WatchHistory.objects.update_or_create(
                user=user,
                video=video,
                defaults={"watched_seconds": watched_seconds}
            )

            return Response({"message": "Watch history saved"})

        except Exception as e:
            return Response({"error": str(e)}, status=400)
        
class ContinueWatchingView(APIView):
    def get(self, request, user_id):
        history = WatchHistory.objects.filter(user_id=user_id).order_by('-updated_at')
        serializer = WatchHistorySerializer(history, many=True)
        return Response(serializer.data)
    

