
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
if __name__ == "__main__":
    speak('Hii Pratyush how are you')

import datetime

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak('Good Morning!')
    elif hour>=12 and hour<18:
        speak('Good Afternoon!')
    else:
        speak('Good Evening!')
    speak('I am Jarvis sir. Please tell me how may I help you')
    

import speech_recognition as sr
def takeCommand():
    # it takes microphones input from the user and returns string output
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listenting....')
        r.pause_threshold = 0.8  # pause_threshold = second of non-speacking audio before a phrase is considered complete
        audio = r.listen(source)
        
    try:
        print('Recognizing....')
        query = r.recognize_google(audio, language='en-in')
        print(f'user said: {query}\n')
        
    except Exception as e:
        #print(e)
        print('Say that again please...')
        return 'None'
    return query



if __name__ == "__main__":
    wishMe()
    #while True:
    if 1:
        query = takeCommand().lower()
        # logic for executing task based on query

        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences=2)
            speak('According to wikipedia')
            print(results)
            speak(results)
        
        elif 'open youtube' in query:
            webbrowser.open('youtube.com')

        elif 'open google' in query:
            webbrowser.open('google.com')

        elif 'open stackoverflow' in query:
            webbrowser.open('stackoverflow.com')

        elif 'play music' in query:
            music_dir = 'D:\\music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime('%H:%M%S')
            speak(f'sir, the time is {strTime}')

        elif 'open code' in query:
            codePath = "C:\\Users\\hp\\AppData\\Local\\Programs\\Microsoft VS Code\Code.exe"
            os.startfile(codePath)

        