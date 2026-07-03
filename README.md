<div align="center">

# 🐶🐱 AI Pet Classifier
### Deep Learning Image Classification using TensorFlow, CNN & Streamlit

<p align="center">
<img src="https://img.shields.io/badge/Python-3.11-blue?logo=python">
<img src="https://img.shields.io/badge/TensorFlow-2.x-orange?logo=tensorflow">
<img src="https://img.shields.io/badge/Keras-Deep%20Learning-red?logo=keras">
<img src="https://img.shields.io/badge/Streamlit-Deployed-ff4b4b?logo=streamlit">
<img src="https://img.shields.io/badge/HuggingFace-Model-yellow?logo=huggingface">
<img src="https://img.shields.io/badge/License-MIT-green">
<img src="https://img.shields.io/badge/Open%20Source-❤-success">
</p>

### 🚀 A Convolutional Neural Network (CNN) powered web application that classifies images into **Cat 🐱** or **Dog 🐶** with confidence scores.

---

## 🌐 Live Demo

### 🚀 Streamlit App
**https://YOUR-STREAMLIT-APP.streamlit.app**

### 🤗 Hugging Face Model
**https://huggingface.co/Sudheer17/AI_Pet_Classifier**

---

## 📑 Table of Contents

- Project Overview
- Features
- Demo
- Architecture
- Project Workflow
- Folder Structure
- Technologies
- Dataset
- Model Architecture
- Hyperparameters
- Installation
- Usage
- Streamlit Deployment
- Hugging Face Integration
- Future Improvements
- Author

---

# 📖 Project Overview

AI Pet Classifier is an end-to-end Deep Learning project that predicts whether an uploaded image belongs to a **Cat** or **Dog**.

This project demonstrates the complete Deep Learning workflow starting from data preprocessing and CNN model training to deploying a production-ready web application using **Streamlit**.

The trained TensorFlow model is stored on **Hugging Face Hub** and dynamically downloaded whenever the application starts, making deployment lightweight and scalable.

---

# ✨ Features

✅ Binary Image Classification

✅ TensorFlow CNN Model

✅ Data Augmentation

✅ Image Preprocessing

✅ Batch Normalization

✅ Confidence Score

✅ Streamlit Web Interface

✅ Hugging Face Model Hosting

✅ Responsive UI

✅ Beginner Friendly

---

# 📸 Application Preview

```
┌──────────────────────────────────────┐
│          AI Pet Classifier           │
│                                      │
│ Upload Image                         │
│                                      │
│        🐱  OR  🐶                    │
│                                      │
│      [ Choose File ]                 │
│                                      │
│      [ Predict ]                     │
│                                      │
│ Prediction : 🐶 Dog                  │
│ Confidence : 98.76%                  │
└──────────────────────────────────────┘
```

(Add screenshots here after deployment.)

---

# 🧠 CNN Architecture

```
Input Image (64x64x3)

        │
        ▼

Image Preprocessing

        │
        ▼

Conv2D (32 Filters)

        │
        ▼

Batch Normalization

        │
        ▼

MaxPooling

        │
        ▼

Conv2D (64 Filters)

        │
        ▼

MaxPooling

        │
        ▼

Conv2D (128 Filters)

        │
        ▼

MaxPooling

        │
        ▼

Flatten

        │
        ▼

Dense (128)

        │
        ▼

Sigmoid Output

        │
        ▼

🐱 Cat / 🐶 Dog
```

---

# 🔄 End-to-End Workflow

```
Dataset

↓

Data Cleaning

↓

Image Resizing

↓

Normalization

↓

Data Augmentation

↓

CNN Model

↓

Training

↓

Validation

↓

Model Saving (.h5)

↓

Upload to Hugging Face

↓

Streamlit App

↓

Image Upload

↓

Prediction

↓

Confidence Score
```

---

# 📂 Project Structure

```
AI_Pet_Classifier/

│
├── app.py
├── cnn_model.h5
├── AI_Pet_Classifier.ipynb
├── requirements.txt
├── README.md
├── LICENSE
│
├── Dataset/
│   │
│   ├── training_set/
│   │      ├── cats/
│   │      └── dogs/
│   │
│   └── test_set/
│          ├── cats/
│          └── dogs/
│
└── Images/
      ├── app.png
      ├── architecture.png
      └── prediction.png
```

---

# ⚙ Technologies Used

| Category | Technologies |
|------------|----------------|
| Language | Python |
| Deep Learning | TensorFlow, Keras |
| Image Processing | Pillow, NumPy |
| Deployment | Streamlit |
| Model Hosting | Hugging Face |
| IDE | VS Code, Google Colab |

---

# 📊 Dataset

### Classes

🐱 Cat

🐶 Dog

### Image Size

```
64 × 64
```

### Color Mode

```
RGB
```

### Output

```
Binary Classification
```

---

# 📈 Hyperparameters

| Parameter | Value |
|------------|--------|
| Optimizer | Adam |
| Loss Function | Binary Crossentropy |
| Activation | ReLU |
| Output Activation | Sigmoid |
| Image Size | 64x64 |
| Batch Size | 32 |
| Epochs | 25 |

---

# 🖥 Streamlit Features

The application provides:

- Upload Images
- Live Image Preview
- Real-time Prediction
- Confidence Percentage
- Low Confidence Warning
- Beautiful Responsive UI
- Fast Model Loading using Cache
- Hugging Face Model Download

---

# 🤗 Hugging Face Integration

Instead of storing the model inside the repository, it is downloaded directly from Hugging Face.

```python
from huggingface_hub import hf_hub_download

model_path = hf_hub_download(
    repo_id="Sudheer17/AI_Pet_Classifier",
    filename="cnn_model.h5"
)

model = tf.keras.models.load_model(model_path)
```

This keeps the repository lightweight while ensuring the latest model is always available.

---

# 🚀 Installation

Clone Repository

```bash
git clone https://github.com/M-Sudheer18/AI_Pet_Classifier.git
```

Move to project

```bash
cd AI_Pet_Classifier
```

Install Requirements

```bash
pip install -r requirements.txt
```

Run

```bash
streamlit run app.py
```

---

# 📦 Requirements

```
tensorflow
keras
numpy
streamlit
Pillow
huggingface_hub
```

---

# 🔮 Future Improvements

- EfficientNet Transfer Learning
- MobileNetV3
- Grad-CAM Visualization
- Multi-class Pet Classification
- TensorFlow Lite Version
- Mobile App Deployment
- Docker Container
- CI/CD Pipeline
- Model Monitoring
- Cloud Deployment

---

# 📌 Key Learning Outcomes

✔ CNN Architecture

✔ Image Classification

✔ TensorFlow

✔ Keras

✔ Streamlit Deployment

✔ Hugging Face Hub

✔ Computer Vision

✔ Model Deployment

✔ Python Programming

---

# 👨‍💻 Author

## Sudheer Muthyala

🎓 B.Tech - Electronics & Communication Engineering

💻 Aspiring AI Engineer | Data Science Enthusiast | Full Stack Learner

### Connect with Me

🐙 GitHub

https://github.com/M-Sudheer18

🤗 Hugging Face

https://huggingface.co/Sudheer17

💼 LinkedIn

(Add your LinkedIn URL)

---

# ⭐ Support

If you found this project helpful,

⭐ Star this repository

🍴 Fork the repository

📝 Share your feedback

---

<div align="center">

## ❤️ Thank You for Visiting

*"Artificial Intelligence is not replacing humans—it is empowering them to solve bigger problems."*

Made with ❤️ by **Sudheer Muthyala**

</div>
