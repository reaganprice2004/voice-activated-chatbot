import os
import time
import sys
from config import (
    RECORD_SECONDS,
    GENERATED_AUDIO_FOLDER,
    INPUT_AUDIO_FILE
)
from audio_utils import ensure_audio_folder_exists, record_audio, play_audio
from chatbot import transcribe_audio, get_chat_response, generate_speech

def launch_interface():
    import gradio as gr

    ensure_audio_folder_exists(GENERATED_AUDIO_FOLDER)

    def chat_interface(user_text):
        if not user_text.strip():
            return "Please enter a message."

        bot_reply = get_chat_response(user_text)
        return bot_reply

    demo = gr.Interface(
        fn=chat_interface,
        inputs=gr.Textbox(label="Type your message"),
        outputs=gr.Textbox(label="Chatbot response"),
        title="Voice-Activated Chatbot",
        description=(
            "A simple NLP final project chatbot with safety and privacy guardrails. "
            "Do not enter passwords, API keys, addresses, or financial information."
        )
    )

    demo.launch()

def main():
    print("Inside main()")
    ensure_audio_folder_exists(GENERATED_AUDIO_FOLDER)

    print("Voice Chatbot Started")
    print("Press Enter to speak.")
    print("Type q and press Enter to quit.")

    while True:
        user_choice = input("\nReady? ").strip().lower()

        if user_choice == "q":
            print("Goodbye.")
            break

        try:
            record_audio(INPUT_AUDIO_FILE, RECORD_SECONDS)

            user_text = transcribe_audio(INPUT_AUDIO_FILE)

            if not user_text:
                print("No speech detected. Please try again.")
                continue

            print("\nYou said:", user_text)

            bot_reply = get_chat_response(user_text)
            print("Bot:", bot_reply)

            output_audio_file = os.path.join(
                GENERATED_AUDIO_FOLDER,
                f"bot_reply_{int(time.time())}.mp3"
            )

            generate_speech(bot_reply, output_audio_file)
            play_audio(output_audio_file)

        except Exception as error:
            print("An error occurred:", error)


if __name__ == "__main__":
    print("app.py started")

    if len(sys.argv) > 1 and sys.argv[1] == "--ui":
        launch_interface()
    else:
        main()