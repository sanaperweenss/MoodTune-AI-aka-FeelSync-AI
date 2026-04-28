# MoodTune-AI-aka-FeelSync-AI
# 🎧 MoodTune-AI  
### AI-Powered Emotion-Based Music Recommendation System
MoodTune-AI is a real-time AI application that detects user emotions through facial expressions and dynamically recommends music using the YouTube API.

---

## 🚀 Features

- 🎥 Real-time face detection using webcam  
- 🧠 Emotion detection using DeepFace (AI/ML)  
- 🎯 Mood-based music recommendation  
- 🎵 YouTube API integration for song suggestions  
- ▶️ Interactive UI with playable music  
- ⚡ Instant emotion-to-music pipeline  

---

## 🧠 How It Works

1. Webcam captures user face  
2. DeepFace analyzes facial expressions  
3. Emotion is detected (Happy, Sad, Neutral, etc.)  
4. Emotion is mapped to a mood  
5. Mood is converted into a search query  
6. YouTube API fetches relevant songs  
7. User selects and plays music  

---

## 🛠️ Tech Stack

- **Frontend:** HTML, CSS, JavaScript  
- **Backend:** Flask (Python)  
- **AI/ML:** DeepFace, TensorFlow  
- **Computer Vision:** OpenCV  
- **API:** YouTube Data API v3  

---

## 📂 Project Structure

🚀 📌 Future Scope Roadmap (Version-wise)
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
