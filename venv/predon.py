import speech_recognition as sr
import datetime
import wikipedia
import pyttsx3
import webbrowser
import random
import os
import math
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices)
engine.setProperty('voice', voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wish():
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour<12:
        print("Assistant: Good morning sir i am IVA your artificial assistant")
        speak("good morning sir i am IVA your artificial assistant")
    elif hour>=12 and hour<16:
        print("Assistant: Good afternoon sir i am IVA your artificial assistant")
        speak("good afternoon sir i am IVA your artificial assistant")
    elif hour>=16 and hour<18:
        print("Assistant: Good evening sir i am IVA your artificial assistant")
        speak("good evening sir i am IVA your artificial assistant")
    else:
        print("Assistant: Good night sir i am IVA your artificial assistant")
        speak("good night sir i am IVA your artificial assistant")
    print("Assistant: How may i help you sir")
    speak("How may i help you sir")
def takecom():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        audio = r.listen(source, phrase_time_limit=5)
    try:
        print("Recognising..")
        text = r.recognize_google(audio, language='en-in')
        print("you:", text)
        return text
    except execption:
        speak("error....")
        print("Network connection error")
        return "none"
if __name__ == "__main__":
    wish()
    while True:
        query = takecom().lower()
        if "wikipedia" in query:
            speak("searching wikipedia")
            query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            print(results)
            speak(results)
        elif 'search' in query:
            speak("searching as explorer")
            results = webbrowser.open(query)
            print(results)
            speak(results)


        # these queries are used to operate any web browser through voice command
        elif "open hotstar" in query or "hotstar" in query:
            webbrowser.open("https://www.hotstar.com/in")
            print("Assistant: opening disney + hotstar sir")
            speak("opening disney + hotstar sir")
        elif "open youtube" in query or "youtube" in query:
            webbrowser.open("https://www.youtube.com/")
            print("Assistant: opening youtube sir, enjoy youtube videos or movies")
            speak("opening youtube sir, enjoy youtube videos or movies")
        elif "open gmail" in query or "gmail" in query:
            webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
            print("Assistant: opening your gmail sir,may be you have some important work")
            speak("opening your gmail sir,may be you have some important work")
        elif "open translator" in query or "translator" in query:
            webbrowser.open("https://translate.google.com/")
            print("Assistant: opening translator sir i think you have some international talks")
            speak("opening translator sir i think you have some international talks")
        elif 'open java point' in query or "java point" in query:
            webbrowser.open("https://www.javatpoint.com/")
            print("Assistant: opening java point sir, i think you want to learn something special rather than social media")
            speak("opening java point sir, i think you want to learn something special rather than social media")
        elif 'open w3school' in query or "w3school" in query:
            webbrowser.open("https://www.w3schools.com/")
            print("Assistant: opening w3schools sir, i think you want to learn coding good i also love that")
            speak("opening w3schools sir, i think you want to learn coding good i also love that")
        elif "open google" in query or "google" in query:
            webbrowser.open("https://www.google.co.in/")
            print("Assistant: opening google sir")
            speak("opening google sir")
        elif "open facebook" in query or "facebook" in query:
            webbrowser.open("https://www.facebook.com/")
            print("Assistant: opening facebook sir")
            speak("opening facebook sir")
        elif "open instagram" in query or "instagram" in query:
            webbrowser.open("https://www.instagram.com/")
            print("Assistant: opening instagram sir")
            speak("opening instagram sir")
        elif "open news" in query or "news" in query:
            webbrowser.open("https://news.google.com/topstories?hl=en-IN&gl=IN&ceid=IN:en")
            print("Assistant: opening news sir")
            speak("opening news sir")
        elif "open twitter" in query or "twitter" in query:
            webbrowser.open("https://www.twitter.com/")
            print("Assistant: opening twitter sir")
            speak("opening twitter sir")
# these queries are used to operate any application through voice command
# give some space
# to know
        elif "chrome" in query:
            print("Assistant: opening google chrome")
            speak("opening Google Chrome")
            path = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(path)
        elif "open my file" in query:
            print("Assistant: opening my file sir")
            speak("opening my file  sir")
            path = "C:\\Mf"
            os.startfile(path)
        elif "open designer" in query:
            print("Assistant: opening qt designer sir")
            speak("opening qt designer")
            path = "C:\\Python38\\Lib\\site-packages\\QtDesigner\\designer.exe"
            os.startfile(path)
        elif "IVA open powerpoint" in query or "open powerpoint" in query:
            print("Assistant: opening power point sir")
            speak("opening power point sir")
            path = "C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"
            os.startfile(path)
        elif "IVA open word" in query or "open word" in query:
            print("Assistant: opening ms word sir")
            speak("opening ms word sir")
            path = "C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
            os.startfile(path)
        elif "IVA open excel" in query or "open excel" in query:
            print("Assistant: opening ms excel sir")
            speak("opening ms excel sir")
            path = "C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\EXCEL.EXE"
            os.startfile(path)
        elif "open calculator" in query:
            print("Assistant: opening calculator sir")
            speak("opening calculator sir")
            path = "C:\\Users\\HP\\PycharmProjects\\predon\\venv\\cal.py"
            os.startfile(path)
        elif "open pycharm" in query:
            print("Assistant: opening Pycharm sir, i think you have some pending work")
            speak("opening Pycharm sir, i think you have some pending work")
            path = "C:\\PyCharm Community Edition 2020.2.1\\bin\\pycharm64.exe"
            os.startfile(path)
        

    #    elif "activate connection mode" in query:
   #      print("Assistant: mode for activating connection is on")
  #        speak("mode for activating conection  is on")
 #          path = "C:\\Users\\HP\\PycharmProjects\\predon\\venv\\test2.py"
#            os.startfile(path)
#        elif"activate server mode" in query:
 #           print("Assistant: mode for activating connection server is on")
  #          speak("mode for activating connection server is on")
   #         path = "C:\\Users\\HP\\PycharmProjects\\predon\\venv\\animation.py"
    #        os.startfile(path)


        elif "shutdown" in query:
            speak("Assistant: shutting down sir")
            os.system('shutdown -s')
# these queries are used to talk with assistant like paradon
# give some space
# to know
        elif'goodbye' in query:
            print("Assistant: good bye sir")
            speak("good bye sir")
            exit()
        elif "good morning" in query or "good evening" in query or "good afternoon" in query or "good night" in query:
            print("Assistant: What can i do for you sir")
            speak("what can i do for you sir")
        elif "how are you" in query:
            print("Assistant: i am fine sir what about you")
            speak("i am fine sir what about you")
        elif "fine" in query:
            print("Assistant: well that is good, i am guessing that")
            speak("well that is good, i am guessing that")
        elif "not exactly" in query:
            print("Assistant: oh,maybe you fine soon")
            speak("oh,maybe you fine soon")
##
##
        elif "what is your daily work" in query or "daily work" in query:
            print("Assistant: my daily work is to help you only i am your assistant i only assist you")
            speak("my daily work is to help you only i am your assistant i only assist you")
        elif "introduction about you" in query or "introduction" in query:
            print("Assistant: well let me introduce my self my name is IVA and i am a program that is made or bulid by parmesh kumar\n"
                 " i am learn every time best through different modes and i have different types of script or packeges to learn new skills")
            speak("well let me introduce my self my name is IVA and i am a program that is made or bulid by parmesh kumar"
                 " i am learn every time best through different modes and i have different types of script or packeges to learn new skills")
        elif "ok" in query:
            print("Assistant: hmmmm")
            speak("hmmmm")
        elif "alright" in query:
            print("Assistant: yes sir")
            speak("yes sir")
        elif "be alert from hackers" in query:
            print("Assistant: Why dont you try to buy a paid antivirus to protect laptop from hackers")
            speak("Why dont you try to buy a paid antivirus to protect laptop from hackers")
        elif "wonderful performance" in query:
            print("Assistant: thank u sir its my pleasure that you are happy")
            speak("thank u sir its my pleasure that you are happy")
        elif "what is time now" in query or "time" in query:
            today = datetime.datetime.now().strftime("%H hours:%M minutes:%S seconds")
            print("Assistant: today date and time ", today)
            speak(f"today date and time {today}")
        elif "nice" in query:
            print("Assistant: yup after some time i learn more words to recognise")
            speak("yup after some time i learn more words to recognise")
        elif "thank you" in query:
            print("Assistant: welcome sir")
            speak("welcome sir")
        elif "your name full form" in query or "full form" in query:
            print("Assistant: my name full form is Intelligence voice assistant ")
            speak("my name full form is Intelligence voice assistant")
        elif "why voice assistant is also known as artificial intelligence" in query:
            print("Assistant: Voice assistant (might be also called digital, virtual or AI assistant) \nis a task-oriented programming application that recognizes human speech and carries out commands pronounced by a user.\n It is powered by AI and bases its performance on cloud storage with millions of words and phrases in it")
            speak("Voice assistant (might be also called digital, virtual or AI assistant) is a task-oriented programming application that recognizes human speech and carries out commands pronounced by a user. It is powered by AI and bases its performance on cloud storage with millions of words and phrases in it")
        elif "notedown" in query:
            file1 = open("newfile.txt","a")
            file1.write(query)
            print("Assistant: saved text")
            speak("saved text")
            file1.close()
        elif "save" in query:
            file2 = open("voicesaved.doc","a")
            file2.write(query)
            print("Assistant: saved document")
            speak("saved document")
            file2.close()
        else:
            print("Assistant: i cant recognise that")
            speak("i cant recognise that")


