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
