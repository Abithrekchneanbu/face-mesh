<div align="center">

<!-- Animated Title -->
<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=35&duration=3000&pause=1000&color=00FF41&center=true&vCenter=true&width=600&lines=🎭+Face+Mesh+Detection;468+Facial+Landmarks;Real-time+Webcam+AI;MediaPipe+%2B+OpenCV" alt="Typing SVG" />

<br/>

<!-- Badges -->
![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python&logoColor=white)
![MediaPipe](https://img.shields.io/badge/MediaPipe-0.10.35-green?style=for-the-badge&logo=google&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-4.13-red?style=for-the-badge&logo=opencv&logoColor=white)
![Platform](https://img.shields.io/badge/Platform-Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

<br/>

<!-- Animated divider -->
<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%">

</div>
</div>

<div align="center">
<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%">

## 🌟 What is Face Mesh?

<div align="center">
</div>

---

<div align="center">
<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=22&duration=2000&pause=500&color=FF6B6B&center=true&vCenter=true&width=500&lines=✨+Features" alt="Features"/>
</div>

## ✨ Features

<div align="center">

| Feature | Description |
|---------|-------------|
| 🟢 468 Landmarks | Full 3D facial landmark detection |
| 📷 Real-time | Live webcam feed processing |
| ⚡ CPU Only | No GPU required |
| 🖥️ Cross Platform | Windows, Mac, Linux |
| 📦 Auto Download | AI model downloads on first run |
| 🎯 High Accuracy | MediaPipe Tasks API |

</div>

<div align="center">
<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%">
</div>

---

<div align="center">
<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=22&duration=2000&pause=500&color=FFD700&center=true&vCenter=true&width=500&lines=⚙️+Installation" alt="Install"/>
</div>

## ⚙️ Installation

### 1️⃣ Clone the repo
```bash
git clone https://github.com/Abithrekchneanbu/face-mesh.git
cd face-mesh
```

### 2️⃣ Create virtual environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac / Linux
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Run the project 🚀
```bash
python face.py
```

> 💡 Model file `face_landmarker.task` (~1MB) downloads automatically on first run!

<div align="center">
<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%">
</div>

---

<div align="center">
<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=22&duration=2000&pause=500&color=00BFFF&center=true&vCenter=true&width=500&lines=🚀+How+It+Works" alt="How"/>
</div>

## 🚀 How It Works

```mermaid
graph TD
    A[📷 Webcam captures frame] --> B[🔄 Flip and convert to RGB]
    B --> C[🤖 MediaPipe processes frame]
    C --> D{Face detected?}
    D -->|Yes| E[📍 Extract 468 landmarks]
    D -->|No| F[⏭️ Skip frame]
    E --> G[🎨 Draw mesh on frame]
    G --> H[🖥️ Display in window]
    H --> A
```

<div align="center">
<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%">
</div>

---

<div align="center">
<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=22&duration=2000&pause=500&color=FF00FF&center=true&vCenter=true&width=500&lines=🛠️+Tech+Stack" alt="Tech"/>
</div>

## 🛠️ Tech Stack

<div align="center">

| Tool | Version | Purpose |
|------|---------|---------|
| 🐍 Python | 3.11 | Core language |
| 🤖 MediaPipe | 0.10.35 | AI face landmark model |
| 👁️ OpenCV | 4.13 | Webcam and drawing |
| 🔢 NumPy | Latest | Array processing |

</div>

<div align="center">
<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%">
</div>

---

<div align="center">
<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=22&duration=2000&pause=500&color=FFA500&center=true&vCenter=true&width=500&lines=📁+Project+Structure" alt="Structure"/>
</div>

## 📁 Project Structure

---


