# 🏭 AI-Based Real-Time Defect Detection & Predictive Maintenance System

> Smart quality control for additive manufacturing — detecting defects **during** production, not after.

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=flat-square)
![TensorFlow](https://img.shields.io/badge/TensorFlow-Keras-orange?style=flat-square)
![OpenCV](https://img.shields.io/badge/CV-OpenCV-green?style=flat-square)
![ESP32](https://img.shields.io/badge/IoT-ESP32-red?style=flat-square)
![Accuracy](https://img.shields.io/badge/Model%20Accuracy-~92%25-brightgreen?style=flat-square)

---

## 📌 Overview

Modern manufacturing systems suffer from **delayed defect detection**, high material wastage, and a lack of real-time monitoring. Traditional approaches only catch defects after production is complete — by then, significant time, energy, and material have already been lost.

This project presents an **AI + IoT integrated system** that works *during* production to enable early intervention:

| Capability | Description |
|---|---|
| 🔍 Surface Defect Detection | CNN-based real-time analysis from camera input |
| 📡 Internal Defect Prediction | Sensor-based detection of cracks, porosity, and anomalies |
| ⚡ Instant Alerts | LED + buzzer triggers on abnormal conditions |
| 📊 Live Dashboard | Real-time visualization of machine health and defect status |

> ⚠️ **Before You Begin:** Dataset files are not included due to size constraints. Model files (`.h5`, `.keras`) must be loaded or trained separately. Full system functionality requires hardware setup with **ESP32 + sensors**.

---

## 🚨 Problem Statement

In additive manufacturing, defects go undetected until it's too late:

- Defects are only found **post-production**, not during the process
- **Internal defects** (cracks, porosity) are invisible to the naked eye
- Manual inspection is **slow, inconsistent, and error-prone**
- Vision systems and sensor data operate in **silos** — no integration

This leads to high rework costs, increased downtime, and reduced production efficiency — problems this system is designed to solve.

---

## 🎯 Objectives

**Primary:** Develop an AI-based system to detect and predict manufacturing defects in real time.

| Category | Objectives |
|---|---|
| Technical | CNN surface defect detection, sensor-based internal defect prediction, ESP32 data acquisition, integrated decision system |
| Industrial | Reduce material wastage, improve product quality, enable predictive maintenance, support Industry 4.0 transformation |

---

## ⚙️ System Architecture

The system integrates **Computer Vision + IoT Sensors + Decision Logic** into a single unified pipeline:

```
Camera Input → Image Processing → CNN Model → Surface Defect Detection
                        ↓
ESP32 → Sensor Data (Temp, Vibration, Load, RPM)
                        ↓
            Decision System (AI + Sensor Fusion)
                        ↓
        Correction Logic + Alert System (LED/Buzzer)
                        ↓
            Real-Time Dashboard Visualization
```

**Pipeline summary:** `Detect → Predict → Decide → Correct → Monitor`

---

## 🧠 Key Features

### 🔍 Real-Time Surface Defect Detection
A CNN model processes live camera input to classify surface defects with ~92% accuracy — in real time during the manufacturing process.

### 📡 Multi-Sensor Monitoring
The ESP32 microcontroller continuously reads from four sensor types:

| Sensor | Component | Data Captured |
|---|---|---|
| Temperature | DHT11 | Thermal anomalies |
| Vibration | Vibration sensor | Mechanical irregularities |
| Load | HX711 load cell | Force / pressure data |
| Speed | RPM sensor | Motor / spindle health |

### 🔗 AI + Sensor Fusion
Visual and sensor data are combined in a unified decision engine, enabling detection of **both surface and internal defects** — something neither source can achieve alone.

### 🚨 Alert System
Abnormal conditions trigger immediate hardware alerts via LED indicators and a buzzer, enabling operators to intervene before defects propagate.

### 🔧 Correction Mechanism
The system doesn't just detect — it actively **adjusts process parameters** to prevent failure continuation.

### 📊 Live Dashboard
A real-time monitoring UI visualizes sensor readings, defect status, and overall machine health.

---

## 📊 Results & Performance

| Metric | Value |
|---|---|
| CNN Model Accuracy | ~92% |
| Defect Recall | ~84% |
| Detection Mode | Real-time (during production) |
| Defect Types Covered | Surface + Internal |

---

## ⚖️ Traditional vs. Proposed System

| Feature | Traditional System | This System |
|---|---|---|
| Detection Time | Post-production | **Real-time** |
| Defect Types | Surface only | **Surface + Internal** |
| Accuracy | Moderate | **~92%** |
| Monitoring | Manual | **Automated** |
| Decision Making | Human-based | **AI-based** |
| Cost Efficiency | Low | **High** |

---

## 🧪 Technologies Used

| Layer | Technologies |
|---|---|
| Machine Learning | TensorFlow, Keras, CNN |
| Computer Vision | OpenCV, NumPy |
| IoT & Hardware | ESP32, DHT11, HX711, Vibration sensor, RPM sensor |
| Application | Python |
| Simulation | Digital twin module |

---

## 📂 Project Structure

```
AM-Quality-Control/
│
├── app.py                 # Main application entry point
├── model.py               # CNN model architecture
├── train_model.py         # Model training pipeline
├── test_model.py          # Model evaluation and testing
├── sensor_model.py        # Sensor-based prediction logic
├── digital_twin.py        # System simulation / digital twin
├── correction_system.py   # Process correction logic
├── utils.py               # Shared helper functions
│
├── dashboard/             # Real-time monitoring UI
│
├── accuracy.png           # Training accuracy graph
├── comparison.png         # System comparison chart
│
├── requirements.txt
└── .gitignore
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- ESP32 microcontroller + sensors (DHT11, HX711, vibration, RPM)
- Pretrained or self-trained model weights (`.h5` / `.keras`)

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/your-username/AM-Quality-Control.git
cd AM-Quality-Control

# 2. Install dependencies
pip install -r requirements.txt

# 3. Add your model weights to the project directory
#    (train using train_model.py or load pretrained weights)

# 4. Launch the application
python app.py
```

### Training the Model

```bash
python train_model.py
```

### Running Tests

```bash
python test_model.py
```

---

## 🏭 Applications

- Additive manufacturing / 3D printing quality control
- Smart factory and Industry 4.0 integration
- Predictive maintenance in industrial machinery
- MSME automation and cost reduction
- Any high-precision manufacturing environment

---

## 🔮 Future Enhancements

- [ ] Real-time cloud monitoring and remote alerting
- [ ] Advanced deep learning models (transformer-based vision)
- [ ] Fully automated process control loop
- [ ] Edge AI deployment (Jetson Nano, Coral)
- [ ] Scalable multi-machine industrial integration

---

> *"This project transforms quality control from inspection after failure → prevention before failure. By combining AI and IoT, it brings manufacturing closer to a fully intelligent, self-monitoring system."*
