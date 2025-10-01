import re
from collections import Counter
import matplotlib.pyplot as plt
import streamlit as st
from googleapiclient.discovery import build
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# YouTube API setup
api_key = "AIzaSyCLUM3PLvXMTLeTuj6CF0hIbY26Fe4crWY"
youtube = build('youtube', 'v3', developerKey=api_key)

# Cleaning function
def clean_text(text):
    text = re.sub(r'http\S+', '', text)  # remove links
    return text.strip()

# Fetch comments
def get_comments(video_id, max_results=30):
    request = youtube.commentThreads().list(
        part="snippet",
        videoId=video_id,
        maxResults=max_results,
        textFormat="plainText"
    )
    response = request.execute()
    comments = [item['snippet']['topLevelComment']['snippet']['textDisplay'] 
                for item in response['items']]
    return comments

# Sentiment analysis
def analyze_sentiments(comments):
    analyzer = SentimentIntensityAnalyzer()
    results = []
    for c in comments:
        clean = clean_text(c)
        score = analyzer.polarity_scores(clean)
        if score['compound'] >= 0.05:
            sentiment = "Positive"
        elif score['compound'] <= -0.05:
            sentiment = "Negative"
        else:
            sentiment = "Neutral"
        results.append((clean, sentiment))
    return results

# Streamlit UI
st.title("🎥 YouTube Comment Sentiment Analyzer")
video_url = st.text_input("Enter YouTube Video URL")

if st.button("Analyze"):
    try:
        # Extract video ID from URL (works for both youtu.be and youtube.com)
        if "v=" in video_url:
            video_id = video_url.split("v=")[-1]
        else:
            video_id = video_url.split("/")[-1]

        comments = get_comments(video_id)
        results = analyze_sentiments(comments)

        # ✅ Show sample comments with sentiment
        st.subheader("📌 Comments with Sentiment")
        for c, s in results[:20]:   # show first 20
            if s == "Positive":
                st.success(f"🙂 {c}")
            elif s == "Negative":
                st.error(f"🙁 {c}")
            else:
                st.info(f"😐 {c}")

        # ✅ Show sentiment distribution chart
        sentiments = [s for _, s in results]
        counts = Counter(sentiments)

        st.subheader("📊 Sentiment Distribution")
        fig, ax = plt.subplots()
        ax.pie(counts.values(), labels=counts.keys(), autopct='%1.1f%%', startangle=90)
        ax.axis('equal')
        st.pyplot(fig)

    except Exception as e:
        st.error(f"Error: {e}")

