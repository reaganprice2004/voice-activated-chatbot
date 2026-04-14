import os
import time
import sounddevice as sd
from scipy.io.wavfile import write
import pygame
from config import SAMPLE_RATE, CHANNELS


def ensure_audio_folder_exists(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)


def record_audio(filename, seconds):
    print("\nRecording... Speak now.")
    audio_data = sd.rec(
        int(seconds * SAMPLE_RATE),
        samplerate=SAMPLE_RATE,
        channels=CHANNELS,
        dtype="int16"
    )
    sd.wait()
    write(filename, SAMPLE_RATE, audio_data)
    print("Recording complete.")


def play_audio(filename):
    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        time.sleep(0.1)