import speech_recognition as sr

r = sr.Recognizer()

while True:
    with sr.Microphone() as source:
        print("\nSpeak (say 'stop' to exit)...")

        r.adjust_for_ambient_noise(source, duration=1)

        try:
            audio = r.listen(source)

            text = r.recognize_google(audio)
            print("You said:", text)

            if "stop" in text.lower():
                print("Program stopped.")
                break

        except sr.UnknownValueError:
            print("Could not understand audio.")
        except sr.RequestError as e:
            print("Error:", e)
