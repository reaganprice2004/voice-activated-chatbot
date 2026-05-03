import os
from openai import OpenAI
from config import (
    OPENAI_API_KEY,
    CHAT_MODEL,
    TRANSCRIPTION_MODEL,
    TTS_MODEL,
    TTS_VOICE,
    SYSTEM_PROMPT,
    MAX_MEMORY_MESSAGES
)

client = OpenAI(api_key=OPENAI_API_KEY)

conversation_history = [
    {"role": "system", "content": SYSTEM_PROMPT}
]
def safety_check(user_text):
    blocked_terms = [
        "password",
        "api key",
        "social security",
        "ssn",
        "credit card",
        "bank account",
        "routing number",
        "home address"
    ]

    lowered_text = user_text.lower()

    for term in blocked_terms:
        if term in lowered_text:
            return False, "For privacy reasons, please do not share sensitive personal information."

    return True, ""

def transcribe_audio(filename):
    with open(filename, "rb") as audio_file:
        transcript = client.audio.transcriptions.create(
            model=TRANSCRIPTION_MODEL,
            file=audio_file
        )
    return transcript.text.strip()


def get_chat_response(user_text):
    safe, safety_message = safety_check(user_text)

    if not safe:
        return safety_message

    conversation_history.append({"role": "user", "content": user_text})

    try:
        response = client.chat.completions.create(
            model=CHAT_MODEL,
            messages=conversation_history,
            temperature=0.7,
            max_tokens=200
        )

        reply = response.choices[0].message.content.strip()
        conversation_history.append({"role": "assistant", "content": reply})

        trim_memory()
        return reply

    except Exception:
        return "Sorry, I had trouble generating a response. Please try again."

def trim_memory():
    if len(conversation_history) > MAX_MEMORY_MESSAGES + 1:
        system = conversation_history[0]
        recent = conversation_history[-MAX_MEMORY_MESSAGES:]
        conversation_history.clear()
        conversation_history.append(system)
        conversation_history.extend(recent)


def generate_speech(text, filename):
    if os.path.exists(filename):
        os.remove(filename)

    speech = client.audio.speech.create(
        model=TTS_MODEL,
        voice=TTS_VOICE,
        input=text
    )

    with open(filename, "wb") as f:
        f.write(speech.read())