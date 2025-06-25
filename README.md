# 🧾 Mortgage Document Classifier

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Streamlit](https://img.shields.io/badge/Built%20with-Streamlit-ff4b4b?logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python&logoColor=white)](https://www.python.org/)
[![GitHub Repo Size](https://img.shields.io/github/repo-size/khizer713/mortgage-doc-classifier)](https://github.com/khizer713/mortgage-doc-classifier)

A hybrid **Streamlit + Flask** machine learning app for classifying scanned mortgage-related documents (e.g., W-2s, pay stubs, bank statements, and 1003 forms). Built for rapid prototyping and future scalability.

---

## 📸 Screenshot

![App Screenshot](streamlit_app/assets/screenshot.png)

> _Tip: Save your screenshot in `streamlit_app/assets/` and update the path above accordingly._

---

## 📂 Project Structure

mortgage-doc-classifier/ 
│ ├── models/ # Trained ML models (e.g., model.h5) 
├── src/ # Core training and inference logic 
│ ├── preprocess.py 
│ ├── train_model.py 
│ └── predict.py 
├── streamlit_app/ # Frontend UI built with Streamlit 
│ ├── app.py 
│ └── assets/ # Images, logos, etc. 
├── requirements.txt # Project dependencies 
└── README.md

---

## 🚀 Quickstart

### 1. Clone the Repository

```bash
git clone https://github.com/khizer713/mortgage-doc-classifier.git
cd mortgage-doc-classifier


### 2. Set Up a Virtual Environment
python -m venv venv
# Activate it:
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

### 3. Install Depedencies 
pip install -r requirements.txt

### 4. Run The App
cd streamlit_app
streamlit run app.py

The app will launch in your default browser at http://localhost:8501.

Features
Classifies multiple mortgage-related document types

Uses OpenCV + TensorFlow backend for image processing

Streamlit frontend with Flask backend API (optional)

Ready to expand with OCR and schema validation

🧪 Example Usage
Upload a scanned document (e.g., paystub.jpg) via the Streamlit UI. The app will:

Preprocess the image

Run it through the trained model

Display the predicted document type and confidence score

📌 Next Steps
Add sample labeled data

Train and save the classification model to /models

Expand Flask API and Streamlit UI for deeper workflows

📄 License
This project is licensed under the MIT License.
