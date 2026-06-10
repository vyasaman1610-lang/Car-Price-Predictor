import streamlit as st
import numpy as np
import joblib
import os

st.set_page_config(
    page_title="Car Price Predictor",
    page_icon="🚗",
    layout="centered"
)

st.markdown("""
<style>
.stApp {
    background: linear-gradient(to bottom, #0f172a, #000000);
    color: white;
}

.main-title {
    text-align: center;
    color: #00ff99;
    font-size: 40px;
    font-weight: bold;
    margin-bottom: 20px;
}

.result-box {
    padding: 20px;
    border-radius: 12px;
    text-align: center;
    font-size: 22px;
    font-weight: bold;
    background: rgba(0,255,153,0.1);
    border: 1px solid #00ff99;
}
</style>
""", unsafe_allow_html=True)

MODEL_PATH = os.path.join(os.path.dirname(__file__), "model.pkl")

try:
    model = joblib.load(MODEL_PATH)
except Exception as e:
    st.error(f"Model loading failed: {e}")
    st.stop()

st.markdown('<div class="main-title">🚗 Car Price Predictor</div>', unsafe_allow_html=True)

Year = st.slider("Year", 2000, 2024, 2015)
Present_Price = st.slider("Present Price (in lakhs)", 0.1, 50.0, 5.0)
Kms_Driven = st.slider("Kilometers Driven", 0, 200000, 50000)
Owner = st.selectbox("Owners", [0, 1, 2, 3])

Fuel_Type = st.radio("Fuel Type", ["Petrol", "Diesel", "CNG"], horizontal=True)
Seller_Type = st.radio("Seller Type", ["Dealer", "Individual"], horizontal=True)
Transmission = st.radio("Transmission", ["Manual", "Automatic"], horizontal=True)

Fuel_Diesel = 1 if Fuel_Type == "Diesel" else 0
Fuel_Petrol = 1 if Fuel_Type == "Petrol" else 0
Seller_Individual = 1 if Seller_Type == "Individual" else 0
Transmission_Manual = 1 if Transmission == "Manual" else 0

if st.button("🔍 Predict Price", use_container_width=True):

    Car_Age = 2026 - Year

    input_data = np.array([[
        Present_Price,
        Kms_Driven,
        Owner,
        Seller_Individual,
        Transmission_Manual,
        Fuel_Diesel,
        Fuel_Petrol,
        Car_Age
    ]], dtype=float)

    try:
        pred_log = model.predict(input_data)[0]
        pred_price = np.expm1(pred_log)
        pred_price = max(pred_price, 0)

        st.markdown(f"""
        <div class="result-box">
            💰 Predicted Selling Price<br><br>
            <span style="color:#00ff99;font-size:30px;">
                ₹ {pred_price:.2f} Lakhs
            </span>
        </div>
        """, unsafe_allow_html=True)

    except Exception as e:
        st.error(f"Prediction error: {e}")
