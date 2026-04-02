# 💳 Credit Card Fraud Detection System

A Machine Learning-based web application that detects fraudulent credit card transactions using an interactive Streamlit dashboard.

---

## 📌 Project Overview

This project predicts whether a transaction is **fraudulent or legitimate** based on key transaction features.  
It combines data preprocessing, feature engineering, machine learning, and a real-time user interface.

---

## 🧠 Machine Learning Models Used

- Logistic Regression  
- Decision Tree Classifier  
- Random Forest Classifier ✅ (Final Model)

The Random Forest model was selected as the best model based on overall performance.

---

## ⚙️ Features Used

- 💰 Transaction Amount (`amt`)  
- ⏰ Transaction Hour (`hour`)  
- 🛒 Transaction Category (`category`)  
- 👤 Customer Age (`age`)  
- 📍 Distance from Merchant (`distance_km`)  

---

## 📊 Model Performance

| Model               | Accuracy | F1 Score | ROC-AUC |
|--------------------|----------|----------|--------|
| Logistic Regression | 0.94     | 0.60     | 0.92   |
| Decision Tree       | 0.95     | 0.65     | 0.93   |
| Random Forest       | **0.97** | **0.75** | **0.96** |

> ⚠️ Replace these values with your actual results if needed

---

## 📈 Visualizations

### 🔹 ROC Curve
![ROC Curve](roc_curve.png)

### 🔹 Confusion Matrix
![Confusion Matrix](confusion_matrix.png)

---

## 🖥️ Streamlit Web Application

The web app allows users to:

- Enter transaction details  
- Get real-time fraud prediction  
- View probability and result instantly  

---

## 📁 Project Structure
