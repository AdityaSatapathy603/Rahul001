
import hashlib

import pyttsx3
import speech_recognition as sr


engine = pyttsx3.init()
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voices',voices[1].id)

rate = engine.getProperty('rate')
engine.setProperty('rate',180)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def take_command():
    r = sr.Recognizer() 
      
    with sr.Microphone() as source: 
        print('Listening...') 
          
        r.pause_threshold = 1.5 
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source) 
    try: 
        print("Recognizing...") 
              
        query = r.recognize_google(audio, language='en-us') 
              
        print(f"User said: {query}\n") 
    except Exception as e: 
            
        return "None"
    return query

#print(encrypt)
while True:
    query = take_command().lower()
    #cmd = input("Enter your command: ")
    if 'code zero' in query: # Master Control Command
        query = query.replace("code zero","")
        #speak('Master Control Request detected...')
        speak('ovreride accepted, voice command deactivated')
            #mark self destruct in t-30s command code 000destruct0
        MARK = input("Enter Your Command Key: ")
        if 'command code 000destruct0' in MARK:
            speak('Command code Zero confirmed...destruct sequence completed and engaged')
            speak('MARK program function will self-destruct in t minus 30 seconds')
                #os.system("shutdown /s /t 30")
        else:
            speak('Aborting Master Control...')
            speak('Program require manual restart')
            exit()

    elif 'code 10' in query or "code ten" in query:
        query = query.replace("code 10","")
        query = query.replace("code ten","")
        speak('over-ride accepted, voice command activated')
        query1 = take_command().lower()
        print(query1)
        if 'mark self destruct in t minus thirty seconds command code zero zero zero destruct zero' in query:
            speak('Command code Zero confirmed...,destruct sequence completed and engaged')
            speak('MARK program function will self-destruct in t minus 30 seconds')
            exit()
        else:
            speak('ERROR...')
            speak('Self-destruct activation not matched')
            exit()