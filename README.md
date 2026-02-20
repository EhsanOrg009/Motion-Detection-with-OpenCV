# 🎥 Motion Detection with OpenCV

A simple yet effective motion detection system built using Python and OpenCV. This project captures frames from a webcam, detects motion using frame differencing, and saves images when motion is detected.

---

## 📌 Features

- Real-time motion detection using webcam
- Frame differencing algorithm
- Automatic image capture on motion detection
- Bounding box visualization around moving objects
- Saves captured images with timestamps
- Lightweight and beginner-friendly

---

## 🛠️ Technologies Used

- Python
- OpenCV (`cv2`)

---

## 🚀 How It Works

1. The webcam captures two consecutive frames.
2. The difference between frames is calculated.
3. The result is processed:
   - Converted to grayscale
   - Blurred to reduce noise
   - Threshold applied to detect motion areas
4. Contours are detected from the processed image.
5. If a contour exceeds a certain area threshold:
   - Motion is detected
   - A bounding box is drawn
   - The frame is saved as an image

---

## ⚙️ Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/motion-detection.git
cd motion-detection
```

---

```bash
pip install opencv-python
```
---

```bash
python main.py
```

---

## 📸 Output Example
- [INFO] Motion detected: motion_captures/motion_0_1700000000.jpg

---

## ❗ Notes
- Make sure your webcam is connected and accessible.
- Works best in stable lighting conditions.
- May produce false positives in noisy environments.

---
