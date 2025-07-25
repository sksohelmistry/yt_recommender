from yt_dlp import YoutubeDL

def scrape_channel_videos(channel_url, max_videos=20):
    ydl_opts = {
        'quiet': True,
        'extract_flat': 'in_playlist',
        'dump_single_json': True
    }
    with YoutubeDL(ydl_opts) as ydl:
        data = ydl.extract_info(channel_url, download=False)
        videos = []
        for entry in data.get('entries', [])[:max_videos]:
            videos.append({
                'title': entry['title'],
                'url': entry['url'],
                'id': entry['id'],
                'channel': data['title'],
                'view_count': entry.get('view_count', 0),
                'upload_date': entry.get('upload_date', '')
            })
    return videos