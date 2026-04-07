# 🧠 See Through AI – Assistive Vision System

## 🚀 Overview
See Through AI is a real-time AI-powered assistive vision system designed to help visually impaired individuals understand their surroundings using a webcam. It uses computer vision and YOLO-based object detection to identify objects in real time and provide audio feedback.

## 🎯 Features
- Real-time object detection using webcam
- YOLO-based object recognition
- Audio feedback using Text-to-Speech
- Multi-object detection support
- Basic distance estimation (if implemented)
- Lightweight and real-time processing

## 🛠️ Tech Stack
- Python
- OpenCV
- YOLO (Ultralytics / Custom Model)
- PyTorch / TensorFlow
- NumPy
- pyttsx3 / gTTS

## 📁 Project Structure
See-Through-AI/
├── models/              # YOLO weights / trained models
├── utils/               # Helper functions
├── main.py              # Main entry point
├── detect.py            # Object detection logic
├── voice.py             # Text-to-speech module
├── requirements.txt     # Dependencies
└── README.md

## ⚙️ Installation
git clone https://github.com/avishka8/See-Through-AI.git  
cd See-Through-AI  
pip install -r requirements.txt  

## ▶️ How to Run
python main.py  

Make sure webcam is connected and YOLO weights are placed inside the models/ folder.

## 🧠 Working
1. Capture live video from webcam  
2. Frames are passed into YOLO model  
3. Objects are detected in real time  
4. Labels are converted into speech  
5. Audio feedback is given to user  

## ⚠️ Limitations
- Accuracy depends on dataset quality  
- Misclassification possible in complex scenes  
- Requires better training for real-world use  
- GPU recommended for smooth performance  

## 🔮 Future Improvements
- Better dataset training  
- Depth estimation for distance detection  
- Transformer-based vision models  
- Mobile app deployment  
- Edge device optimization  

## 👨‍💻 Author
Avishka S  
VIT Bhopal
