# app.py
import streamlit as st
import cv2
import numpy as np
import pickle
from PIL import Image
from numpy.linalg import norm
from insightface.app import FaceAnalysis

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="IITG Face Recognition", page_icon="🎓", layout="wide")

st.title("🎓 IIT Guwahati Student Face Recognition System")
st.write("Upload an image to find a matching student from the IITG dataset.")

# --- MODEL AND DATA LOADING ---
@st.cache_resource
def load_model_and_data():
    face_app = FaceAnalysis(name='buffalo_l', providers=['CPUExecutionProvider'])
    face_app.prepare(ctx_id=0)
    with open("known_faces_data.pkl", "rb") as f:
        known_faces_data = pickle.load(f)
    return face_app, known_faces_data

app, known_faces = load_model_and_data()
st.success(f"✅ Model and data for {len(known_faces)} students loaded successfully!")

# --- CORE FUNCTIONS ---
def find_match(test_embedding, threshold=1.2):
    best_name, best_path, best_dist = "Unknown", None, float("inf")
    for name, (path, emb) in known_faces.items():
        dist = norm(test_embedding - emb)
        if dist < best_dist and dist < threshold:
            best_name, best_path, best_dist = name, path, dist
    return best_name, best_path, best_dist

# --- UI LOGIC ---
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

# CORRECTED LINE BELOW
if uploaded_file is not None:
    image = Image.open(uploaded_file).convert('RGB')
    img_array = np.array(image)
    
    faces = app.get(img_array)
    
    col1, col2 = st.columns(2)
    with col1:
        st.image(image, caption='Uploaded Image', use_column_width=True)

    if faces:
        test_embedding = faces[0].normed_embedding
        matched_name, matched_path, distance = find_match(test_embedding)
        
        with col2:
            if matched_name != "Unknown":
                st.success(f"**Match Found!**")
                st.info(f"**Name:** {matched_name}")
                st.info(f"**Similarity Distance:** {distance:.3f} (Lower is better)")
                matched_image = Image.open(matched_path)
                st.image(matched_image, caption=f"Matched: {matched_name}", use_column_width=True)
            else:
                st.error("No match found in the dataset.")
    else:
        with col2:
            st.error("No face detected in the uploaded image.")
