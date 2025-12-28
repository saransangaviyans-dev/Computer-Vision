# Facial Emotion Recognition

This project performs basic facial emotion recognition using a webcam.
It uses the `facial-emotion-recognition` Python module to detect emotions
from faces captured in real time.

## Description

The program captures video from the webcam, detects faces, and predicts
the facial emotion for each detected face using a pre-built library.

## Emotions

The detected emotions depend on the `facial-emotion-recognition` module
and may include emotions such as:

- Happy
- Sad
- Angry
- Neutral
- Surprised

## Technologies Used

- Python
- OpenCV
- facial-emotion-recognition module

## How It Works

1. Capture video using webcam
2. Detect face in each frame
3. Pass face to `facial-emotion-recognition` module
4. Display detected emotion on the screen

## How to Run

1. Install dependencies:

```bash
pip install -r requirements.txt
```
