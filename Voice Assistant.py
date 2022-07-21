
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser


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

if __name__ == "__main__":
    wishMe()


    import speech_recognition as sr
def takeCommand():
    
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listenting....')
        r.pause_threshold = 0.8  
        audio = r.listen(source)
        
    try:
        print('Recognizing....')
        query = r.recognize_google(audio, language='en-in')
        print(f'user said: {query}\n')
        
    except Exception as e:
        
        print('Say that again please...')
        return 'None'
    return query

    if __name__ == "__main__":
            wishMe()

if 1:
        query = takeCommand().lower()
        

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


        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime('%H:%M%S')
            speak(f'sir, the time is {strTime}')

        