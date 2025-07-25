from yt_dlp import YoutubeDL

def scrape_channel_videos(channel_url, max_videos=20):
    ydl_opts = {
        'quiet': True,
        'extract_flat': True,
        'force_generic_extractor': True,
    }
    with YoutubeDL(ydl_opts) as ydl:
        try:
            data = ydl.extract_info(channel_url, download=False)
        except Exception as e:
            raise Exception(f"Failed to extract info: {e}")

        videos = []
        for entry in data.get('entries', [])[:max_videos]:
            video_id = entry.get('id')
            if video_id:
                videos.append({
                    'title': entry.get('title', 'N/A'),
                    'url': f"https://www.youtube.com/watch?v={video_id}",
                    'id': video_id,
                    'channel': data.get('title', 'Unknown'),
                    'view_count': entry.get('view_count', 0),
                    'upload_date': entry.get('upload_date', '')
                })
        return videos
