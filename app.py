import streamlit as st
from scraper import scrape_channel_videos
from recommender import recommend_top

st.title("🧠 YouTube Recommendation Engine")

channels_input = st.text_area("Paste up to 200 YouTube channel URLs (one per line):")
submit = st.button("Get Top 30 Videos")

if submit:
    channel_urls = channels_input.strip().split("\n")
    all_videos = []
    with st.spinner("Scraping channels..."):
        for url in channel_urls:
            try:
                vids = scrape_channel_videos(url)
                all_videos.extend(vids)
            except Exception as e:
                st.warning(f"Failed to scrape {url}: {e}")

    st.success(f"Scraped {len(all_videos)} videos.")

    top_videos = recommend_top(all_videos)
    st.subheader("📈 Top 30 Recommended Videos")
    for vid in top_videos:
        st.markdown(f"**{vid['title']}**")
        st.markdown(f"[Watch now](https://www.youtube.com/watch?v={vid['id']}) — Views: {vid['view_count']}")
        st.markdown("---")