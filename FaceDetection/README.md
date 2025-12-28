# Face Detection using OpenCV

This project performs real-time face detection using a webcam and the Haar Cascade algorithm provided by OpenCV.

## Workflow

1. Load Haar Cascade face detection model
2. Initialize the camera
3. Read frames from the webcam
4. Convert color image to grayscale
5. Detect faces using Haar Cascade
6. Draw bounding boxes around detected faces
7. Display output in real time

## Features

- Real-time face detection
- Haar Cascade classifier
- Bounding box on detected faces
- ESC key to exit

## Technologies Used

- Python
- OpenCV (cv2)

## Files

- `faceDetection.py` – main Python script
- `haarcascade_frontalface_default.xml` – face detection model

## How to Run

1. Install dependencies:

```bash
pip install -r requirements.txt
```
