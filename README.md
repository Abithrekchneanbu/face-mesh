Face Mesh — Real-time 3D Face Landmark Detection

Real-time **468-point face mesh** detection using **MediaPipe** and **OpenCV** in Python.
Detects facial landmarks live from your webcam — runs entirely on CPU!


Demo

Run the project to see real-time green face mesh overlay on your webcam feed.



Features

468 3D facial landmark detection
Real-time webcam feed
Lightweight — runs on CPU only
Works on Windows, Mac, Linux
Auto-downloads the model on first run (~1MB)


Tech Stack

| Tool | Purpose |
|------|---------|
| [MediaPipe](https://mediapipe.dev/) | Face landmark detection model |
| [OpenCV](https://opencv.org/) | Webcam capture & drawing |
| Python 3.11 | Core language |


Installation

1.Clone the repository
bash
git clone https://github.com/Abithrekchneanbu/face-mesh.git
cd face-mesh


2.Create virtual environment
bash
Windows
python -m venv venv
venv\Scripts\activate

Mac/Linux
python3 -m venv venv
source venv/bin/activate


3.Install dependencies
bash
pip install -r requirements.txt


4.Run
bash
python face.py


The model file `face_landmarker.task` (~1MB) will be downloaded automatically on first run.



Controls

| Key | Action |
|-----|--------|
| `Q` | Quit the application |



Project Structure
