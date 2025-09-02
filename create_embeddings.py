# create_embeddings.py
import os
import cv2
import pickle
from insightface.app import FaceAnalysis

# Initialize InsightFace model
print("🚀 Initializing InsightFace model...")
app = FaceAnalysis(name='buffalo_l', providers=['CPUExecutionProvider'])
app.prepare(ctx_id=0)

# Path to your dataset
KNOWN_DIR = 'dataset'
known_faces = {}

print(f"🔄 Processing dataset in '{KNOWN_DIR}' folder...")
image_files = [f for f in os.listdir(KNOWN_DIR) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]

for index, filename in enumerate(image_files):
    path = os.path.join(KNOWN_DIR, filename)
    name = os.path.splitext(filename)[0]

    img = cv2.imread(path)
    if img is None:
        print(f"⚠️ Could not read {path}, skipping.")
        continue

    faces = app.get(img)

    if faces:
        known_faces[name] = (path, faces[0].normed_embedding)
        print(f"✅ ({index + 1}/{len(image_files)}) Processed: {name}")
    else:
        print(f"❌ ({index + 1}/{len(image_files)}) No face found in {path}, skipping.")

# Save the dictionary to a file
with open("known_faces_data.pkl", "wb") as f:
    pickle.dump(known_faces, f)

print(f"\n🎉 Success! Saved embeddings for {len(known_faces)} faces to known_faces_data.pkl")