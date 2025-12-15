🎙️ Whisper Offline Speech-to-Text (Streamlit)

An offline real-time speech-to-text web app built using OpenAI Whisper, Streamlit, and WebRTC.
It captures microphone audio from the browser, processes it locally, and transcribes speech without any cloud API.


---

🚀 Features

🎤 Live microphone input via browser (WebRTC)

🧠 Offline transcription using OpenAI Whisper

⚡ Real-time processing in audio chunks

🖥️ Simple Streamlit UI

🔒 No internet needed for transcription



---

🛠️ Tech Stack

Python

Streamlit

OpenAI Whisper

streamlit-webrtc

NumPy

SoundFile

PyAV



---

📁 Project Structure

.
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation


---

📦 Installation

1️⃣ Clone the repository

git clone https://github.com/your-username/whisper-streamlit-stt.git
cd whisper-streamlit-stt

2️⃣ Create a virtual environment (recommended)

python -m venv venv
source venv/bin/activate   # Linux / macOS
venv\Scripts\activate      # Windows

3️⃣ Install dependencies

pip install -r requirements.txt


---

▶️ Run the Application

streamlit run app.py

Then open your browser at:

http://localhost:8501


---

🎙️ How It Works

1. Browser captures microphone audio using WebRTC


2. Audio frames are buffered and converted to mono


3. Buffered audio is saved temporarily as a .wav file


4. Whisper (offline) transcribes the audio


5. Transcribed text is displayed in real time
