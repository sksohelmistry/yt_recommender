import pandas as pd
from datetime import datetime

def score_video(video):
    views = video['view_count']
    date_str = video.get('upload_date', '')
    if date_str:
        try:
            age_days = (datetime.now() - datetime.strptime(date_str, "%Y%m%d")).days
            recency_score = max(0, 30 - age_days)  # Favor newer videos
        except:
            recency_score = 0
    else:
        recency_score = 0

    return views + (recency_score * 1000)

def recommend_top(videos, top_n=30):
    for v in videos:
        v['score'] = score_video(v)
    return sorted(videos, key=lambda x: x['score'], reverse=True)[:top_n]