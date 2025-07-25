# scraper.py
import yt_dlp
import time

def scrape_channel_videos(channel_url, max_videos=10):
    ydl_opts = {
        'quiet': True,
        'extract_flat': True,
        'force_generic_extractor': True,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(channel_url, download=False)

            if '_type' in info and info['_type'] == 'playlist':
                entries = info.get('entries', [])[:max_videos]
                videos = []

                for entry in entries:
                    try:
                        video_url = f"https://www.youtube.com/watch?v={entry['id']}"
                        video_info = ydl.extract_info(video_url, download=False)

                        videos.append({
                            'title': video_info.get('title'),
                            'url': video_url,
                            'views': video_info.get('view_count', 0),
                            'upload_date': video_info.get('upload_date'),
                            'thumbnail': video_info.get('thumbnail'),
                        })
                    except Exception as ve:
                        print(f"Skipped video: {ve}")
                    time.sleep(0.5)

                return videos
            else:
                print(f"Not a valid channel or playlist: {channel_url}")
                return []
    except Exception as e:
        print(f"Error scraping {channel_url}: {e}")
        return []
