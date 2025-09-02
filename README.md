

````markdown
# 🎓 IIT Guwahati Student Face Recognition System

[![Live Demo](https://img.shields.io/badge/Live_Demo-Hugging_Face-blue?style=for-the-badge&logo=huggingface)](https://huggingface.co/spaces/demodemo9758/IITG-Face-App)

A web application built with Streamlit that uses the InsightFace library to recognize and match student faces from a large dataset.



---

## 🚀 Features

-   **Real-time Recognition**: Upload a student's photo and instantly find a match in the dataset.
-   **High Accuracy**: Leverages the powerful `buffalo_l` model from InsightFace for robust facial feature extraction.
-   **Efficient Backend**: Pre-computes and caches face embeddings for fast matching, even with thousands of images.
-   **Interactive UI**: A simple and clean user interface built with Streamlit for easy file uploads and clear result presentation.
-   **Side-by-Side Comparison**: Displays the uploaded image next to the matched student's photo for visual verification.

---

## 🛠️ Technology Stack

-   **Web Framework**: [Streamlit](https://streamlit.io/)
-   **Face Recognition**: [InsightFace](https://github.com/deepinsight/insightface)
-   **AI Model Backend**: [ONNX Runtime](https://onnxruntime.ai/)
-   **Core Libraries**: Python, OpenCV, NumPy

---

## 📦 Local Setup and Installation

To run this project on your local machine, follow these steps:

**1. Clone the Repository:**
```bash
git clone [https://github.com/Aan9758/IITG-Face-App.git](https://github.com/Aan9758/IITG-Face-App.git)
cd IITG-Face-App
````

**2. Install Dependencies:**
Ensure you have Python 3.8+ installed. Then, install the required libraries from `requirements.txt`.

```bash
pip install -r requirements.txt
```

> **Note for Windows users:** You may need to install Microsoft C++ Build Tools if the `insightface` installation fails.

**3. Prepare the Dataset (if needed):**

  - The pre-computed embeddings are included in `known_faces_data.pkl`.
  - To add new faces, place new student images in the `dataset/` folder and run the following script to regenerate the embeddings file:
    ```bash
    python create_embeddings.py
    ```

**4. Run the Streamlit App:**

```bash
streamlit run app.py
```

The application will open in a new tab in your web browser.

-----

## 📁 Project Structure

```
.
├── 📄 app.py                    # The main Streamlit application script
├── 📄 create_embeddings.py      # Script to process the dataset into a .pkl file
├── 📄 known_faces_data.pkl      # Pre-computed face embeddings for fast lookups
├── 📄 requirements.txt          # List of Python dependencies
├── 🖼️ screenshot.png            # A screenshot of the running app
└── 📁 dataset/                   # Folder containing all the student images
    └── 📜 .gitkeep
```

```

---

This method should work without any issues. Thank you again for your patience.
```
