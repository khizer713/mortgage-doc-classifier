# 🧾 Mortgage Document Classifier

A hybrid **Streamlit + Flask** machine learning app for classifying scanned mortgage-related documents (e.g., W-2s, pay stubs, bank statements, and 1003 forms). Built for rapid prototyping and future scalability.

---

## 📂 Project Structure

mortgage-doc-classifier/ 
│ ├── models/ # Trained ML models (e.g., model.h5) 
├── src/ # Core training and inference logic 
│ ├── preprocess.py 
│ ├── train_model.py 
│ └── predict.py 
├── streamlit_app/ # Frontend UI built with Streamlit 
│ └── app.py 
├── requirements.txt # Project dependencies 
└── README.md


---

## 🚀 Quickstart

### 1. Clone the Repository
2. Set Up a Virtual Environment
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

🧠 Features
Supports classification of multiple mortgage-related document types

Uses OpenCV + TensorFlow backend for image processing

Simple frontend via Streamlit, extensible with Flask or cloud APIs

Ready to expand with OCR and schema validation

📌 Next Steps
Add sample labeled data

Train and save the classification model to /models

Expand Flask API and Streamlit UI for deeper workflows


