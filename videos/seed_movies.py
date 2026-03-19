import requests
from datetime import datetime
from videos.models import Video

API_KEY = "ccbb53a6a38ea0730d4a7f90da8cdf03"

def fetch_movies():
    url = f"https://api.themoviedb.org/3/trending/movie/day?api_key={API_KEY}"
    response = requests.get(url)

    if response.status_code != 200:
        print("Error fetching data:", response.text)
        return

    data = response.json()

    for movie in data.get("results", []):
        try:
            Video.objects.get_or_create(
                title=movie.get("title"),
                defaults={
                    "description": movie.get("overview", ""),
                    "category": "Trending",
                    "thumbnail_url": "https://image.tmdb.org/t/p/w500" + str(movie.get("poster_path")),
                    "video_url": "https://sample-videos.com/video123/mp4/720/big_buck_bunny_720p_1mb.mp4",
                    "duration": 7200,
                    "release_date": datetime.strptime(movie.get("release_date"), "%Y-%m-%d").date() if movie.get("release_date") else datetime.today().date(),
                    "is_trending": True
                }
            )
        except Exception as e:
            print("Error saving movie:", e)

    print("✅ Movies inserted successfully!")