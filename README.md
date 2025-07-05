<<<<<<< HEAD
# ai-meeting-assistant
=======
# 🧠 AI Meeting Assistant 🎧

A lightweight voice-based assistant that listens to your voice (like in Zoom or Google Meet), transcribes it, and responds intelligently — all **offline using Ollama and local LLMs** like TinyLLaMA or Phi-3.

---

## 🚀 Features

* 🎤 Voice recording with 1-click
* 🧠 Speech-to-text transcription using Whisper
* 💬 Natural responses using local LLMs via Ollama
* 💻 Runs fully **offline** (no API keys or billing required)
* 💇️ Lightweight models (works with as low as 2GB RAM)

---

## 📁 Folder Structure

```
ai-meeting-assistant/
│
├── app.py                 # Streamlit app
├── audio_utils.py         # Audio recording logic
├── transcribe_utils.py    # Whisper-based transcription
├── ai_utils.py            # Ollama-based response generation
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
```

---

## 💪 Installation & Setup

### 🔧 Prerequisites

* Python 3.10 or later
* Pip + virtualenv
* Streamlit
* Whisper
* Ollama

---

### 📆 Step 1: Clone the repo

```bash
git clone https://github.com/your-username/ai-meeting-assistant.git
cd ai-meeting-assistant
```

---

### 🚪 Step 2: Create virtual environment and install dependencies

```bash
python -m venv venv
venv\Scripts\activate     # On Windows
# source venv/bin/activate  # On Mac/Linux

pip install -r requirements.txt
```

> 📝 Sample `requirements.txt`:

```txt
streamlit
whisper
sounddevice
numpy
ollama
python-dotenv
```

---

### 🧠 Step 3: Install and Run Ollama

#### ✅ Download Ollama:

[https://ollama.com/download](https://ollama.com/download)

#### ✅ Run a lightweight model (recommended for low RAM):

```bash
ollama run tinyllama
```

> First run will download the model (\~400MB). Keep the terminal open.

---

### 🏃️ Step 4: Run the App

```bash
streamlit run app.py
```

Open in browser → [http://localhost:8501](http://localhost:8501)
Click **“Start Listening”** and speak for 5 seconds. You'll get a transcription + intelligent response.

---

## 📸 Screenshots

| Record Audio | Get Answers |
| ------------ | ----------- |
|              |             |

---

## 🧐 Model Options

Supported local models (via Ollama):

* `tinyllama` ✅ (ideal for low memory)
* `phi3` (lightweight)
* `gemma:2b` (medium size)
* `llama3` (only if > 6GB RAM)

Update `ai_utils.py` to switch models:

```python
client.chat(model='tinyllama', ...)
```

---

## 📌 To-Do / Improvements

*

---

## 🧑‍💼 Author

**Riya Sonal Nazareth**
🔗 [LinkedIn](https://www.linkedin.com/in/riya-sonal-nazareth-20b26a227/)
💻 [GitHub](https://github.com/Riya-sonal)

---

## 📜 License

This project is open source under the [MIT License](LICENSE).
>>>>>>> d7d6642 (Initial commit with working AI Meeting Assistant and README)
