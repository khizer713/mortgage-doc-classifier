import streamlit as st 

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.predict import classify_image

st.title("Mortgage Document Classifier")

uploaded_file = st.file_uploader("Upload a scanned document image", type=["jpg", "jpeg", "png"])
if uploaded_file:
    with open("temp.jpg", "wb") as f:
        f.write(uploaded_file.getbuffer())

    pred = classify_image("temp.jpg", "models/model.h5")
    st.write("Prediction:", pred)
