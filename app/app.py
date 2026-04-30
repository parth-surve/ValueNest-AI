import streamlit as st
import numpy as np
import json
import time
import matplotlib.pyplot as plt
import sys
import os

# Fix import path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.predict import predict_price

# ---------------- CONFIG ----------------
st.set_page_config(page_title="ValueNest AI", layout="centered")

# ---------------- STYLING ----------------
st.markdown("""
<style>
.main {
    background: linear-gradient(135deg, #0e1117, #1c1f26);
}

h1, h2, h3 {
    color: #ffffff;
}

/* Button */
.stButton>button {
    background: linear-gradient(90deg, #00c6ff, #0072ff);
    color: white;
    border-radius: 12px;
    height: 3em;
    font-weight: bold;
    width: 100%;
}

/* Result card */
.result-box {
    padding: 20px;
    border-radius: 15px;
    background: #1f2937;
    text-align: center;
    font-size: 24px;
    font-weight: bold;
    color: #00ffcc;
}
</style>
""", unsafe_allow_html=True)

# ---------------- LOAD LOCATIONS ----------------
with open("models/columns.json", "r") as f:
    data = json.load(f)
    locations = [col.replace("location_", "") for col in data if "location_" in col]

# ---------------- HEADER ----------------
st.title("🏠 ValueNest AI")
st.markdown("### 🧠 AI-Powered House Price Predictor")
st.markdown("Predict real estate prices instantly using machine learning.")
st.divider()

# ---------------- INPUT SECTION ----------------
st.markdown("## 🏡 Property Details")

col1, col2 = st.columns(2)

with col1:
    total_sqft = st.number_input("Total Sqft", 300, 10000, 1200)
    bath = st.number_input("Bathrooms", 1, 10, 2)

with col2:
    balcony = st.number_input("Balconies", 0, 5, 1)
    bhk = st.number_input("BHK", 1, 10, 2)

location = st.selectbox("📍 Select Location", sorted(locations))

st.divider()

# ---------------- PREDICTION ----------------
if st.button("🚀 Predict Price"):

    with st.spinner("Analyzing property..."):
        time.sleep(1.2)
        price = predict_price(total_sqft, bath, balcony, bhk, location)

    st.markdown("## 💰 Prediction Result")

    st.markdown(f"""
    <div class="result-box">
        ₹ {round(price, 2)} Lakhs
    </div>
    """, unsafe_allow_html=True)


    # ---------------- INSIGHT ----------------
    st.info("💡 Bathrooms have a strong influence on price in this model.")
    st.warning("⚠️ Based on historical data (~5–8 years old)")

# ---------------- SIDEBAR ----------------
st.sidebar.title("📊 About ValueNest AI")

st.sidebar.markdown("""
**Machine Learning House Price Predictor**

### ⚙️ Model
- XGBoost Regressor

### 📌 Features
- Area (sqft)
- Location
- BHK
- Bathrooms
- Balcony

### 🚀 Built With
- Python
- FastAPI
- Streamlit
""")

# ---------------- FOOTER ----------------
st.divider()
st.caption("Built by Parth Surve 🚀")