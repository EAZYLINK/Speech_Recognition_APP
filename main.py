import datetime
from AppOpener import open, close
import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


while True:
    def take_command():
        try:
            with sr.Microphone() as source:
                print("Listening...")
                talk("Listening")
                voice = listener.listen(source)
                command = listener.recognize_google(voice)
                command = command.lower()
        except:
            talk("You didn't say anything...")
            exit()
        return command


    def run_voice_assistant():
        command = take_command()
        if command is not None:
            print(command)
            if 'play' in command:
                song = command.replace('play', '')
                talk('Playing some song...' + song)
                pywhatkit.playonyt(song)
            elif 'time' in command:
                time = datetime.datetime.now().strftime('%H:%M')
                print(time)
                talk('Current time is ' + time)
            elif 'what is' or 'who is' in command:
                search = command.replace('what is' or 'who is', '')
                info = wikipedia.summary(search, 1)
                print(info)
                talk(info)
            else:
                talk("I don't understand what you said")
        else:
            talk("You have not said anything")

    run_voice_assistant()
