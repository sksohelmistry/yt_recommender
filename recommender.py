from datetime import datetime

def score_video(video):
    views = video.get('view_count') or 0  # default to 0 if None
    date_str = video.get('upload_date', '')

    recency_score = 0
    if date_str:
        try:
            age_days = (datetime.now() - datetime.strptime(date_str, "%Y%m%d")).days
            recency_score = max(0, 30 - age_days)  # more recent = higher score
        except Exception:
            pass

    return views + (recency_score * 1000)

def recommend_top(videos, top_n=30):
    for v in videos:
        try:
            v['score'] = score_video(v)
        except Exception as e:
            v['score'] = 0  # fallback if any error
    return sorted(videos, key=lambda x: x['score'], reverse=True)[:top_n]
