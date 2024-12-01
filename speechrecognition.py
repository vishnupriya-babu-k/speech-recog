import pyttsx3
import speech_recognition as sr
from datetime import datetime

def speak(w):
    engine = pyttsx3.init()
    engine.say(w)
    engine.runAndWait()

while True:
    r = sr.Recognizer()
    with sr.Microphone() as src:
        r.adjust_for_ambient_noise(src, duration=2)
        print("Speak now")
        try:
            aud = r.listen(src, timeout=1)  # Adjust the timeout parameter as needed
            words = r.recognize_google(aud)
            print("You said " + words)
        except sr.WaitTimeoutError:
            print("Listening timed out while waiting for phrase to start")
            continue

    if "hello" in words:
        print("Hello to you too!")
        speak("Hello to you too")
    elif "how are you" in words:
        print("I am fine, thanks")
        speak("I am fine, thanks")
    elif "goodbye" in words:
        print("Goodbye to you too!")
        speak("Goodbye to you too")
        break
    elif "what is your name" in words:
        print("My name is Vishnu's Chatbot")
        speak("My name is Vishnu's Chatbot")
    elif "what time is it" in words:
        now = datetime.now()
        current_time = now.strftime("%H:%M")
        print(f"The current time is {current_time}")
        speak(f"The current time is {current_time}")
    else:
        print("Huh?!")
        speak("huh?")