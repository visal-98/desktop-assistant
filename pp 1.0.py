import pyttsx3 #pip install
import datetime
import speech_recognition as sr #speech 
import wikipedia
import webbrowser

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time=datetime.datetime.now().strftime("%I:%M %S") #24HR TIME
    talk('current time is '+ Time)

def date():
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    date = datetime.datetime.now().day
    talk('the current date is')
    talk(date)
    talk(month)
    talk(year)

def wishme():
    talk("welcome sir!")
    time()

    hour =datetime.datetime.now().hour
    if hour>=6 and hour<12:
        talk("good morning sir!")
    elif hour>=12 and hour<18:
        talk("good afternoon sir!")
    elif hour>=18 and hour<24:
        talk("good Evening sir!")
    else:
        talk("woo ... its sleeping time")

    talk("pp 1.O at your service....,Please tell me how can i help you..?")

def command():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recogniging...")
        query = r.recognize_google(audio,language='en-us')
        print(query)

    except Exception as e:
        print(e)
        print("please give me any instruction or say ofline...")
        return "None"
    return query

if __name__ == "__main__":
    wishme()

    while True:
        query = command().lower()

        if 'time' in query:
            time()
        elif 'date' in query:
            date()
        elif 'wikipedia' in query:
            talk("searching...")
            person=query.replace('wikipedia', '')
            info=wikipedia.summary(person, 1)
            print(info)
            talk(info)
        elif 'what is' in query:
            talk("searching...")
            person=query.replace('what is', '')
            info=wikipedia.summary(person, 1)
            print(info)
            talk(info)
        elif 'play' in query:
            song = query.replace('play', '')
            talk('playing on youtube' + song)
            webbrowser.open('https://www.youtube.com/results?search_query='+song)
        elif 'hello' in query:
            talk('hello')
        elif 'hai' in query:
            talk('hello')
        elif 'date' in query:
            talk('sorry, I have a headache')
        elif 'are you single' in query:
            talk('I am in a relationship with wifi')
        elif 'how are you' in query:
            talk('thank you, i am fine .... you?')
        elif 'who are you' in query:
            talk('I am pp 1.O ... your assistant,...developed by vishal')
        elif 'search' in query:
            talk('what should i search for')
            search_Term = command().lower()
            talk('searching...')
            webbrowser.open('https://www.google.com/search?q='+search_Term)
        elif 'where is' in query:
            query = query.replace('where is','')
            loctaion = query
            talk("you asked me to locate"+loctaion)
            webbrowser.open("https://www.google.com/maps/place/"+loctaion)
        elif 'youtube' in query:
            talk('please wait a second...')
            webbrowser.open("https://youtube.com")
        elif 'google' in query:
            talk('please wait a second...')
            webbrowser.open("https://google.com")
        elif 'gmail' in query:
            talk('please wait a second...')
            webbrowser.open("https://gmail.com")
        elif 'whatsapp' in query:
            talk('please wait a second...')
            webbrowser.open("https://web.whatsapp.com/")
        elif 'offline' in query:
            talk('going ofline sir!..Have A nice Day...')
            quit()
    else:
        talk('Please tell me again.')
        