import pyttsx3
import pyaudio
import datetime
import webbrowser
import wikipedia
import os
import sys
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def wish_me():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak('Good Morning!')

    elif 12 <= hour < 18:
        speak('Good Afternoon!')

    else:
        speak('Good Evening!')

    speak('Jarvis is online. Please tell me how may I help you.')

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        r.energy_threshold = 100 
        audio = r.listen(source)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language = 'en-in')
        print(f'User Said: {query}\n')       

    except Exception as e:
        print(e)
        speak('Say that again please...')
        return "None"
    return query

if __name__ == "__main__":
    wish_me()

    while True:
        query = take_command().lower()

        if 'who are you' in query or 'introduce yourself' in query:
            speak('I am Jarvis, your personal Desktop assistant... Version 1.1.0. Speed Unknown...')

        elif 'who wrote you' in query or 'introduce me' in query or 'introduce mi' in query or 'who am i' in query:
            speak('You are Seraj Muneer Faridy, Siri for short... ')

        elif 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences = 2)
            speak('According to Wikipedia...')
            speak(results)
            print(results)

        elif 'open youtube' in query:
            speak('Opening Youtube...')
            webbrowser.open('www.youtube.com')

        elif 'search youtube' in query:
            speak('What should I search?')
            query = take_command()
            speak('Initiating Youtube Search Sequence!')
            webbrowser.open(f'https://www.youtube.com/results?search_query={query}')

        elif 'open google' in query:
            speak('Opening Google...')
            webbrowser.open('www.google.com')

        elif 'search google' in query:
            speak('What should I search?')
            query = take_command()
            speak('Initiating Google Search Sequence!')
            webbrowser.open(f'https://www.google.com/search?q={query}')

        elif 'open duolingo' in query:
            speak('Opening Duolingo...')
            webbrowser.open('www.duolingo.com/learn')

        elif 'open w3 schools' in query or 'open w 3 schools' in query:
            speak('Opening W3 Schools...')
            webbrowser.open('www.w3schools.com')

        elif 'open w3 html' in query or 'open w 3 html' in query:
            speak('Opening W3 HTML...')
            webbrowser.open('www.w3schools.com/html/default.asp')

        elif 'open w3 css' in query or 'open w 3 css' in query:
            speak('Opening W3 CSS...')
            webbrowser.open('www.w3schools.com/css/default.asp')

        elif 'open w3 javascript' in query or 'open w 3 javascript' in query:
            speak('Opening W3 Javascript...')
            webbrowser.open('www.w3schools.com/javascipt/default.asp')

        elif 'open chrome' in query:
            speak('Opening Google Chrome...')
            chrome = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(chrome)  

        elif 'exit' in query or 'quit' in query or 'abort' in query:
            speak('Initiating Exit Sequence!')
            break

        elif 'shutdown' in query or 'shut down' in query:
            speak('Initiating Shutdown Sequence!')
            speak('Terminating All Executable Files!')
            os.system('shutdown /s /f /t 0')