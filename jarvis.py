import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import requests
import pyjokes
import pyautogui
import wolframalpha
import psutil
import time

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

if __name__ == "__main__":
    NOTE = '''
    ________|JARVIS VIRTUAL ASSISTANT|_________
    |CREATED BY: Akul Goel                    |
    |________________COMMANDS_________________|
    |#open youtube|#open google|#open github  |
    |#check battery|#search wikipedia|#ask me |
    |#put computer on sleep mode|#log off     |
    |_________________________________________|
    '''
    print(NOTE)
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

        elif 'open blooket' in query:
            webbrowser.open("blooket.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'pip install' in query:
            message = query
            stopwords = ['install']
            querywords = message.split()
            resultwords  = [word for word in querywords if word.lower() not in stopwords]
            result = ' '.join(resultwords)
            rand = [('installing '+result)]
            speak(rand)
            os.system('python -m pip install ' + result)

        elif 'battery' in query:
            battery()

        elif 'cpu' in query:
            cpu()

        elif 'memory' in query:
            memory()

        elif 'npm install' in query:
            message = query
            stopwords = ['install']
            querywords = message.split()
            resultwords  = [word for word in querywords if word.lower() not in stopwords]
            result = ' '.join(resultwords)
            rand = [('installing '+result)]
            speak(rand)
            os.system('npm install ' + result)

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
            time.sleep(5)

        elif 'open github' in query:
            webbrowser.open("github.com")   
            time.sleep(5)

        elif "camera" in query or "take a photo" in query:
            ec.capture(0,"robo camera","img.jpg")

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
            api_key="Paste your own id here"
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
            app_id="paste your own id here"
            client = wolframalpha.Client('paste in your own id here too')
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)

        elif 'open w3school' in query:
            webbrowser.open("w3schools.com")

        elif 'who made you' in query:
            speak('Akul Goel made me.')

        elif 'thank you' in query:
            speak('Of course, sir. No need to thank me')

        elif 'what can you do' in query:
            speak('I can click screenshots of your current screen, click a photo using your camera, and much more!')
