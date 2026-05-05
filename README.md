# 🎤 Voice Chatbot

**Course:** CSC 433: Natural Language Processing

**Timeline:** February 2026-April 2026

---

## 🗺️ Overview
This project implements a **voice-activated chatbot** that processes spoken input and generates spoken responses. It demonstrates a complete NLP pipeline integrating:
- Speech recognition
- Language modeling
- Speech synthesis  

The system enables real-time voice interaction between a user and an AI model.

---

## 🎯 Project Objectives
- Build an end-to-end voice interaction system  
- Convert speech input into text using ASR  
- Generate responses using a GPT-based model  
- Convert responses back into speech using TTS  
- Demonstrate a fully integrated NLP pipeline  

---

## 🧹 System Pipeline
1. Record user speech from microphone  
2. Convert speech to text (ASR)  
3. Generate response using GPT model  
4. Convert response to speech (TTS)  
5. Play response audio  

---

## ⚙️ Features
- Speech-to-text (microphone input)  
- GPT-based chatbot responses  
- Text-to-speech output  
- Short-term conversation memory  
- End-to-end voice interaction pipeline  
- System prompt for controlled and concise responses  
- Basic safety and privacy guardrails  
- Multilingual input support  
- Optional browser-based user interface (Gradio)    

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

### 4. Run with browser interface (optional)
`python app.py --ui`

This launches a simple web interface using Gradio.  
Open the provided local URL (typically http://127.0.0.1:7860) in your browser.

---

## 🧪 Current Status
- Core functionality is complete  
- Voice input → response → audio output is working    
- Safety and privacy guardrails are implemented  
- Optional user interface has been added  
- Further improvements will focus on usability and performance    

---

## ⚠️ Notes
- Microphone access must be enabled  
- `.env` file is excluded for security  
- Audio files are not stored in the repository  

---

## 🔮 Future Improvements
- Full voice input/output support in the web interface  
- Real-time voice activity detection (instead of fixed recording time)  
- More advanced safety filtering and moderation  
- Improved conversation memory (long-term context)  
- Deployment to a public platform (e.g., Hugging Face Spaces)  
- Reduced latency and faster response times  

---

## 🔒 Safety & System Behavior
The chatbot includes basic safety and privacy guardrails to prevent misuse and protect user data.

- The system prompt guides the chatbot to remain helpful, concise, and safe
- The chatbot avoids handling sensitive personal information such as:
  - Passwords
  - API keys
  - Social Security numbers
  - Credit card or banking information
  - Home addresses
- Harmful, unsafe, or illegal requests are not fulfilled
- For medical, legal, or financial topics, the chatbot provides general guidance only

These safeguards are implemented using both prompt design and simple input filtering.

---

## 📚 Technologies Used
- Python
- OpenAI API
- SoundDevice (audio input)
- Pygame (audio output)
- Gradio (user interface)

---

## 🎯 Description
This project demonstrates an end-to-end NLP system combining:
- Speech Recognition (ASR)
- Transformer-based Language Modeling
- Text-to-Speech (TTS)

---

## 📸 Screenshots
Screenshots of full voice interaction shown below, with both input from speech from user and output from bot demonstrated fully.
<img width="1343" height="557" alt="Screenshot 2026-04-14 213500" src="https://github.com/user-attachments/assets/ef81f2d9-fcf2-4a20-bdea-96f305c0b894" />
<img width="1341" height="372" alt="Screenshot 2026-04-14 213805" src="https://github.com/user-attachments/assets/86d7c661-1a98-4afe-9348-26980c2613a8" />

