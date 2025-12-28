# Colored Object Detection using OpenCV (HSV)

This project demonstrates real-time colored object detection using a webcam and OpenCV.  
HSV (Hue, Saturation, Value) color space is used for accurate color filtering.

---

## 📌 Features

- Live webcam feed
- HSV color range tuning using trackbars
- Detects a specific colored object
- Draws circle and center point on detected object
- Prints object movement direction (Left, Right, Front, Stop)

---

## 🧠 How It Works

1. Webcam captures live video
2. Frame is converted from BGR to HSV
3. A color mask is created using HSV range
4. Morphological operations reduce noise
5. Contours are detected
6. The largest contour is tracked as the object

---

## 📂 Files Explanation

- `hsv.py`  
  Used to find correct HSV values using trackbars.

- `ColoredObjectDetection.py`  
  Uses the selected HSV values to detect and track the object.

---

## ⚙️ Requirements

- Python 3.8+
- OpenCV
- NumPy
- imutils

Install dependencies using:

```bash
pip install -r requirements.txt
```
