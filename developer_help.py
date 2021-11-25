import os
import jarvis

############################## PYTHON PROGRAMMING SUPPORT ##################################
def pipInstall():
    message = jarvis.query
    stopwords = ['install']
    querywords = message.split()
    resultwords  = [word for word in querywords if word.lower() not in stopwords]
    result = ' '.join(resultwords)
    rand = [('installing '+result)]
    jarvis.speak(rand)
    os.system('python -m pip install ' + result)
############################## PYTHON PROGRAMMING SUPPORT ##################################

############################## JAVASCRIPT PROGRAMMING SUPPORT ##################################
def npmInstall():
    message = jarvis.query
    stopwords = ['install']
    querywords = message.split()
    resultwords  = [word for word in querywords if word.lower() not in stopwords]
    result = ' '.join(resultwords)
    rand = [('installing '+result)]
    jarvis.speak(rand)
    os.system('npm install ' + result)
############################## JAVASCRIPT PROGRAMMING SUPPORT ##################################
