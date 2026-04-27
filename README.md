# Smart Safety Monitoring System

## 📌 Overview

This project is a safety monitoring system designed to detect unauthorized human presence in restricted areas.

It combines motion-triggered logic with real-time visual detection to improve accuracy and reduce false alerts in monitoring environments.

---

## 🎯 Problem Statement

Traditional monitoring systems often generate false alerts due to:

* Environmental movement
* Continuous camera processing
* Lack of a validation mechanism

---

## 💡 Solution

This system uses a two-step validation approach:

* Motion detection trigger (simulated sensor)
* Human presence verification using visual detection

This ensures alerts are generated only for meaningful events.

---

## 🧠 System Architecture

```
Motion Trigger → Camera Capture → Human Detection → Alert API
```

---

## ⚙️ Features

* Real-time camera monitoring
* Motion-triggered processing
* Human presence detection
* Backend alert system using APIs
* Event-based logging for clarity

---

## 🛠️ Tech Stack

* Python
* OpenCV
* FastAPI
* NumPy

---

## 📂 Project Structure

```
smart-safety-ai/
│
├── app/
│   ├── main.py          # Main application controller
│   ├── detection.py     # Human detection logic
│   ├── sensor.py        # Motion trigger simulation
│   ├── alert.py         # Alert handler
│   ├── api.py           # Backend service
│
├── requirements.txt
├── README.md
```

---

## ▶️ How to Run

### 1. Install dependencies

```
pip install -r requirements.txt
```

### 2. Start backend service

```
uvicorn app.api:app --reload
```

### 3. Run the application

```
python app/main.py
```

---

## 📸 Sample Output

* ✅ NO ACTIVITY
* ⚠️ MOTION DETECTED
* 🚨 HUMAN DETECTED

(Add your screenshot here)

Example:

```
![Demo](Screenshot (497).png)
```

---

## 🚀 Future Enhancements

* Integration with real sensor hardware
* Cloud-based alert storage and monitoring
* Notification system (Email/SMS)
* Web dashboard for monitoring events
* Edge device deployment

---

## 🧠 Key Highlights

* Event-driven system design
* Efficient processing using trigger-based logic
* Real-time detection pipeline
* Backend integration using APIs

---

## 📌 Author

Kannan U
Senior Engineer | System Design & Monitoring Solutions

---

## 🔗 GitHub

(Add your GitHub profile link here)
