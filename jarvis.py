import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import pyjokes
import pyautogui
import wolframalpha
import time
import requests
import psutil
import sys
import random
import yfinance as yf

import developer_help

from ecapture import ecapture as ec
from urllib.request import urlopen
from bs4 import BeautifulSoup as soup

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning sir, how may I help you?")

    elif hour>=12 and hour<18:
        speak("Good Afternoon sir, how may I help you?")   

    else:
        speak("Good Evening sir, how may I help you?")  

def news():
    """
    This method will tells top 15 current NEWS
    :return: list / bool
    """
    try:
        news_url = "https://news.google.com/news/rss"
        Client = urlopen(news_url)
        xml_page = Client.read()
        Client.close()
        soup_page = soup(xml_page, "xml")
        news_list = soup_page.findAll("item")
        li = []
        for news in news_list[:15]:
            li.append(str(news.title.text.encode('utf-8'))[1:])
        return li
    except Exception as e:
        print(e)
        return False

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def battery():
    batt = str(psutil.sensors_battery())
    batt=batt.split()
    i=(batt[0].split('('))
    i=(i[1].split('='))
    print(i[1])
    speak('Sir System battery is at' + i[1]+'%')

def cpu():
    usage = str(psutil.cpu_percent())
    speak('Sir System CPU is at' + usage)

def memory():
    mem = str(psutil.virtual_memory())
    mem=mem.split(',')
    i=(mem[2].split('='))
    speak('Sir System Memory Percentage is ' +i[1]+'%' )
    j=(mem[1].split('='))
    speak('Sir System Free Memory is at' +j[1] )

def check_weather():
    api_key="14c0f7d7686b567fd266e35fe94c4dc3"
    base_url="https://api.openweathermap.org/data/2.5/weather?"
    speak("what is the city name")
    city_name=takeCommand()
    complete_url=base_url+"appid="+api_key+"&q="+city_name
    response = requests.get(complete_url)
    x=response.json()
    if x["cod"]!="404":
        y=x["main"]
        current_temperature = y["temp"]
        current_humidiy = y["humidity"]
        z = x["weather"]
        weather_description = z[0]["description"]
        speak(" Temperature in kelvin unit is " +
               str(current_temperature) +
               "\n humidity in percentage is " +
               str(current_humidiy) +
               "\n description  " +
               str(weather_description))
        print(" Temperature in kelvin unit = " +
               str(current_temperature) +
               "\n humidity (in percentage) = " +
               str(current_humidiy) +
               "\n description = " +
               str(weather_description))

if __name__ == "__main__":
    NOTE = '''
        +=======================================+
        |......JARVIS VIRTUAL INTELLIGENCE......|
        +---------------------------------------+
        |#Author: Akul Goel                     |
        |#Date: 01/06/2016                      |
        |#Changing the Description of this tool |
        | Won't made you the coder              |
        |#I don't take responsibility for       |
        | problems regarding viruses or glitches|
        +---------------------------------------+
        |......JARVIS VIRTUAL INTELLIGENCE......|
        +=======================================+
        |              OPTIONS:                 |
        |#hello/hi     #goodbye    #sleep mode  |
        |#your name    #jarvis     #what time   |
        |#asite.com    #next music #music       |
        |#pause music  #wifi       #thank you   |
        |#start/stop someapp                    |
        |#pip install/npm install               |
        +=======================================+
    '''
    print(NOTE)
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
            
        elif 'wake up' in query:
            takeCommand()
            
        elif 'goodbye' in query:
            sys.exit()
            
        elif 'go to sleep' in query:
            speak('Ok sir, I am going to sleep. You can call me back anytime.')
            break
        
        elif "what's up" in query or 'how are you' in query:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy', 'Ready to help you sir']
            speak(random.choice(stMsgs))

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open blooket' in query:
            webbrowser.open("blooket.com")

        elif 'open chrome' or 'open google' in query:
            print("Opening Chrome Browser...")
            speak("opening chrome browser")
            chrome = 'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe'
            os.startfile(os.path.join(chrome))

        elif 'close chrome' or 'close google' in query:
            print("closing Chrome Browser...")
            speak("closing chrome browser")
            os.system('TASKKILL /F /IM Google_Chrome.exe')

        elif 'volume up' in query:
            pyautogui.press("volumeup")

        elif 'volume down' in query:
            pyautogui.press("volumedown")

        elif 'volume mute' or 'mute' in query:
            pyautogui.press("volumemute")

        elif 'pip install' in query:
            developer_help.pipInstallPackage()

        elif 'battery' in query:
            battery()

        elif 'cpu' in query:
            cpu()

        elif 'memory' in query:
            memory()

        elif 'npm install' in query:
            developer_help.npmInstallPackage()

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
            time.sleep(5)

        elif 'open github' in query:
            webbrowser.open("github.com")   
            time.sleep(5)

        elif "camera" in query or "take a photo" in query:
            time.sleep(5)
            ec.capture(0,"Camera","img.jpg")

        elif ('sleep mode') in query:
            speak('good night')
            os.system('rundll32.exe powrprof.dll,SetSuspendState 0,1,0')

        elif 'log out' in query:
            speak("Sir system is logging out")
            speak("Sir Goodbye")
            os.system("shutdown -l")

        elif 'shut down' in query:
            speak("Sir system is Shuting down")
            speak("Goodbye Sir ")
            os.system("shutdown /s /t 1")

        elif 'restart' in query:
            speak("Sir system is Restarting")
            speak("Goodbye Sir ")
            os.system("shutdown /r /t 1")
            
        elif 'remember that' in query:
            speak("What should I remember?")
            data = takeCommand()
            speak("you said me to remember that"+data)
            remember = open('data.txt','w')
            remember.write(data)
            remember.close()
            speak("Sir i am Remembering Your Data")
            speak("Any thing for me Sir")
            
        elif 'do you know anything' in query:
            speak("Yes Sir")
            remember =open('data.txt', 'r')
            speak("You said me to remember that" +remember.read())

        elif "weather" in query:
            check_weather()

        elif 'screenshot' in query:
            image = pyautogui.screenshot()
            image.save('screenshot.png')
            speak('Screenshot taken')

        elif 'open visual studio code' in query:
            vscodePath = 'C:\\Users\\materialsworld\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code'
            os.startfile(vscodePath)
            
        elif "open command prompt" in query:
            speak('opening command prompt')
            os.system("start cmd")

        elif "what is my ip" in query:
            ip = requests.get("https://api.ipify.org").text
            speak(f"Your ip address is {ip}")
            print(f"Your ip address is {ip}")

        elif 'open android studio' in query:
            androidStudioPath = 'C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Android Studio'
            os.startfile(androidStudioPath)

        elif 'open google calendar' in query:
            webbrowser.open('calendar.google.com')

        elif 'change voice to female voice' in query:
            engine.setProperty('voice', voices[1].id)
            speak('Voice has been changed to female voice')
            speak('Hello,sir. I am Friday.')

        elif 'change voice to male voice' in query:
            engine.setProperty('voice', voices[0].id)
            speak('Voice has been changed to male voice')
            speak('Hello,sir. I am Jarvis.')

        elif 'play music' in query:
            music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'Hello jarvis' in query:
            speak('How are you doing, sir?')

        elif 'random joke' in query:
            random_joke = pyjokes.get_joke(language="en", category="all")
            print(random_joke)
            speak(random_joke)

        elif 'the time' in query:
            time = time.ctime().split(" ")[3].split(":")[0:2]  
            if time[0] == "00":  
                hours = '12'  
            else:  
                hours = time[0]  
            minutes = time[1]  
            time = f'{hours} {minutes}'  
            speak(time)  

        elif 'open the folder Professional Apps' in query:
            folderPath = "C:\\Users\\materialsworld\\Desktop\\Akul Goel\\Professional Apps"
            os.startfile(folderPath)

        elif 'open the folder Akul Whitehat' in query:
            folder1Path = "C:\\Users\\materialsworld\\Desktop\\Akul Goel\\Akul Whitehat"
            os.startfile(folder1Path)

        elif 'news' in query:
            news()

        elif 'ask' in query:
            speak('I can answer to computational and geographical questions. What question do you want to ask me')
            question = takeCommand()
            app_id="TTXXJU-JKXAR7LYX3"
            client = wolframalpha.Client('TTXXJU-JKXAR7LYX3')
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)

        elif 'open w3schools' in query:
            webbrowser.open("w3schools.com")

        elif 'who made you' in query:
            speak('Akul Goel made me.')

        elif 'thank you' in query:
            speak('Of course, sir. No need to thank me')

        elif 'what can you do' in query:
            speak('I can click screenshots of your current screen, click a photo using your camera and do much more. I have a list of commands to help you.')
            print(NOTE)
            
        elif 'stock prices' in query:
            search_term = takeCommand().lower().split(" of ")[-1].strip() #strip removes whitespace after/before a term in string  
            stocks = {  
                "apple":"AAPL",  
                "microsoft":"MSFT",  
                "facebook":"FB",  
                "tesla":"TSLA",  
                "bitcoin":"BTC",  
                "amazon":"AMZN"
            }  
            try:  
                stock = stocks[search_term]  
                stock = yf.Ticker(stock)  
                price = stock.info["regularMarketPrice"]  
    
                speak(f'the stock price of {search_term} is {price} {stock.info["currency"]}')  
            except:  
                speak('oops, something went wrong')
