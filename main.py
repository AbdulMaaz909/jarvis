import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests


recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "99dfcc595cb0635be520a70730e65802"

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processcommand(c):
    if "open google" in c.lower ():
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower ():
        webbrowser.open("https://youtube.com")
    elif "open facebook" in c.lower ():
        webbrowser.open("https://facebook.com")
    elif "open github" in c.lower ():
        webbrowser.open("https://github.com")
    elif "open playstore" in c.lower ():
        webbrowser.open("https://playstore")
    elif c.lower().startswith("play"):
        song= c.lower().split(" ")[1]  #play skyfall ['play','pathan'] indexing 1 (split means space)
        link= musicLibrary.music[song]
        webbrowser.open(link)
    
    elif "news" in c.lower():
        r = requests.get(f"https://newsdata.io/api/1/latest?apikey={newsapi}")
        if r.status_code ==200:
            #parse the JSON response
            data= r.json()

            #extrat the articles
            articles = data.get('articles',[])

            for article in articles:
                speak(article['title']) 

    
    

if __name__=="__main__":
    speak("Initializing Jarvis...")
    while True:
        r =sr.Recognizer()

        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("listening...")
                audio = r.listen(source,timeout=3,phrase_time_limit=2)
            word = r.recognize_google(audio)
            if(word.lower() == "jarvis"):
                speak("Yes Abdul Maaz")
                #listen for command 
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processcommand(command)

        except Exception as e:
            print("Error; {0}".format(e))




