from http import server
import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import wikipedia
import smtplib
import webbrowser as wb


engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
newVoiceRate = 150
engine.setProperty('rate', newVoiceRate)

def speak(audio):
    
    engine.say(audio)
    engine.runAndWait()

def time():
    time = datetime.datetime.now().strftime("%I:%M:%S")
    speak(time)

def date():
    year =int(datetime.datetime.now().year)
    month =int(datetime.datetime.now().month)
    date =int(datetime.datetime.now().day)
    speak("the current date is "+str(date)+str(month)+str(year))

def wishme():
    speak("Welcome back sir!")
  
    hour = datetime.datetime.now().hour
    if hour >=6 and hour <=12:
        speak("Good morning ")
    elif hour >=12 and hour < 18:
        speak("Good afternoon ")
    elif hour >=18 and hour <=24:
        speak("Good Evening ")
    speak("At your service sir!")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio =r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language= 'en=IN')
        print(query)
    except Exception as e:
        print(e)
        speak("I beg your pardon...")
        return "None"
    return query


def sendmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login("sohamup13@gmail.com","onnlhxgrhdvdecxu")
    server.sendmail("sohamup13@gmail.com",to,content)
    server.close()

if __name__== "__main__":
 #   wishme()
    while True:
        query = takeCommand().lower()
        print(query)

        if "time" in query:
            time()

        elif "date" in query:
            date()
        elif "offline" in query:
            quit()
        elif "wikipedia" in query:
            speak("Searching...")
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query,sentences=2)
            speak(result)

        elif "send email" in query:
            try:
                speak("What is the content? ")
                content= takeCommand()
                speak("Who is the receiver? ")
                fto = takeCommand().replace(" ","")
                to= str(fto) + "@gmail.com"
                sendmail(to,content)
                speak("Mail sent successfully")
            except Exception as e:
                print(e)
                speak("Unable to send the mail")
            
        elif "youtube" in query:
            query = query.replace("youtube","")
            
            #chromepath = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s"
            url = "https://www.youtube.com/results?search_query=" + query
            wb.get().open(url)
            #wb.get(chromepath).open_new_tab(search+ ".com")

        elif "play" in query:
            query=query.replace("play","")
            url="https://open.spotify.com/search/"+query
            wb.get().open(url)
