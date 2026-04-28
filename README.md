# MoodTune 🎵
**Facial Expression Based Music Recommendation System**

Detects your facial expression via webcam using **DeepFace** and
recommends real-time YouTube music via the **YouTube Data API v3**.

---

## Architecture

```
Browser Webcam
     │  (base64 JPEG)
     ▼
Flask /api/detect  ──►  DeepFace  ──►  emotion scores + dominant mood
     │
     ▼
Flask /api/recommendations/<mood>  ──►  YouTube Data API v3  ──►  track list
     │
     ▼
Frontend  ──►  YouTube iframe player
```

---

## Setup

### 1. Clone / place project files
```
moodtune/
├── app.py
├── emotion_detector.py
├── requirements.txt
├── README.md
└── templates/
    └── index.html
```

### 2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```
> First run will auto-download DeepFace model weights (~100 MB).

### 4. Get a YouTube Data API v3 Key
1. Go to https://console.cloud.google.com/
2. Create a project → **Enable APIs** → search **YouTube Data API v3** → Enable
3. **Credentials** → **Create Credentials** → **API Key**
4. Copy the key

### 5. Set your API key
**Option A — Environment variable (recommended)**
```bash
export YOUTUBE_API_KEY="AIza..."          # Mac/Linux
set  YOUTUBE_API_KEY=AIza...              # Windows CMD
$env:YOUTUBE_API_KEY="AIza..."            # PowerShell
```

**Option B — Edit app.py directly**
```python
YOUTUBE_API_KEY = "AIza..."
```

### 6. Run the app
```bash
python app.py
```
Open your browser at **http://localhost:5000**

---

## API Endpoints

| Method | Route | Description |
|--------|-------|-------------|
| GET  | `/` | Web UI |
| POST | `/api/detect` | Detect emotion from base64 image |
| GET  | `/api/recommendations/<mood>` | Get YouTube tracks for mood |
| GET  | `/api/moods` | List all supported moods |

### POST /api/detect
**Request body:**
```json
{ "image": "data:image/jpeg;base64,/9j/..." }
```
**Response:**
```json
{
  "dominant": "happy",
  "face_found": true,
  "scores": {
    "angry": 0.12,
    "disgust": 0.03,
    "fear": 0.08,
    "happy": 92.45,
    "sad": 1.22,
    "surprise": 3.11,
    "neutral": 2.99
  }
}
```

### GET /api/recommendations/happy?count=8
**Response:**
```json
{
  "mood": "happy",
  "label": "Happy Vibes 😄",
  "query": "happy upbeat pop songs playlist 2024",
  "tracks": [
    {
      "id": "ZbZSe6N_BXs",
      "title": "Happy - Pharrell Williams",
      "channel": "PharrellWilliamsVEVO",
      "thumbnail": "https://i.ytimg.com/vi/.../mqdefault.jpg",
      "url": "https://www.youtube.com/watch?v=ZbZSe6N_BXs",
      "embed_url": "https://www.youtube.com/embed/ZbZSe6N_BXs?autoplay=1&rel=0"
    }
  ]
}
```

---

## Supported Moods → Music Queries

| Mood | Query |
|------|-------|
| 😄 happy | happy upbeat pop songs playlist 2024 |
| 😢 sad | sad emotional songs heartbreak playlist |
| 😠 angry | intense rock metal high energy playlist |
| 😰 fearful | calm soothing relaxing ambient music |
| 🤢 disgusted | alternative indie quirky music playlist |
| 😲 surprised | exciting electronic dance music EDM |
| 😐 neutral | chill lofi hip hop study beats |

---

## Customising Mood Queries
Edit `MOOD_QUERIES` in `app.py`:
```python
MOOD_QUERIES = {
    "happy": "your custom search query here",
    ...
}
```

## Tech Stack
- **Backend:** Python · Flask · DeepFace · OpenCV
- **AI Model:** DeepFace (VGG-Face / retinaface detector)
- **Music API:** YouTube Data API v3
- **Frontend:** Vanilla JS · YouTube IFrame API

## Future Scope
🔹 v1.0 – Current System (Baseline)
✅ What you already built
Real-time emotion detection (DeepFace)

Mood classification

YouTube-based music recommendation

Interactive UI with playback

🔹 v1.1 – UX & Automation Upgrade
🎯 Goal: Make system smoother & smarter
🔄 Auto emotion detection (every 2–3 sec)

🎵 Auto-play first recommended song

🎬 “Now Playing” UI (title, thumbnail)

⏳ Loading indicators (Detecting mood…)

💬 Dynamic mood messages (human-like feedback)

🔹 v1.2 – Intelligence Improvement
🎯 Goal: Improve accuracy & stability
🧠 Emotion smoothing (average last N frames)

🔄 Mood transition detection (real-time updates)

🎯 Better mood mapping logic

⚡ Reduce “neutral bias”

🔹 v2.0 – Personalization System
🎯 Goal: Make it user-aware
🗂️ Store mood history (SQLite/JSON)

📊 Track:

mood

time

selected songs

🎯 Personalized recommendations:

mood + time + past behavior

👉 Now it becomes adaptive system

🔹 v2.1 – Analytics Dashboard
🎯 Goal: Add Data Science layer
📈 Mood trend graphs

📊 Emotion distribution chart

🎵 Most played genres

📅 Daily/weekly insights

👉 Strong DS + ML signal for recruiters

🔹 v3.0 – Context-Aware AI System
🎯 Goal: Add deeper intelligence
🕒 Context-based recommendations:

Morning → energetic

Night → calm

📚 Activity-based mode:

Study → focus music

Workout → high BPM

🔹 v3.5 – Multi-Modal Emotion Detection
🎯 Goal: Improve AI depth
🎤 Voice-based emotion detection

👁️ Facial + voice combined analysis

🧠 More accurate mood inference

🔹 v4.0 – Agentic AI Integration (🔥 IMPORTANT)
🎯 Goal: Turn system into AI agent, not just model
🤖 What is Agentic AI here?
Instead of:

Detect → Recommend

Agent will:

Observe → Think → Decide → Act → Learn

🧠 Features to Add
1. 🎯 Intelligent Decision Agent
Takes input:

mood

history

time

Decides:

what type of music to play

when to change it

2. 🔄 Continuous Learning Agent
Learns from:

skipped songs

played songs

Improves recommendations over time

3. 💬 Conversational AI Agent (MoodTune Bot)
Chat interface:

“I feel low”

“Play something relaxing”

Responds with:

music + suggestions

4. 🧠 Goal-Oriented Behavior
Agent can:

Improve mood intentionally

Suggest transitions:

Sad → Calm → Happy

5. 🔁 Feedback Loop System

User Emotion → Agent Analysis → Music Recommendation → User Reaction → Learning → Improved Decision
6. 🧩 Tech to Use for Agentic AI
Python + Flask (backend)

Simple rule-based agent (start)

Later upgrade:

LangChain

OpenAI API

Memory modules

🔹 v5.0 – Deployment & Productization
🎯 Goal: Real-world system
☁️ Deploy on cloud (Render / Railway)

📱 Mobile-friendly UI

🔐 Secure API handling (.env)

👥 Multi-user support (login system)



