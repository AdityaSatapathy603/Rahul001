import speech_recognition as sr
import pyttsx3
import random
import time

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voices',voices[1].id)
rate = engine.getProperty('rate')
engine.setProperty('rate',185)
#print(rate)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#def take_command():
#    try:
#        with sr.Microphone() as source:
#            print('listening...')
#            voice = listener.listen(source)
#            command = listener.recognize_google(voice)
#            command = command.lower()
#            if 'mark' in command:
#                command = command.replace('mark', '')
#                print(command)
#    except:
#        pass
#    return command

if __name__ == "__main__":
    speak("Just say roll the dice or flip the dice...")
    print("Just say roll the dice or flip the dice...")
    random_number_index = 0
    while True:
        query = input(">>> ")

        if 'roll count' in query or 'number of roll' in query:
            print(random_number_index)
            
        elif 'roll' in query:
            query = query.replace('roll', '')
            alpha = str(random.randint(1,6))
            print(alpha)
            speak(alpha)
            random_number_index = (random_number_index + 1)
            time.sleep(1)

        elif 'roll again' in query:
            query = query.replace('roll again','')
            dice_num = str(random.randint(1,6))
            print(dice_num)
            speak(dice_num+'this time')
            random_number_index = (random_number_index + 1)
            time.sleep(1)
 
        elif 'flip' in query:
            query = query.replace('flip','')
            dice_num = str(random.randint(1,6))
            print(dice_num)
            speak(dice_num+' ,this time')
            time.sleep(1)