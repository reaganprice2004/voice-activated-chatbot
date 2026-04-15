# 🎤 Voice Chatbot NLP Project

## 📌 Overview
This project implements a voice-activated chatbot that processes spoken input and returns a spoken response. It demonstrates a complete natural language processing (NLP) pipeline, including speech recognition, language modeling, and speech synthesis.

---

## ⚙️ Features
- 🎤 Speech-to-text (microphone input)
- 🤖 GPT-based chatbot responses
- 🔊 Text-to-speech output
- 🧠 Short-term conversation memory
- 🔄 End-to-end voice interaction pipeline

---

## 🧠 System Pipeline
1. Record user speech from microphone  
2. Convert speech to text (ASR)  
3. Generate response using GPT model  
4. Convert response to speech (TTS)  
5. Play response audio  

---

## 🗂️ Project Structure
```
voice_chatbot_project/
│
├── app.py # Main program loop
├── config.py # Configuration and API setup
├── audio_utils.py # Audio recording & playback
├── chatbot.py # NLP + API logic
├── requirements.txt # Dependencies
├── .env # API key (not included in repo)
├── README.md
└── generated_audio/ # Output audio files (ignored)
```
---

## 🚀 How to Run

### 1. Install dependencies
`pip install -r requirements.txt`

### 2. Add API key
Create a `.env` file:
`OPENAI_API_KEY=your_api_key_here`

### 3. Run the chatbot
`python app.py`

---

## 🧪 Current Status
- Core functionality is complete  
- Voice input → response → audio output is working  
- Further improvements will focus on usability and performance  

---

## ⚠️ Notes
- Microphone access must be enabled  
- `.env` file is excluded for security  
- Audio files are not stored in the repository  

---

## 🔮 Future Improvements
- Improved user interaction (UI/UX)
- Better response control and formatting
- Latency measurement and optimization
- Optional GUI interface

---

## 📚 Technologies Used
- Python
- OpenAI API
- SoundDevice (audio input)
- Pygame (audio output)

---

## 🎯 Description
This project demonstrates an end-to-end NLP system combining:
- Speech Recognition (ASR)
- Transformer-based Language Modeling
- Text-to-Speech (TTS)

---

## 📸 Screenshots
Screenshots of full voice interaction will be added after testing in an appropriate environment.
