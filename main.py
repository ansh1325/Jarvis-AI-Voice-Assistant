print("Radhey Radhey")
import speech_recognition as sr
import pyaudio
import webbrowser
import requests
from openai import OpenAI
from gtts import gTTS
import pygame
import os
import google.generativeai as genai

genai.configure(api_key="AIzaSyDVT1ZvpJw6oepMTBmn1obaYBNFOuo2GKk")

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "1"

def ai(command):
    model = genai.GenerativeModel("gemini-2.5-pro")
    response = model.generate_content(
        f"You are Jarvis, a concise virtual assistant. "
        f"Always respond in under 2 sentences. "
        f"User: {command}"
    )
    text = "".join([p.text for p in response.candidates[0].content.parts if p.text])
    print(text)
    return text



recognizer=sr.Recognizer()
newsapi="83f79fbf525f4761866df95ff0d9c3ab"

    
def speak(text):
    tts = gTTS(text)
    tts.save('temporary.mp3')
    pygame.mixer.init()
    pygame.mixer.music.load('temporary.mp3')
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    pygame.mixer.music.unload()
    os.remove('temporary.mp3')


music={
    "at peace":"https://youtu.be/jVVwYXV22zg?si=TJ31tLIXn3OKfG4q",
    "champions anthem":"https://youtu.be/BwfjneL67ZU?si=5tO3a1vgvj2rlzuy",
    "52 bars":"https://youtu.be/4DfVxVeqk2o?si=bFdsy7v-SoOXa7AS",
    "wavy":"https://youtu.be/XTp5jaRU3Ws?si=SPNrAJKC1qfoEQqN",
    "sirra":"https://youtu.be/knGCfzm4jWs?si=JEZR9xA7utLv2XUd",
    "arjan vailly":"https://youtu.be/zqGW6x_5N0k?si=_BLQ14TgyJNuDGaD",
    "raj karega khalsa":"https://www.youtube.com/watch?v=gftrEAfkK9U&pp=ygURcmFqIGthcmVnYSBraGFsc2E%3D",
    "russian bandana":"https://youtu.be/1OAjeECW90E?si=XI7k-JFpI71GyGYf"
}

def processcommand(c):
    
    if "open google" in c.lower():
        webbrowser.open("https://www.google.com/")
    elif "open youtube" in c.lower():
        webbrowser.open("https://www.youtube.com/")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://www.linkedin.com/")
    elif 'open instagram' in c.lower():
        webbrowser.open("https://www.instagram.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://www.facebook.com/")
    elif c.lower().startswith("play"):
        song=c.lower().replace("play","",1).strip()
        link=music[song]
        webbrowser.open(link)
    elif "news" in c.lower():
        r= requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
        if r.status_code==200:
            data=r.json()
            articles=data.get('articles',[])
            for article in articles:
                print(article["title"])
                speak(article["title"])
    else:
        result=ai(c)
        speak(result)

if __name__=="__main__":
    speak("Initializing Jarvis")
    while True:
        r=sr.Recognizer()
        print("Recognizing..")
        try:
            with sr.Microphone() as source:
                print("Listening..")
                audio=r.listen(source,timeout=3,phrase_time_limit=3)
            word=r.recognize_google(audio)
            if("jarvis" in word.lower()):
                print("Jarvis listened ")
                speak("Yes")
                with sr.Microphone() as source:
                    print("Jarvis Active ")
                    audio=r.listen(source)
                    command=r.recognize_google(audio)
                    if command.lower().startswith("exit"):
                        speak("Goodbye!")
                        break

                    processcommand(command)
        except Exception as e:
            print("error",e)