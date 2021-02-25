import speech_recognition as sr
from gtts import gTTS
import os
import playsound


def speak(text):
    tts = gTTS(text=text, lang="en")
    filename = "voice.mp3"
    tts.save(filename)
    print(text)
    playsound.playsound(filename)
    os.remove(filename)


def hear():
    r3 = sr.Recognizer()
    with sr.Microphone() as source:
        while True:
            print("Speak something")
            audio = r3.record(source, duration=3)
            try:
                txt = r3.recognize_google(audio)
                print(txt)
                return txt
            except:
                speak("Say now")



