

---

````markdown
# 🎓 IIT Guwahati Student Face Recognition System  

[![Live Demo](https://img.shields.io/badge/🚀_Live_Demo-Hugging_Face-blue?style=for-the-badge&logo=huggingface)](https://huggingface.co/spaces/demodemo9758/IITG-Face-App)  
[![GitHub Stars](https://img.shields.io/github/stars/Aan9758/IITG-Face-App?style=for-the-badge&logo=github)](https://github.com/Aan9758/IITG-Face-App/stargazers)  
[![Forks](https://img.shields.io/github/forks/Aan9758/IITG-Face-App?style=for-the-badge&logo=github)](https://github.com/Aan9758/IITG-Face-App/network/members)  

⚡ A **Streamlit-powered web app** that uses the **InsightFace** `buffalo_l` model to recognize and match student faces from IIT Guwahati’s dataset with **high accuracy**.  

---

## ✨ Features  

✅ **Real-time Recognition** – Upload a photo & instantly find the closest match  
✅ **High Accuracy** – Powered by **InsightFace `buffalo_l`** model  
✅ **Fast Matching** – Uses pre-computed embeddings for **speed** ⏱️  
✅ **Clean UI** – Simple drag-and-drop uploads via Streamlit  
✅ **Side-by-Side Comparison** – Original vs. matched student photo  

---

## 🛠️ Tech Stack  

| Component | Technology |
|-----------|------------|
| 🌐 Web Framework | [Streamlit](https://streamlit.io/) |
| 🤖 Face Recognition | [InsightFace](https://github.com/deepinsight/insightface) |
| ⚡ AI Backend | [ONNX Runtime](https://onnxruntime.ai/) |
| 📸 Image Processing | OpenCV |
| 🔢 Math/ML | NumPy, Python |

---

## 📥 Installation  

<details>
<summary>▶️ Expand to see setup steps</summary>  

**1. Clone this repo**  
```bash
git clone https://github.com/Aan9758/IITG-Face-App.git
cd IITG-Face-App
````

**2. Create virtual environment (recommended)**

```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux  
venv\Scripts\activate      # Windows
```

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

**4. Run the app**

```bash
streamlit run app.py
```

</details>  

---

## 🎮 Usage

1. Upload a **student’s photo** (`.jpg` / `.png`)
2. The app extracts embeddings & compares with the IITG dataset
3. Get **best match + similarity score**
4. See **side-by-side visualization** for verification ✅

---

## 📸 Demo Preview

![App Screenshot](https://via.placeholder.com/800x400.png?text=IITG+Face+Recognition+Demo)

---

## 📂 Project Structure

```
IITG-Face-App/
│── app.py              # Main Streamlit app
│── embeddings.npy      # Pre-computed face embeddings
│── dataset/            # Student images dataset
│── requirements.txt    # Dependencies
│── README.md           # Documentation
```

---

## 🎯 Try it Out

<a href="https://huggingface.co/spaces/demodemo9758/IITG-Face-App">
    <img src="https://img.shields.io/badge/▶️%20Launch%20App-HuggingFace-orange?style=for-the-badge&logo=huggingface" alt="Live Demo"/>
</a>

---

## 🤝 Contributing

We ❤️ contributions!

* Fork this repo
* Create a feature branch (`git checkout -b feature-xyz`)
* Commit changes & push (`git push origin feature-xyz`)
* Open a **PR** 🚀

---

## 📧 Contact

👨‍💻 **Author:** Aman Saraswat
📩 Email: *your\_email\_here*
🔗 [LinkedIn](https://linkedin.com/in/your-profile)

```

---

⚡ Now your README has:  
- A **Live Demo badge** at the top.  
- A **big orange “Launch App” button** in a “Try it Out” section.  
- Professional formatting with emojis, collapsible setup steps, and structure.  

Do you also want me to add a **“How It Works” flowchart (upload → embeddings → matching → result)** as an image so it looks even more professional for GitHub?
```
