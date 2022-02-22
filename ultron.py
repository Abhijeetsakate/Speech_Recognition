import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices =engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour <12:
        speak("Good Morning Sir")
    
    elif hour >=12 and hour <18:
        speak("Good Afternoon Sir")

    else:
        speak("Good Evening Sir")
    speak("Hello Sir EDITH Here")

def takecommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio)
        print("You said " + r.recognize_google(audio))
    
    except Exception as e:
        print("Say again")
        return "None"
    return query

if __name__ == "__main__":
    wishme()
    #speak("india is best")
    while True:
        query =takecommand().lower()
        
        if 'wikipedia' in query:
            speak("Searching Wikipedia......")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            speak(results)
        
        elif 'open chrome' in query:
            codepath = "C:\Program Files\Google\Chrome\Application\chrome.exe"
            os.startfile(codepath)
        
        elif 'open facebook' in query:
            webbrowser.get(path).open("facebook.com")
        
        elif 'open youtube' in query:
            webbrowser.get(path).open("youtube.com")

        elif 'open gmail' in query:
            webbrowser.get(path).open("gmail.com")