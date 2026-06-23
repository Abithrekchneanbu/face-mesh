<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0d0d0d,50:00FF41,100:0d0d0d&height=220&section=header&text=🎭%20Face%20Mesh%20Detection&fontSize=52&fontColor=00FF41&animation=fadeIn&fontAlignY=38&desc=Real-time%20468%20Facial%20Landmarks%20%7C%20MediaPipe%20%2B%20OpenCV%20%7C%20Python%203.11&descAlignY=58&descSize=16&descColor=ffffff" width="100%"/>

<br/>

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=700&size=22&duration=2500&pause=800&color=00FF41&center=true&vCenter=true&multiline=false&width=700&lines=👋+Hey+there!+Welcome+to+Face+Mesh+Detection;🎭+I+built+this+from+scratch+using+MediaPipe+AI;🟢+Detects+468+facial+landmarks+in+real-time;📷+All+you+need+is+a+webcam+and+Python+3.11;⚡+Runs+on+CPU+—+no+expensive+GPU+needed;🚀+Clone+it%2C+run+it%2C+see+your+face+mapped!" alt="Typing SVG" />

<br/><br/>

![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)
![MediaPipe](https://img.shields.io/badge/MediaPipe-0.10.35-00C853?style=for-the-badge&logo=google&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-4.13-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)
![Windows](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)
![MIT License](https://img.shields.io/badge/License-MIT-F7DF1E?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-00FF41?style=for-the-badge)
![Made With Love](https://img.shields.io/badge/Made%20with-❤️-ff69b4?style=for-the-badge)

<br/>

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%">

</div>

---

## 👋 Hey, I'm Abithrekchneanbu!

I'm a developer who loves building cool computer vision projects. This is one of my favorite builds — a **real-time face mesh detector** that maps **468 points** on your face live from your webcam. No fancy hardware needed, just Python and a camera!

I built this because I wanted to understand how modern facial AR filters work under the hood — the kind you see in Snapchat, Instagram, and TikTok. Turns out, it's all about these 468 landmark points!

> *"The best way to learn computer vision is to build something you can literally see working in real time."*

<div align="center">
<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%">
</div>

---

<div align="center">
<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=26&duration=2000&pause=500&color=00FF41&center=true&vCenter=true&width=600&lines=🌟+What+Does+This+Project+Do%3F" alt="What"/>
</div>

<br/>

<table>
<tr>
<td width="55%">

### 🧠 The Idea

When you open this project and point your webcam at your face, the AI instantly starts mapping **468 unique points** across your entire face — your eyes, nose, lips, cheeks, forehead, and jaw. All in real-time!

These 468 points form a **triangular mesh** (like a 3D net) draped over your face. Every single frame, the model re-detects and re-draws all of them — at smooth speed, on just your CPU.

### 🎯 Why 468 Points?

Google's MediaPipe team trained a neural network on millions of faces to identify exactly these 468 key positions. Each point corresponds to a specific facial feature. For example:
- Points `33` and `263` are your eye corners
- Points `61` and `291` are your lip corners  
- Point `4` is the tip of your nose
- Points `10` and `152` are top and bottom of your face

</td>
<td width="45%">
</td>
</tr>
</table>

<div align="center">
<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%">
</div>

---

<div align="center">
<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=26&duration=2000&pause=500&color=FF6B6B&center=true&vCenter=true&width=600&lines=✨+Features" alt="Features"/>
</div>

<br/>

<div align="center">

|  | Feature | What It Means |
|--|---------|--------------|
| 🟢 | **468 Facial Landmarks** | Every frame, 468 points are detected and drawn on your face |
| 📷 | **Real-time Webcam** | Live video feed processed frame by frame |
| ⚡ | **CPU Only** | No GPU needed — runs on any modern laptop |
| 🖥️ | **Cross Platform** | Works on Windows, Mac, and Linux |
| 📦 | **Auto Model Download** | AI model (~1MB) downloads itself on first run |
| 🎯 | **MediaPipe Tasks API** | Uses Google's latest and most accurate API |
| 🔒 | **100% Local** | Nothing sent to internet — everything runs on your machine |
| 🎨 | **Visual Mesh** | Green dots + connecting lines drawn over your face |
| 🔄 | **Auto Flip** | Webcam is mirrored so it feels natural like a selfie |
| 🛡️ | **Error Handling** | Dropped frames are skipped gracefully, no crashes |

</div>

<div align="center">
<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%">
</div>

---

<div align="center">
<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=26&duration=2000&pause=500&color=FFD700&center=true&vCenter=true&width=600&lines=⚙️+Getting+Started" alt="Install"/>
</div>

<br/>

> ✅ **Requirement:** Python 3.11 only. MediaPipe does NOT work on Python 3.12 or above.

### 1️⃣ Clone the repository

```bash
git clone https://github.com/Abithrekchneanbu/face-mesh.git
cd face-mesh
```

### 2️⃣ Create a virtual environment

This keeps your project dependencies separate and clean.

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac / Linux
python3 -m venv venv
source venv/bin/activate
```

You should see `(venv)` appear at the start of your terminal line. That means you're inside the virtual environment.

### 3️⃣ Install all dependencies

```bash
pip install -r requirements.txt
```

This installs MediaPipe, OpenCV, and NumPy automatically.

### 4️⃣ Run it!

```bash
python face.py
```

A window will open showing your webcam. Point it at your face and watch the green mesh appear! Press `Q` to quit.

> 💡 **First run only:** The model file `face_landmarker.task` (~1MB) will download automatically. This only happens once!

<div align="center">
<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%">
</div>

---

<div align="center">
<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=26&duration=2000&pause=500&color=00BFFF&center=true&vCenter=true&width=600&lines=🚀+How+It+Works+Under+the+Hood" alt="How"/>
</div>

<br/>

```mermaid
graph TD
    A[🎬 Start face.py] --> B[📥 Download model if not present]
    B --> C[📷 Open webcam with OpenCV]
    C --> D[🔄 Capture frame]
    D --> E[🔀 Flip frame horizontally]
    E --> F[🎨 Convert BGR to RGB]
    F --> G[🤖 Pass to MediaPipe Face Landmarker]
    G --> H{👤 Face detected?}
    H -->|✅ YES| I[📍 Get 468 landmark coordinates]
    H -->|❌ NO| D
    I --> J[🔗 Draw mesh connections]
    J --> K[🟢 Draw landmark dots]
    K --> L[🖥️ Show frame in window]
    L --> M{⌨️ Q pressed?}
    M -->|No| D
    M -->|Yes| N[🛑 Release camera and exit]

    style A fill:#0d0d0d,color:#00FF41,stroke:#00FF41
    style G fill:#0d0d0d,color:#00BFFF,stroke:#00BFFF
    style H fill:#0d0d0d,color:#FFD700,stroke:#FFD700
    style N fill:#0d0d0d,color:#FF4444,stroke:#FF4444
```

<br/>

### 🧪 The AI Pipeline Explained

The magic happens in just a few steps:

**Step 1 — Face Detection**
MediaPipe first runs a fast face detector on the full image to find where your face is. This is the same BlazeFace model used in Google products.

**Step 2 — Landmark Prediction**
Once your face is located, a second neural network zooms into that region and predicts the exact 3D coordinates of all 468 points.

**Step 3 — Tracking**
Instead of running the detector every frame (slow), MediaPipe tracks your face from the previous frame and only re-detects when it loses track. This is what makes it real-time fast!

**Step 4 — Drawing**
OpenCV takes those 468 coordinate pairs and draws green circles at each point, then connects them with lines to form the visible mesh.

<div align="center">
<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%">
</div>

---

<div align="center">
<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=26&duration=2000&pause=500&color=FF00FF&center=true&vCenter=true&width=600&lines=🛠️+Tech+Stack" alt="Tech"/>
</div>

<br/>

<div align="center">
<img src="https://skillicons.dev/icons?i=python,opencv,vscode,git,github&theme=dark" />
</div>

<br/>

<div align="center">

| Tool | Version | Why I Used It |
|------|---------|--------------|
| 🐍 **Python** | 3.11 | Best compatibility with MediaPipe |
| 🤖 **MediaPipe** | 0.10.35 | Google's AI model for face landmark detection |
| 👁️ **OpenCV** | 4.13 | Industry standard for webcam and image processing |
| 🔢 **NumPy** | Latest | Fast array operations for image data |
| 💻 **VS Code** | Latest | My code editor of choice |

</div>

<div align="center">
<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%">
</div>

---

<div align="center">
<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=26&duration=2000&pause=500&color=FFA500&center=true&vCenter=true&width=600&lines=📁+Project+Structure" alt="Structure"/>
</div>

<br/>
> 📌 Note: `face_landmarker.task` is auto-downloaded at runtime and excluded from the repo via `.gitignore` to keep the repo lightweight.

<div align="center">
<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%">
</div>

---

<div align="center">
<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=26&duration=2000&pause=500&color=00FF88&center=true&vCenter=true&width=600&lines=🎮+Controls" alt="Controls"/>
</div>

<br/>

<div align="center">

| Key | Action |
|:---:|--------|
| `Q` | ❌ Quit and close the window |

</div>

> 💡 Just press `Q` while the webcam window is focused to exit cleanly.

<div align="center">
<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%">
</div>

---

<div align="center">
<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=26&duration=2000&pause=500&color=FF6B6B&center=true&vCenter=true&width=600&lines=💡+What+Can+You+Build+With+This%3F" alt="Ideas"/>
</div>

<br/>

This project is a **foundation** — once you have 468 landmark points, you can build almost anything:

<div align="center">

| Project Idea | What You Need |
|-------------|--------------|
| 😴 **Drowsiness Detector** | Track eye landmarks — detect if eyes are closing |
| 💄 **Virtual Makeup** | Overlay colors on lip/cheek landmarks |
| 😊 **Emotion Detector** | Analyze mouth/eyebrow positions |
| 🕶️ **AR Glasses Filter** | Place 3D glasses on eye landmarks |
| 🎭 **Face Swap** | Map one face mesh onto another |
| 🖱️ **Head Pose Mouse** | Control mouse by tilting your head |
| 🎤 **Lip Sync Detector** | Detect when mouth is open/closed |
| 🏋️ **Face Exercise App** | Count facial exercises using landmark movement |

</div>

<div align="center">
<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%">
</div>

---

<div align="center">
<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=26&duration=2000&pause=500&color=FF4444&center=true&vCenter=true&width=600&lines=⚠️+Troubleshooting" alt="Trouble"/>
</div>

<br/>

<details>
<summary>📷 &nbsp;<b>Camera not found / No camera error</b></summary>
<br>

On Windows, OpenCV sometimes can't access the camera by default. Use the Windows Media Foundation backend:

```python
# In face.py, change this line:
cap = cv2.VideoCapture(0, cv2.CAP_MSMF)
```

If camera index 0 doesn't work, try index 1:
```python
cap = cv2.VideoCapture(1, cv2.CAP_MSMF)
```
</details>

<details>
<summary>❌ &nbsp;<b>AttributeError: module 'mediapipe' has no attribute 'solutions'</b></summary>
<br>

This happens because newer MediaPipe removed the old `solutions` API. This project uses the new **Tasks API**. Make sure you have the right version:

```bash
pip uninstall mediapipe -y
pip install mediapipe==0.10.35
```
</details>

<details>
<summary>🔒 &nbsp;<b>Camera access denied / permission error</b></summary>
<br>

Windows blocks camera access by default for desktop apps. Fix it here:
Windows Settings

→ Privacy & Security

→ Camera

→ ✅ Camera access → ON

→ ✅ Let apps access your camera → ON

→ ✅ Let desktop apps access your camera → ON


<summary>🐌 &nbsp;<b>Laggy or very low FPS</b></summary>
<br>

Lower the webcam resolution in `face.py`:
```python
cap.set(3, 640)   # width
cap.set(4, 480)   # height
```
Also make sure no other app (Zoom, Teams, OBS) is using your camera at the same time.
</details>

<details>
<summary>⬇️ &nbsp;<b>Model download is very slow or fails</b></summary>
<br>

The model file `face_landmarker.task` is only ~1MB and downloads once. If it fails, you can manually download it from:
https://storage.googleapis.com/mediapipe-models/face_landmarker/face_landmarker/float16/1/face_landmarker.task

Place it in the same folder as `face.py` and it won't try to download again.
</details>

<details>
<summary>🪟 &nbsp;<b>Window opens but shows black screen</b></summary>
<br>

Your camera might need a moment to warm up. Wait 2-3 seconds. If still black, try changing the backend:
```python
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
```
</details>

<div align="center">
<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%">
</div>

---

<div align="center">
<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=26&duration=2000&pause=500&color=00BFFF&center=true&vCenter=true&width=600&lines=🤝+Contributing" alt="Contribute"/>
</div>

<br/>

Contributions are welcome! If you want to improve this project:

1. 🍴 **Fork** this repo
2. 🌿 **Create** a new branch: `git checkout -b feature/your-feature`
3. ✏️ **Make** your changes
4. 💾 **Commit:** `git commit -m "Add your feature"`
5. 📤 **Push:** `git push origin feature/your-feature`
6. 🔃 **Open** a Pull Request

### 💡 Ideas for contribution
- Add FPS counter on screen
- Add multiple face detection support
- Add face landmark index labels
- Add face distance estimation
- Add screenshot save feature with `S` key

<div align="center">
<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%">
</div>

---

<div align="center">
<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=26&duration=2000&pause=500&color=FFD700&center=true&vCenter=true&width=600&lines=📜+License" alt="License"/>
</div>

<br/>

This project is licensed under the **MIT License** — feel free to use it, modify it, and build on top of it. Just give credit! 🙏

<div align="center">
<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%">
</div>

---

<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=700&size=20&duration=2000&pause=1000&color=00FF41&center=true&vCenter=true&width=700&lines=Thanks+for+checking+out+Face+Mesh+Detection!;If+this+helped+you%2C+drop+a+⭐+on+the+repo!;Built+with+❤️+by+Abithrekchneanbu;Happy+coding+and+keep+building+cool+stuff+🚀" alt="Footer Typing"/>

<br/><br/>

[![GitHub stars](https://img.shields.io/github/stars/Abithrekchneanbu/face-mesh?style=social)](https://github.com/Abithrekchneanbu/face-mesh/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/Abithrekchneanbu/face-mesh?style=social)](https://github.com/Abithrekchneanbu/face-mesh/network)
[![GitHub watchers](https://img.shields.io/github/watchers/Abithrekchneanbu/face-mesh?style=social)](https://github.com/Abithrekchneanbu/face-mesh)
[![GitHub followers](https://img.shields.io/github/followers/Abithrekchneanbu?style=social)](https://github.com/Abithrekchneanbu)

<br/>

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0d0d0d,50:00FF41,100:0d0d0d&height=120&section=footer" width="100%"/>

</div>
