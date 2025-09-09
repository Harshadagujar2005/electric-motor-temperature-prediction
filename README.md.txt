# 🔥 Electric Motor Temperature Prediction

This project predicts the **rotor temperature of an electric motor** using various Machine Learning algorithms:
- Linear Regression
- Decision Tree
- Random Forest
- Support Vector Machine (SVM)

The best-performing model (**Random Forest**) is deployed using a **Flask web application** for real-time prediction.

---

## 🚀 Features
- Data preprocessing and feature engineering  
- Comparison of multiple ML algorithms  
- Model evaluation using MSE and R² score  
- Saving the best model in `.pkl` format  
- Flask integration with a user-friendly web interface  

---

## 📊 Dataset
The dataset contains the following features:
- Ambient temperature (°C)  
- Coolant temperature (°C)  
- Voltage (d, q axes)  
- Current (d, q axes)  
- Motor speed (rpm)  
- **Target:** Rotor Permanent Magnet (PM) Temperature  

---

## ⚙️ How to Run

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/Electric-Motor-Temperature-Prediction.git
   cd Electric-Motor-Temperature-Prediction
Install dependencies:

pip install -r requirements.txt


Train the model:

python train_model.py


Run Flask app:

python app.py


Open your browser and go to:

http://127.0.0.1:5000/

🌐 Project Workflow

Data Collection

Preprocessing

Feature Engineering

Model Training

Model Evaluation

Save Best Model (model.pkl)

Flask Deployment

Web-based Prediction


👩‍💻 Author

Harshada Gahininath Gujar
MIT Academy of Engineering, Alandi

📚 References

Pedregosa et al., Scikit-learn: Machine Learning in Python, JMLR, 2011

Flask Documentation

Research papers on predictive maintenance