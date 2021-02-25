import speech_recognition as sr
from gtts import gTTS
import os
import playsound


def hear():
    r3 = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak something")
        audio = r3.record(source, duration=3)
        txt = r3.recognize_google(audio)
        print(txt)
        return txt


def speak(text):
    tts = gTTS(text=text, lang="en")
    filename = "voice.mp3"
    tts.save(filename)
    print(text)
    playsound.playsound(filename)
    os.remove(filename)

