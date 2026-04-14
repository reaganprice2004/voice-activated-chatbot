import os
from dotenv import load_dotenv

load_dotenv()

RECORD_SECONDS = 5
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError("Missing OPENAI_API_KEY in .env file.")

SAMPLE_RATE = 16000
CHANNELS = 1

GENERATED_AUDIO_FOLDER = "generated_audio"
INPUT_AUDIO_FILE = os.path.join(GENERATED_AUDIO_FOLDER, "user_input.wav")
OUTPUT_AUDIO_FILE = os.path.join(GENERATED_AUDIO_FOLDER, "bot_reply.mp3")

CHAT_MODEL = "gpt-3.5-turbo"
TRANSCRIPTION_MODEL = "gpt-4o-mini-transcribe"
TTS_MODEL = "tts-1"
TTS_VOICE = "alloy"

SYSTEM_PROMPT = (
    "You are a helpful voice chatbot for an NLP final project. "
    "Keep responses conversational, clear, and under 3 sentences unless the user asks for more detail."
)

MAX_MEMORY_MESSAGES = 8