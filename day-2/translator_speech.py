import speech_recognition as sr
from googletrans import Translator
from datetime import datetime

recognizer = sr.Recognizer()
translator = Translator()

filename = "translations.txt"

# Create file with heading if it doesn't exist
try:
    open(filename, "x", encoding="utf-8").write(
        "English to Telugu Translation History\n"
        + "=" * 50
        + "\n\n"
    )
except FileExistsError:
    pass

print("English → Telugu Voice Translator Started")
print("Say 'stop' to exit.\n")

while True:
    try:
        with sr.Microphone() as source:
            print("Listening...")

            recognizer.adjust_for_ambient_noise(source, duration=1)

            audio = recognizer.listen(
                source,
                timeout=5,
                phrase_time_limit=20
            )

        english_text = recognizer.recognize_google(audio)

        print("\nEnglish :", english_text)

        if english_text.lower().strip() == "stop":
            print("Translator stopped.")
            break

        translated = translator.translate(
            english_text,
            src='en',
            dest='te'
        )

        telugu_text = translated.text

        print("Telugu  :", telugu_text)

        timestamp = datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )

        with open(filename, "a", encoding="utf-8") as file:
            file.write(f"Time: {timestamp}\n")
            file.write(f"English: {english_text}\n")
            file.write(f"Telugu : {telugu_text}\n")
            file.write("-" * 50 + "\n")

        print("Saved to translations.txt\n")

    except sr.WaitTimeoutError:
        print("No speech detected for 5 seconds.\n")

    except sr.UnknownValueError:
        print("Could not understand audio.\n")

    except Exception as e:
        print("Error:", e)
