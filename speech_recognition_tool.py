# Import necessary libraries
import speech_recognition as sr
import pyaudio
import time

# Constants for commands
COMMANDS = {
    "start": "Starting process...",
    "stop": "Stopping process...",
    "pause": "Pausing process...",
    "continue": "Continuing process...",
    "exit": "Exiting program..."
}

# Main recognition function
def recognize_speech():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    # Automatic mic calibration
    with mic as source:
        print("[SYSTEM] Calibrating microphone...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("[READY] Listening for commands...")

    while True:
        with mic as source:
            try:
                audio = recognizer.listen(source, timeout=5)
                command = recognizer.recognize_google(audio).lower()
                print(f"[HEARD] \"{command}\"")

                if command in COMMANDS:
                    print(f"[ACTION] {COMMANDS[command]}")
                    if command == "exit":
                        print("[SYSTEM] Exiting program...")
                        break
                else:
                    print("[WARNING] Unrecognized command.")

            except sr.WaitTimeoutError:
                print("[WARNING] Listening timed out while waiting for phrase to start.")
            except sr.UnknownValueError:
                print("[ERROR] Could not understand audio.")
            except sr.RequestError as e:
                print(f"[ERROR] Could not request results from Google Speech Recognition service; {e}")
            except Exception as e:
                print(f"[ERROR] An unexpected error occurred: {e}")

# Main program loop
if __name__ == "__main__":
    try:
        recognize_speech()
    except KeyboardInterrupt:
        print("\n[USER] Program terminated.")
