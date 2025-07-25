# app.py
import streamlit as st
from scraper import scrape_channel_videos

st.set_page_config(page_title="YouTube Channel Recommender", layout="wide")
st.title("🎯 YouTube Channel Recommender")

# User input: YouTube channel URLs (one per line)
channel_urls_input = st.text_area("Paste YouTube channel URLs (one per line):", height=200)
max_videos = st.slider("Max videos per channel", min_value=1, max_value=20, value=5)

if st.button("🔍 Scrape & Recommend"):
    with st.spinner("Scraping YouTube... Please wait."):
        channel_urls = [url.strip() for url in channel_urls_input.split('\n') if url.strip()]
        all_videos = []

        for url in channel_urls:
            try:
                videos = scrape_channel_videos(url, max_videos=max_videos)
                all_videos.extend(videos)
            except Exception as e:
                st.error(f"Error scraping {url}: {e}")

        if all_videos:
            st.success(f"✅ Scraped {len(all_videos)} video(s) successfully.")
            for video in all_videos:
                st.markdown(f"### [{video['title']}]({video['url']})")
                st.image(video['thumbnail'], width=320)
                st.write(f"📅 Uploaded: {video['upload_date']} | 👁️ Views: {video['views']}")
                st.markdown("---")
        else:
            st.warning("⚠️ No videos found. Channel may be invalid or private.")
