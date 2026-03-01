# ✋ Touchless Gesture Controller using Vision Agents

## 🚀 Project Overview
Touchless Gesture Controller is a real-time AI-based human–computer interaction system that allows users to control actions using hand gestures without physical contact.

The system captures live webcam input, detects hand gestures, and converts them into commands such as **Pause**, **Accept**, and **Next**. This demonstrates how Vision AI and real-time agents can enable natural, touch-free interaction.

---

## 🎯 Features
- Real-time hand tracking using webcam
- Gesture recognition using computer vision
- Touchless command execution
- Live command display on screen
- Low-latency interaction pipeline

---

## 🧠 Tech Stack
- **Vision Agents SDK** – real-time agent infrastructure
- **Stream Video API** – low latency video interaction
- **Gemini API** – AI agent integration
- **MediaPipe** – hand landmark detection
- **OpenCV** – video processing
- **Python**

---

## 🏗️ Architecture
1. Webcam captures live video frames.
2. MediaPipe detects hand landmarks.
3. Gesture logic interprets finger positions.
4. Commands are generated from gestures.
5. Results displayed in real time.

---

## ✋ Supported Gestures
| Gesture | Command |
|---|---|
| Open Palm | PAUSE |
| One Finger / Thumbs Up | ACCEPT |
| Two Fingers | NEXT |

---

## ▶️ How to Run

```bash
git clone https://github.com/its-sanskriti/touchless-gesture-controller.git
cd vision-agent-demo
python examples/gesture_agent/gesture_controller.py

