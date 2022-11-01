import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voices',voices[1].id)

rate = engine.getProperty('rate')
engine.setProperty('rate',172)

def speak(audio):
    engine.say(audio)
    engine.runAndWait() 

def say():
    speech = input('Speech Drive Test : ')
    speak(speech)

if __name__ == "__main__":
    while True:
        say()