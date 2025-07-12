import streamlit as st
from streamlit_webrtc import webrtc_streamer, AudioProcessorBase
import whisper
import numpy as np
import av
import soundfile as sf
import tempfile

st.title("🎙️ Whisper Offline Speech-to-Text")

# Load Whisper model
@st.cache_resource
def load_model():
    return whisper.load_model("base")

model = load_model()

class AudioProcessor(AudioProcessorBase):
    def __init__(self):
        self.buffer = []

    def recv_queued(self, frames):
        for frame in frames:
            pcm = frame.to_ndarray()
            if pcm.ndim > 1:
                pcm = pcm.mean(axis=0)
            self.buffer.append(pcm)
        return frames[-1]

    def get_audio_buffer(self):
        if len(self.buffer) >= 50:
            audio = np.concatenate(self.buffer)
            self.buffer = []
            return audio
        return None

ctx = webrtc_streamer(
    key="whisper",
    audio_processor_factory=AudioProcessor,
    media_stream_constraints={"audio": True, "video": False}
)

if ctx.audio_processor:
    audio_data = ctx.audio_processor.get_audio_buffer()
    if audio_data is not None:
        st.info("Processing...")

        with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as f:
            sf.write(f.name, audio_data, samplerate=48000)

            try:
                result = model.transcribe(f.name)
                st.success("Transcription:")
                st.write(result["text"])
            except Exception as e:
                st.error(f"Whisper failed: {e}")
