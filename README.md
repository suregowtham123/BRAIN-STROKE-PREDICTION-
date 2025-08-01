# 🧠 Brain Stroke Detection with 6 DOF Robotic Simulation

This project aims to detect the risk of brain stroke using machine learning techniques and simulate a **6 DOF (Degrees of Freedom)** robotic arm that assists in medical diagnostics. The robot is enhanced with concepts of **Robotic CALM (Cooperative and Autonomous Learning Manipulator)**, **Focus**, and **Flair** to perform precision-based and adaptive tasks in a simulated healthcare environment.



## 🧪 Project Overview

- ✅ **Brain Stroke Prediction** using ML models on patient health data.
- 🤖 **6 DOF Robotic Arm Simulation** to mimic medical equipment alignment tasks.
- 🧠 **Robotic CALM**: Robot learns from environment to assist doctors more efficiently.
- 🎯 **Focus**: Precision in targeting brain regions or patient data.
- ✨ **Flair**: Adaptive and smooth robot motion for enhanced user experience.



## 🧬 Dataset

- **File**: `brain_stroke.csv`
- **Source**: Kaggle or custom
- **Features include**:
  - Age, gender, hypertension, heart disease
  - Smoking status, glucose level, C-reactive protein
  - Cholesterol level, physical activity level, alcohol consumption
  - Family history



## 🧠 Machine Learning

- **Preprocessing**:
  - Handling missing values
  - Encoding categorical data
  - Feature scaling and normalization

- **Models Used**:
  - Logistic Regression
  - Random Forest
  - Support Vector Machine (SVM)
  
- **Evaluation Metrics**:
  - Accuracy
  - Precision, Recall, F1-score
  - ROC-AUC



## 🤖 Robotic Simulation

- **6 DOF Robotic Arm**:
  - Simulated using `PyBullet` or `Gazebo`
  - Performs equipment alignment or brain scan assist tasks
  - Controlled using inverse kinematics for precision

- **Robotic CALM**:
  - Learns from past movements and scan data to improve accuracy
  - Reacts autonomously to doctor/patient interaction or scan feedback

- **Focus**:
  - Precisely targets areas on brain scans or device alignment zones

- **Flair**:
  - Introduces smooth motion transitions and adaptive learning features



## 🔧 Technologies Used

| Category         | Tools/Libraries                 |
|------------------|----------------------------------|
| Language         | Python                          |
| ML Libraries     | scikit-learn, pandas, NumPy      |
| Visualization    | Matplotlib, Seaborn              |
| Simulation       | PyBullet (or Gazebo/ROS)         |
| Deployment       | Flask (for ML model deployment)  |


## 🚀 Screenshots
![FrontEnd Page](.png)


### 1. Clone the Repository
```bash
git clone https://github.com/your-username/brain-stroke-detection.git
cd brain-stroke-detection
