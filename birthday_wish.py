import datetime
import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voices',voices[1].id)

rate = engine.getProperty('rate')
engine.setProperty('rate',180)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def birthday_remainder():
    birth_days = {"January 02" : "Bhavys\'s", "January 09" : "Divyansh\'s", "January 31" : 'Naisha\'s',
     "February 22" : 'Tani\'s', "February 03" : "Taha\'s", "February 17" : "Yashvi\'s",
     "March 07" : "Avisikta\'s", "April 01" : 'Munmun\'s' , "April 05" : 'Arko & your sister Swati\'s', 
     "April 28" : "Shailesh\'s", "April 09" : 'Kush\'s', "May 06" : "Kajal\'s", "May 30" : 'Subham\'s' , 
     "June 12" : 'Tik Tik\'s', "June 10" : 'Aditya Sharma\'s', "June 14" : 'your sister Sikha\'s', 
     "June 19" : 'Your' , 
     "June 25" : 'Ipshan\'s' , "June 30" : 'Rambo\'s' , 
     "July 01" : 'amrapali\'s' , "July 09" : 'Tim\'s' , "July 21" : 'Khushi Singh & Gyanish\'s',
     "August 29" : 'Titli, Vani & of course King of pop, Mivhael Jackson\'s',
     "September 02" : 'Nasreem ma\'am\'s', "September 03" : 'Arshi\'s',  "September 22" : 'Himanshi\'s', 
     "September 29" : 'Tanisha\'s',
     "October 02" : 'Devyani\'s', "November 17" : 'Batra\'s',}
    now = datetime.datetime.now()
    srurge = now.strftime('%B %d')
    #print(srurge)
    if srurge in birth_days:
        print(srurge,'Sir today is ',birth_days[srurge],' birthday.')
        #speak('By the way...')
        speak('Sir today is '+birth_days[srurge]+' birthday.')
        if 'June 19' in srurge:
            print("Happy Birthday Sir🎂🎉!")
            print("May you have a great year ahead, and enjoy the day.")
            speak("Happy Birthday Sir!,May you have a great year ahead, and enjoy the day")
    else:
        print("There ain\'t any birthdays today!")
        speak("There ain\'t any birthdays today!")