# 📊 Customer Churn Prediction & Analysis Platform

An end-to-end **Customer Churn Prediction and Analytics Platform** that combines **Machine Learning, Data Visualization, Business Intelligence dashboards, and Web Deployment** to help organizations identify churn risks, understand customer behavior, and make data-driven retention decisions.

This project is designed as a **real-world, production-style analytics application**, not just a model notebook.

---

## 🚀 Project Overview

Customer churn is one of the biggest challenges for subscription-based businesses. This project provides:

- 🔮 **Churn Prediction using Machine Learning**
- 👥 **Customer Segmentation Analysis**
- 📈 **Interactive Data Visualizations (Plotly)**
- 📊 **Embedded Power BI Dashboards**
- 🌐 **Modern Web Interface (Flask + HTML/CSS/JS)**
- ☁️ **Cloud Deployment Ready (AWS / Render / GCP)**

The application allows business users to:
- Predict whether a customer is likely to churn
- Analyze churn trends across demographics and subscriptions
- Understand revenue loss due to churn
- Segment customers for targeted retention strategies

---

## 🧠 Machine Learning Pipeline

### 🔹 Data Processing
- Handled numerical and categorical features
- Applied **one-hot encoding** for categorical variables
- Scaled numerical features using **MinMaxScaler**
- Balanced classes using **SMOTE (imbalanced-learn)**

### 🔹 Features Used

### 🔹 Models
- Trained churn classification model (scikit-learn)
- Saved model and scaler as `.pkl` files
- Loaded directly into Flask for real-time inference

---

## 📈 Analytics & Visualizations
-CustomerID  
-Age  
-Tenure  
-Usage Frequency  
-Support Calls  
-Payment Delay  
-Total Spend  
-Last Interaction  
-Gender (Male/Female)  
-Subscription Type (Basic / Standard / Premium)  
-Contract Length (Monthly / Quarterly / Annual)  <br>

### 🔹 Plotly Visualizations (10 Key Insights)  
**Churn Analysis**
- Churn Rate Distribution
- Churn by Gender
- Churn by Subscription Type
- Churn by Contract Length

**Customer Behavior**
- Tenure vs Churn
- Support Calls vs Churn
- Payment Delay vs Churn

**Revenue Insights**
- Total Spend by Subscription Type
- Average Spend by Churn Status
- Age Distribution by Churn

All plots are dynamically generated and displayed within the web application.

---

## 📊 Power BI Dashboards

Three professional dashboards were created and integrated:

1️⃣ **Churn Overview Dashboard**
- Churn rate by contract length
- Tenure-based churn trends
- Overall churn distribution

2️⃣ **Revenue Impact Dashboard**
- Revenue loss due to churn
- Spend comparison (churned vs retained)
- Support call patterns

3️⃣ **Customer Engagement Dashboard**
- Usage frequency analysis
- Payment delay impact
- Contract and subscription performance

These dashboards provide **executive-level insights** alongside ML predictions.

---

## 🌐 Web Application (Flask)

### 🔹 Pages Included
- **Home** – Project overview
- **Churn Prediction** – Interactive prediction form
- **Customer Segmentation** – Cluster-based insights
- **Analytics** – Plotly visualizations
- **Dashboard** – Embedded Power BI reports

### 🔹 Tech Stack
- Backend: **Flask**
- Frontend: **HTML, CSS, JavaScript**
- Styling: Modern, warm color palette, responsive for **1366×768** screens
- Interactive UX with dynamic form handling

---

## 📂 Project Structure

customer_analytics_app/  
│  
├── main.py  
├── requirements.txt  
├── Procfile  
├── app.yaml 
├── README.md  
│  
├── models/  
│ ├── churn_model.pkl  
│ └── scaler.pkl  
│  
├── templates/  
│ ├── index.html  
│ ├── predict.html  
│ ├── segmentation.html  
│ ├── analytics.html  
│ └── dashboard.html  
│  
├── static/  
│ ├── style.css  
│ ├── script.js  
│ └── plots/  
│  
├── segmentation_utils.py  
└── customer_churn_dataset.csv  

---

## ☁️ Deployment

This project is **cloud-ready** and has been deployed/tested on:

### 🔹 AWS EC2
- Ubuntu instance
- SSH access using `.pem` key
- Flask app exposed on port **8080**
- Security Group configured for HTTP access

### 🔹 Render
- Gunicorn-based deployment
- `Procfile` configured
- Automatic builds from GitHub

### 🔹 Google Cloud (App Engine)
- `app.yaml` included
- Compatible with GCP Python runtime

---

## 🛠 Installation & Run Locally

1.git clone https://github.com/your-username/Customer-churn-prediction-and-analysis.git<br>
2.cd customer_analytics_app<br>
3.python -m venv venv<br>
4.source venv/bin/activate   # Windows: venv\Scripts\activate  
5.pip install -r requirements.txt<br>
6.python main.py<br>

🎯 Key Outcomes:  
-Built a production-style ML system, not just a notebook  
-Combined ML + BI + Web Development  
-Designed for business decision-making  
-Deployed on real cloud infrastructure  
-Resume-ready & interview-ready project  

🔮 Future Enhancements:  
-Model monitoring & drift detection  
-Role-based access control  
-Real-time database integration  
-Automated retraining pipeline  
-A/B testing for churn reduction strategies  

👤 Author:  
Aniketanand Sandipkumar  
🔗App Link:https://customer-churn-prediction-and-analysis.onrender.com
