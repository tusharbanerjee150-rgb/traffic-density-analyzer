# 🚦 Traffic Density Analyzer

## 📌 Overview

This project uses computer vision techniques to detect vehicles in a traffic video and classify traffic density as Low, Medium, or High.

## 🎯 Objective

To analyze traffic conditions by counting vehicles in real-time using OpenCV.

## ⚙️ Technologies Used

* Python
* OpenCV
* NumPy

## 🧠 Methodology

1. Load traffic video
2. Convert frames to grayscale
3. Detect vehicles using Haar Cascade
4. Count detected vehicles
5. Classify density based on count

## ▶️ How to Run

```bash
pip install -r requirements.txt
python src/main.py
```

## 📊 Output

* Detects vehicles using bounding boxes
* Displays number of cars
* Classifies traffic as:

  * Low
  * Medium
  * High

## 🚀 Future Scope

* Use YOLO for better accuracy
* Real-time camera integration
* Smart traffic signal control

## 👨‍💻 Author

Tushar Kumar Banerjee
25BAI10677
