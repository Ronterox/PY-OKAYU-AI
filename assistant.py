import owner_info as owner
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import subprocess
import tkinter

engine = pyttsx3.init()


def speak(text):
    print(text)
    engine.say(text)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Hello. Good Morning " + owner.NAME)
    elif hour >= 12 and hour < 18:
        speak("Hello. Good Afternoon " + owner.NAME)
    else:
        speak("Hello. Good Evening " + owner.NAME)


def getStatement():
    speak("\nWhatdoyouneed?" + owner.NAME)
    return input('Response: ').lower()


def checkStatement(statement):
    if 'wikipedia' in statement:
        speak('Let me look that up in wikipedia...')
        statement = statement.replace("wikipedia", "")
        try:
            results = wikipedia.summary(statement, sentences=1)
            speak("According to Wikipedia")
            speak(results)
        except:
            speak("Try to be more specific! There\'s a lot of options")
    elif 'search' in statement or "look for" in statement:
        statement = statement.replace("search for", "")
        statement = statement.replace("search", "")
        statement = statement.replace("look for", "")
        webbrowser.get(owner.chrome_path).open_new_tab(
            "https://www.google.com/search?q={}".format(statement))
    elif 'youtube' in statement or 'open youtube' in statement:
        if statement == 'youtube' or statement == 'open youtube':
            speak('I will open youtube then...')
            webbrowser.get(owner.chrome_path).open('youtube.com')
        else:
            statement = statement.replace('open youtube', "")
            statement = statement.replace('youtube', "")
            speak(f'I will look for {statement} on youtube then...')
            webbrowser.get(owner.chrome_path).open('https://www.youtube.com/results?search_query={}'.format(statement))
    elif 'okayu' in statement:
        speak('I gotchu bro!')
        webbrowser.get(owner.chrome_path).open(
            'https://www.youtube.com/channel/UCvaTdHTWBGv3MKj3KVqJVCw')
    elif 'play music' in statement:
        speak('Ya like jaazz?')
        os.startfile(
            os.path.join(owner.songsDir,
                         os.listdir(owner.songsDir)[0]))
    elif 'time' in statement:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"{owner.NAME} The time is {strTime}")
    elif "shutdown" in statement or "sign out" in statement or "log off" in statement:
        speak("Ok , your pc will log off in 5 seconds, make sure you exit from all applications")
        subprocess.call(["shutdown", "/s", "/t", "5"])
    elif "call me" in statement or "change name" in statement:
        if"call me" in statement:
            statement = statement.replace("call me", "")
            owner.NAME = statement
        else:
            speak("What do you want me to call you?")
            owner.NAME = input()
    elif 'goodbye' in statement or 'bye' in statement or 'see ya' in statement or 'cya' in statement or 'exit' in statement:
        speak("See ya")
        return True
    return False

#window = tkinter.Tk()
#window.geometry('400x300')
#window.mainloop()
wishMe()
statement = getStatement()
speak("Did you say: " + statement)
while not checkStatement(statement):
    statement = getStatement()