"""
emotion_detector.py
Detects facial expressions from webcam using DeepFace.
Returns a dict of emotion probabilities.
"""

import cv2
import numpy as np
from deepface import DeepFace


def detect_from_frame(frame: np.ndarray) -> dict:
    """
    Analyze a single BGR frame and return emotion scores.

    Returns:
        {
          "dominant": "happy",
          "scores": { "happy": 92.3, "sad": 1.2, ... },
          "face_found": True
        }
    """
    try:
        result = DeepFace.analyze(
            frame,
            actions=["emotion"],
            enforce_detection=True,
            silent=True,
        )
        emotions = result[0]["emotion"]          # raw % scores
        dominant = result[0]["dominant_emotion"]
        return {"dominant": dominant, "scores": emotions, "face_found": True}
    except Exception:
        return {"dominant": "neutral", "scores": {}, "face_found": False}


def detect_from_webcam(camera_index: int = 0) -> dict:
    """
    Capture one frame from the webcam and return emotion scores.
    Useful for single-shot detection called from the API route.
    """
    cap = cv2.VideoCapture(camera_index)
    if not cap.isOpened():
        return {"dominant": "neutral", "scores": {}, "face_found": False, "error": "Camera not accessible"}

    ret, frame = cap.read()
    cap.release()

    if not ret:
        return {"dominant": "neutral", "scores": {}, "face_found": False, "error": "Could not read frame"}

    return detect_from_frame(frame)


def live_detection_loop(camera_index: int = 0, on_emotion=None):
    """
    Continuous webcam loop.  Calls on_emotion(result_dict) each time
    a face is analyzed.  Press 'q' to quit.

    on_emotion: callable(dict) — receives the result from detect_from_frame()
    """
    cap = cv2.VideoCapture(camera_index)
    if not cap.isOpened():
        print("Error: could not open camera.")
        return

    print("Starting live detection — press Q to quit.")
    frame_skip = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame_skip += 1
        if frame_skip % 15 == 0:           # analyze every 15th frame (~2 fps)
            result = detect_from_frame(frame)
            if on_emotion:
                on_emotion(result)

            # Overlay dominant emotion on frame
            label = result["dominant"].upper()
            cv2.putText(frame, label, (20, 40),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.2, (124, 110, 247), 2)

        cv2.imshow("MoodTune — Face Detection", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    # Quick test: snap one frame and print result
    result = detect_from_webcam()
    print("Detected emotion:", result)
