from yt_dlp import YoutubeDL

def scrape_channel_videos(channel_url, max_videos=10):
    ydl_opts = {
        'quiet': True,
        'extract_flat': False,      # Get full video data (views, title, etc.)
        'playlistend': max_videos,  # Limit number of videos
        'skip_download': True
    }

    with YoutubeDL(ydl_opts) as ydl:
        try:
            data = ydl.extract_info(channel_url, download=False)
        except Exception as e:
            raise Exception(f"Failed to extract info: {e}")

        entries = data.get('entries', [])
        if not entries:
            return []

        videos = []
        for entry in entries:
            videos.append({
                'title': entry.get('title', 'N/A'),
                'url': f"https://www.youtube.com/watch?v={entry.get('id')}",
                'id': entry.get('id'),
                'channel': entry.get('channel', 'Unknown'),
                'view_count': entry.get('view_count', 0),
                'upload_date': entry.get('upload_date', '')
            })

        return videos
