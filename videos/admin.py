from django.contrib import admin
from .models import Video
from .models import WatchHistory

admin.site.register(Video)
admin.site.register(WatchHistory)
