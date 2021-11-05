import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import requests
import subprocess
import pyjokes
import pyautogui
import wolframalpha
import smtplib
from ecapture import ecapture as ec

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

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
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

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'open github' in query:
            webbrowser.open("github.com")   

        elif "camera" in query or "take a photo" in query:
            ec.capture(0,"robo camera","img.jpg")

        elif "weather" in query:
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

        elif 'where am i' or 'where are we' in query:
            speak('Let me check, sir')
            try:
                ipAdd = requests.get('https://api.ipify.org').text
                print(ipAdd)
                url = 'https://get.geojs.io/v1/ip/geo'+ipAdd+'.json'
                geo_requests = requests.get(url)
                geo_data = geo_requests.json()
                city = geo_data['city']
                country = geo_data['country']
                speak(f'Sir, I might be wrong, but I believe we are in {city}, {country}')
            except Exception as e:
                speak('Sorry sir, I am not able to find our location')

        elif 'screenshot' in query:
            image = pyautogui.screenshot()
            image.save('screenshot.png')
            speak('Screenshot taken')

        elif 'open visual studio code' in query:
            vscodePath = 'C:\\Users\\materialsworld\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code'
            os.startfile(vscodePath)

        elif 'open android studio' in query:
            androidStudioPath = 'C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Android Studio'
            os.startfile(androidStudioPath)

        elif 'open google calendar' in query:
            webbrowser.open('calendar.google.com')

        elif 'change voice to female voice' in query:
            engine.setProperty('voice', voices[1].id)
            speak('Voice has been changed to female voice')

        elif 'change voice to male voice' in query:
            engine.setProperty('voice', voices[0].id)
            speak('Voice has been changed to male voice')

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
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            print('NOTE: The time is given in the ')
            speak(f"Sir, the time is {strTime}")

        elif 'open the folder Professional Apps' in query:
            folderPath = "C:\\Users\\materialsworld\\Desktop\\Akul Goel\\Professional Apps"
            os.startfile(folderPath)

        elif 'open the folder Akul Whitehat' in query:
            folder1Path = "C:\\Users\\materialsworld\\Desktop\\Akul Goel\\Akul Whitehat"
            os.startfile(folder1Path)

        elif 'news' in query:
            news = webbrowser.open('https://timesofindia.indiatimes.com/home/headlines')
            speak('Here are some headlines from the Times of India,Happy reading')

        elif 'ask' in query:
            speak('I can answer to computational and geographical questions. What question do you want to ask me')
            question = takeCommand()
            app_id="TTXXJU-JKXAR7LYX3"
            client = wolframalpha.Client('TTXXJU-JKXAR7LYX3')
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)

        elif 'email to me' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "akulgoel2010@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry sir, it seems there is a problem. I am not able to send this email")

        elif 'who made you' in query:
            speak('Akul Goel made me.')

        elif 'thank you' in query:
            speak('Of course, sir. No need to thank me')

        elif "log off" in query or "sign out" in query:
            speak("Ok , your pc will log off in 10 sec, make sure you exit from all applications")
            subprocess.call(["shutdown", "/l"])