import pyttsx3
import speech_recognition as sr
import webbrowser
import random
from datetime import date
from datetime import datetime

today = date.today()
#print("Today's date:", today)

Assistant = pyttsx3.init('sapi5')
voices = Assistant.getProperty('voices')
Assistant.setProperty('voices', voices[0].id)

file_jokes = open("jokes.txt", "r")
file_jokes_read = file_jokes.read()
file_jokes.close()


def speak(audio):
    print('    ')
    Assistant.say(audio)
    Assistant.runAndWait()


def takecommand():
    command = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        command.pause_threshold = 1
        audio = command.listen(source)

        try:
            print('Recognizing...')
            query = command.recognize_google(audio, language='en-in')
            print(f"Ahmad main said: {query.lower()}")

        except Exception as Error:
            return "none"

        return query.lower()


speak("Hi Ahmad main! Whats up?")

while True:

    reiterator = True
    query = takecommand()
    query.lower()   

    if reiterator:     
        if "search on google" in query:
            speak("Searching")
            x = query.strip()
            webbrowser.open('https://google.com/search?q=' + x[16:])
            speak("Command completed.")
            reiterator = False

    if reiterator:
        if "search on youtube" in query:
            speak("Searching")
            yt = query.strip()
            webbrowser.open('https://www.youtube.com/results?search_query=' + yt[17:])
            speak("Command completed.")
            reiterator = False

    if reiterator:
        if 'joke' in query:
            jokes_list = file_jokes_read.split(",")
            #print(jokes_list)
            index_joke = random.randint(0, len(jokes_list)-1)
            #print(index_joke)
            speak(str(jokes_list[index_joke]))
            reiterator = False

    if reiterator:
        if 'Good night' in query:
            speak("Good night")
            reiterator = False

    if reiterator:
        if 'date' in query:
            # Textual month, day and year	
            d2 = today.strftime("%B %d, %Y")
            #print("d2 =", d2)   
            speak(d2)
            reiterator = False

    if reiterator:
        if "time" in query:
            now = datetime.now()
            current_time = str(now.strftime("%H:%M:%S"))
            list_time = current_time.split(":")
            speak(f"The time is {list_time[0]} hours, {list_time[1]} minutes, and {list_time[2]} seconds.")
            reiterator = False

    if reiterator:
        if 'exit' or 'Bye' in query:
            speak("Goodbye, see you later")
            reiterator = False
            exit()
        
    
    





