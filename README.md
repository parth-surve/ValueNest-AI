# 🏠 ValueNest AI — House Price Prediction System

🚀 **Live App:** https://valuenest-ai.streamlit.app

---

## 📌 Overview

**ValueNest AI** is an end-to-end machine learning project that predicts house prices based on key features like area, location, BHK, bathrooms, and balcony.

The project demonstrates a **complete ML pipeline** — from data preprocessing and model training to deployment using a modern web interface.

---

## 🎯 Features

* 📊 Predict house prices instantly
* 📍 Location-based pricing using encoded features
* 🧠 Machine Learning model (XGBoost Regressor)
* 🎨 Interactive UI built with Streamlit
* ⚡ Real-time predictions
* 🌐 Deployed on Streamlit Cloud

---

## 🧠 Tech Stack

* **Language:** Python
* **Libraries:** NumPy, Pandas, Scikit-learn, XGBoost
* **Backend:** FastAPI
* **Frontend:** Streamlit
* **Model Saving:** Joblib
* **Deployment:** Streamlit Cloud

---

## 🏗️ Project Structure

```
ValueNest-AI/
│
├── app/                # Streamlit UI
│   └── app.py
│
├── api/                # FastAPI backend
│   └── main.py
│
├── src/                # Core ML logic
│   ├── predict.py
│   ├── data_preprocessing.py
│   ├── utils.py
│   └── config.py
│
├── models/             # Saved model & columns
│   ├── house_price_model.joblib
│   └── columns.json
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/          # EDA & training
│   └── eda.ipynb
│
├── requirements.txt
└── README.md
```

---

## ⚙️ How It Works

1. User enters property details (sqft, location, BHK, etc.)
2. Input is preprocessed into model-compatible format
3. Model predicts price (log scale → converted back using exp)
4. Result displayed via Streamlit UI

---

## 📊 Model Details

* Model Used: **XGBoost Regressor**
* Hyperparameter tuning using **GridSearchCV**
* Target transformation: **log(price)** for better stability

### 📈 Performance

* R² Score: ~0.83
* Cross-validation score: ~0.76

---

## ⚠️ Limitations

* Dataset is ~5–8 years old
* Does not include market trends or inflation
* Predictions are approximate, not real-time market values

---

## 🚀 Future Improvements

* 📊 Add price trends visualization
* 📍 Integrate map-based location insights
* 🧠 Add confidence intervals
* 🔄 Use updated dataset for real-world accuracy
* 🌐 Deploy FastAPI backend separately

---

## 👨‍💻 Author

**Parth Surve**
Computer Engineering Student

---

## ⭐ If you liked this project

Give it a ⭐ on GitHub and share your feedback!
