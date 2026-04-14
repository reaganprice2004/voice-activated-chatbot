from config import (
    RECORD_SECONDS,
    GENERATED_AUDIO_FOLDER,
    INPUT_AUDIO_FILE,
    OUTPUT_AUDIO_FILE
)
from audio_utils import ensure_audio_folder_exists, record_audio, play_audio
from chatbot import transcribe_audio, get_chat_response, generate_speech

print("app.py started")

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

            generate_speech(bot_reply, OUTPUT_AUDIO_FILE)
            play_audio(OUTPUT_AUDIO_FILE)

        except Exception as error:
            print("An error occurred:", error)

if __name__ == "__main__":
    main()