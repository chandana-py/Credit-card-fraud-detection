import streamlit as st
import pickle
import numpy as np

# ================================
# 🔹 Load Model & Encoder
# ================================
model = pickle.load(open("model.pkl", "rb"))
encoder = pickle.load(open("encoder.pkl", "rb"))

# ================================
# 🔹 Page Config
# ================================
st.set_page_config(page_title="Fraud Detector", layout="centered")

st.title("💳 Credit Card Fraud Detection")
st.write("Enter transaction details to predict fraud")

# ================================
# 🔹 Inputs
# ================================
amt = st.number_input("Transaction Amount ($)", min_value=0.0, value=100.0)

hour = st.slider("Transaction Hour (0–23)", 0, 23, 12)

category = st.selectbox(
    "Transaction Category",
    ["shopping", "food", "travel", "entertainment", "others"]
)

age = st.number_input("Customer Age", min_value=18, max_value=100, value=30)

distance = st.number_input("Distance from Merchant (km)", min_value=0.0, value=5.0)

# ================================
# 🔹 Encode Category (IMPORTANT FIX)
# ================================
try:
    cat_encoded = encoder.transform([category])[0]
except:
    # fallback if category not in encoder
    cat_encoded = 0

# ================================
# 🔹 Prediction
# ================================
if st.button("🔍 Check Transaction"):

    # Feature order MUST match training
    features = np.array([[amt, hour, cat_encoded, age, distance]])

    prob = model.predict_proba(features)[0][1]

    st.subheader("Result")

    if prob > 0.5:
        st.error(f"⚠️ Fraud Detected! ({prob*100:.2f}%)")
    else:
        st.success(f"✅ Legitimate Transaction ({100 - prob*100:.2f}% safe)")

    # Progress bar
    st.progress(int(prob * 100))

# ================================
# 🔹 Info Section
# ================================
st.markdown("---")
st.subheader("📊 Model Insights")

st.write("""
- 💰 Amount → High amounts increase fraud risk  
- ⏰ Late-night transactions → more suspicious  
- 📍 Large distance → unusual behavior  
- 👤 Age → spending pattern differences  
""")