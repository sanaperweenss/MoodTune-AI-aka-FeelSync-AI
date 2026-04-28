"""
MoodTune - Facial Express
ion Based Music Recommendation System
Flask backend with YouTube Data API v3 integration
"""

from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
import googleapiclient.discovery
import base64
import numpy as np
import cv2
import os

from emotion_detector import detect_from_frame, detect_from_webcam

app = Flask(__name__)
CORS(app)

# ── YouTube API setup ────────────────────────────────────────────────────────
YOUTUBE_API_KEY\
    = os.environ.get("YOUTUBE_API_KEY", "AIzaSyAZ2uS0AneWP13CZ3g4UvnHKJVe5seZxr8")

MOOD_QUERIES = {
    "happy":     "happy upbeat pop songs playlist 2024",
    "sad":       "sad emotional songs heartbreak playlist",
    "angry":     "intense rock metal high energy playlist",
    "fearful":   "calm soothing relaxing ambient music",
    "disgusted": "alternative indie quirky music playlist",
    "surprised": "exciting electronic dance music EDM",
    "neutral":   "chill lofi hip hop study beats",
}

MOOD_LABELS = {
    "happy":     "Happy Vibes 😄",
    "sad":       "Melancholic 😢",
    "angry":     "Intense Mode 😠",
    "fearful":   "Calm & Ease 😰",
    "disgusted": "Eclectic Mix 🤢",
    "surprised": "Surprise Drop 😲",
    "neutral":   "Chill Zone 😐",
}


def get_youtube_client():
    return googleapiclient.discovery.build(
        "youtube", "v3", developerKey=YOUTUBE_API_KEY
    )


def search_youtube(mood: str, max_results: int = 8):
    """Search YouTube for tracks matching the detected mood."""
    query = MOOD_QUERIES.get(mood, MOOD_QUERIES["neutral"])
    try:
        yt = get_youtube_client()
        response = (
            yt.search()
            .list(
                part="snippet",
                q=query,
                type="video",
                videoCategoryId="10",   # Music category
                maxResults=max_results,
                order="relevance",
                safeSearch="moderate",
            )
            .execute()
        )

        tracks = []
        for item in response.get("items", []):
            vid_id = item["id"]["videoId"]
            snippet = item["snippet"]
            tracks.append({
                "id":        vid_id,
                "title":     snippet["title"],
                "channel":   snippet["channelTitle"],
                "thumbnail": snippet["thumbnails"].get("medium", {}).get("url", ""),
                "published": snippet.get("publishedAt", "")[:10],
                "url":       f"https://www.youtube.com/watch?v={vid_id}",
                "embed_url": f"https://www.youtube.com/embed/{vid_id}?autoplay=1&rel=0",
            })
        return tracks

    except Exception as e:
        print(f"YouTube API error: {e}")
        return []


# ── Routes ───────────────────────────────────────────────────────────────────

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/detect", methods=["POST"])
def detect_emotion():
    """
    Accepts a base64-encoded JPEG image from the browser webcam
    and returns DeepFace emotion scores.
    Body JSON: { "image": "<base64 data-url>" }
    """
    data = request.get_json(force=True)
    b64 = data.get("image", "")
    if not b64:
        result = detect_from_webcam()
        return jsonify(result)
    try:
        img_bytes = base64.b64decode(b64.split(",")[-1])
        arr = np.frombuffer(img_bytes, dtype=np.uint8)
        frame = cv2.imdecode(arr, cv2.IMREAD_COLOR)
        result = detect_from_frame(frame)
    except Exception as e:
        result = {"dominant": "neutral", "scores": {}, "face_found": False, "error": str(e)}
    return jsonify(result)


@app.route("/api/recommendations/<mood>")
def recommendations(mood: str):
    """Return YouTube track recommendations for a given mood."""
    mood = mood.lower().strip()
    if mood not in MOOD_QUERIES:
        mood = "neutral"

    count = min(int(request.args.get("count", 8)), 15)
    tracks = search_youtube(mood, count)

    return jsonify({
        "mood":   mood,
        "label":  MOOD_LABELS.get(mood, ""),
        "query":  MOOD_QUERIES.get(mood, ""),
        "tracks": tracks,
    })


@app.route("/api/moods")
def moods():
    """List all supported moods."""
    return jsonify(list(MOOD_QUERIES.keys()))


if __name__ == "__main__":
    app.run(debug=True, port=5000)
