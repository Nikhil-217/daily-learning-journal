import speech_recognition as sr
from googletrans import Translator
from datetime import datetime
import os

# Initialize
recognizer = sr.Recognizer()
translator = Translator()

# Microphone tuning
recognizer.pause_threshold = 2.5
recognizer.dynamic_energy_threshold = False
recognizer.energy_threshold = 500

FILE_NAME = "translations.txt"

# Create translation history file if it doesn't exist
if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        f.write("ENGLISH → TELUGU TRANSLATION HISTORY\n")
        f.write("=" * 60 + "\n\n")

print("=" * 60)
print("English → Telugu Voice Translator")
print("Speak naturally.")
print("Say 'stop' anytime to exit.")
print("=" * 60)

while True:
    try:
        with sr.Microphone() as source:
            print("\nListening...")

            # Calibrate for room noise
            recognizer.adjust_for_ambient_noise(source, duration=1)

            audio = recognizer.listen(
                source,
                timeout=5,          # wait max 5 sec for speech to start
                phrase_time_limit=180  # max 3 min recording
            )

        print("Processing speech...")

        # Speech → Text
        english_text = recognizer.recognize_google(audio).strip()

        print(f"\nRecognized: [{english_text}]")

        # Exit condition
        if "stop" in english_text.lower():
            print("\nTranslator stopped.")
            break

        # Translate
        result = translator.translate(
            english_text,
            src="en",
            dest="te"
        )

        telugu_text = result.text

        print("\nEnglish:")
        print(english_text)

        print("\nTelugu:")
        print(telugu_text)

        # Save to file
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open(FILE_NAME, "a", encoding="utf-8") as f:
            f.write(f"Time    : {timestamp}\n")
            f.write(f"English : {english_text}\n")
            f.write(f"Telugu  : {telugu_text}\n")
            f.write("-" * 60 + "\n")

        print("\nSaved to translations.txt")

    except sr.WaitTimeoutError:
        print("\nNo speech detected for 5 seconds.")

    except sr.UnknownValueError:
        print("\nCould not understand the speech. Please try again.")

    except sr.RequestError as e:
        print(f"\nSpeech recognition service error: {e}")

    except Exception as e:
        print(f"\nUnexpected error: {e}")
