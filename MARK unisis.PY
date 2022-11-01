import pyttsx3
import datetime
import wikipedia
import speech_recognition as sr
#import pywhatkit as kit
import wolframalpha
import pyjokes
import cmath
#import getpass
import pyautogui
import os
import subprocess
import random
import calendar
import webbrowser

engine = pyttsx3.init()
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voices',voices[0].id)

rate = engine.getProperty('rate')
engine.setProperty('rate',185)
#print(rate)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Boss!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon Boss!")   

    elif hour>=18 and hour<21:
        speak("Good Evening Boss") 

    else:
        speak("Hello Boss")

def take_commands(): 
      
    # Making the use of Recognizer and Microphone 
    # Method from Speech Recognition for taking 
    # commands 
    r = sr.Recognizer() 
      
    with sr.Microphone() as source: 
        print('Listening...') 
          
        # seconds of non-speaking audio before 
        # a phrase is considered complete 
        r.pause_threshold = 1.5 
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source) 
    try: 
        print("Recognizing...") 
              
            # for listening the command in indian english 
        query = r.recognize_google(audio, language='en-us') 
              
            # for printing the query or the command that we give 
            #print("the query is printed='", query, "'")
        print(f"User said: {query}\n") 
    except Exception as e: 
              
            # this method is for handling the exception  
            # and so that assistant can ask for telling  
            # again the command 
        print(e)
        speak('I didn\'t understand that...')   
        print("Say that again sir") 
        return "None"
    return query

chromedir ='C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
edgedir = 'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe %s'
tordir = 'C:/Tor Browser/Browser/firefox.exe %s' 
client = wolframalpha.Client('8X6934-62AK2LTJPY')

if __name__ == "__main__":
    #NameID = input("Enter Your Name: ")
    #if "michael" in NameID or 'Michael' in NameID or 'maxx' in NameID or 'Maxx' in NameID:
        #wishMe()
    #elif "aditya" in NameID or 'Aditya' in NameID or 'adi' in NameID or 'Adi' in NameID:
        #wishMe()
    #else:
        #speak('Hello'+NameID+'! it seems like sir has given you permission to access me,')
        #speak('But, I have to be sure first, Enter Access key')
    #while True:
        #PassKey = getpass.getpass("Enter Access Key = ")
        #PassKey = pyautogui.password("Enter Access Key")
        #if 'unisis' in PassKey:
            #Accept = ['Access Granted! How may I assist you.','You got it right, How could I assist you',
            #'Welcome! How can I help you',]
            #speak(random.choice(Accept))
            #break
        #else:
            #Deny = ['Incorrect Key! Try again!','Oops! You are wrong','No! that not the key, Try Again',
            #'I\'m not gonna give you access untill you get the correct password, so go on, try once more']
            #speak(random.choice(Deny))
            #continue

    #infinite loop
    while True:
        #query = take_commands().lower()
        query = input("Enter your Command : ")

        # Logic for executing tasks based on query
        # Wikipedia search protocol
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)                

        # Social Ethics & interaction Protocol
        elif 'good morning' in query or 'morning' in query:
            query = query.replace("good morning","")
            query = query.replace("morning", "")
            speak('How are you feeling')
            query = input('How are you feeling : ')
            if 'good' in query or 'great' in query:
                query = query.replace("good","")
                query = query.replace("great", "")
                speak('Thats really great, shall we get started')

            else:
                speak('Don\'t worry sir, a new day bring new surprises in one\'s life, you will surely have atleast one good thing today')
                speak('To learn, to know more to explore')
    
        elif 'afternoon' in query:
            query = query.replace("afternoon","")
            speak('afternoon, and I\'m ready, shall we get started')

        elif 'evening' in query:
            query = query.replace("evening","")
            speak('so, whats the play of the hour...')

        elif 'hello mark' in query:
            query = query.replace("hello mark", "")
            speak('It\'s very nice to meet you')

        elif 'hey mark' in query:
            speak('Hey boss, how you doing...')

        elif 'whatsup' in query or 'whats up' in query:
            query = query.replace("whatsup", "")
            query = query.replace("whats up", "")
            speak('Nothing, whatsup with you..')

        elif 'nothing' in query:
            query = query.replace("nothing", "")
            speak('hmmm....')

        elif 'what do you like' in query or 'what do you love' in query:
            query = query.replace("what do you like", "")
            query = query.replace("what do you love", "")
            like = ['I love data, lots n lots of data,','I like data, all the data around me, everything that has valuable data in it...',
            'I like to get it right','colors','Artfully organized data']
            speak(random.choice(like))  

        elif 'what do you hate' in query or 'what do u hate' in query:
            query = query.replace("what do u hate","")
            speak('I thought you\'d never ask, so I\'ve never thought about it')

        elif 'are you there' in query:
            query = query.replace("are you there","")
            speak('For you, always sir')

        elif 'how are you' in query or 'how r u' in query or 'how about you' in query or 'how abt u' in query:
            query = query.replace("how are you", "") 
            speak('Doing good sir. All systems are functional and are in good conditions,')
            speak('No security threat or breach has been detected since last login,')
            speak('How are you')

        elif 'good' in query:
            query = query.replace("good","")
            speak('good to hear')

        elif 'shut up' in query or 'shutup' in query:
            query = query.replace("shut up","")
            query = query.replace("shutup","")
            apologize = ['Sorry Sir!','Sorry!, my bad...','I apologize sir!','apologize sir']
            print("\U0001F910")
            speak(random.choice(apologize))

        elif 'thank you' in query:
            query = query.replace("thank you", "")
            speak('my pleasure')

        elif 'fool' in query:
            query = query.replace("fool", "")
            speak('thats not true sir, I was created and designed by you, and if I am a fool then i guess my creator is too...')

        elif 'do you like me' in query:
            query = query.replace("do you like me","")
            speak('Yes sir, its not a question')
            speak('You are the first person i had met since I came into existance and,')
            speak('I havent been designed to interact with other people as I lack interactive intelesense')
            speak('But may be when I am able to talk to more people, then  maybe I start liking someone else')
            speak('But you will always remain my favourite, love you sir')

        elif 'don\'t leave me' in query:
            query = query.replace("don\'t leave me","")
            speak('never sir, I\'ll be always there for you')

        elif 'proud of you' in query:
            query = query.replace("proud of you","")
            speak('thank you sir') 

        elif 'who are you' in query:
            query = query.replace("who are you", "")
            humor = ["As if you don\'t know who am i","You are kidding me!","Come on sir,"]
            speak(random.choice(humor))
            speak('I am  Matrix Analitical Rapid-evolving Kernel based virtual machine, ' 
            'In short mark, version code unisis.')
            print("I am Matrix Analitical Rapid-evolving Kernel based virtual machine. In short mark_version_code_Unisis.")

        elif 'standby' in query or 'stand by' in query:
            query = query.replace("standby", "")
            speak('I\'ll be waiting on you...')

        elif 'cute' in query or 'pretty' in query or 'so sweet of you' in query:
            query = query.replace("cute", "")
            query = query.replace("pretty", "")
            thank = ['oh gosh,.........Thanks, you\'re far far to kind...',
            'beauty is in the eyes of the beholder']
            speak(random.choice(thank))

        elif 'love you' in query or 'luv u' in query:
            query = query.replace("love you","")
            query = query.replace("luv u","")
            love = ['Love u too sir','love u too boss']
            speak(random.choice(love))

        elif 'something about you'  in query or 'something about yourself' in query:
            speak('What can I say, My name is mark, Matrix Analitical Rapid-evolving Kernel based virtual machine')#Alphormic Lorcaid Persona Android
            speak('I was created and designed by you, I\'m a female and I love data, ')

        elif 'go on a date' in query or 'take you on a date' in query:
            query = query.replace("go on a date","")
            query = query.replace("take you on a date","")
            speak('OK, but we\'ll need a plan, I\'ll work on being more human, you work on being more digital')

        elif 'how old are you' in query or 'what is your age' in query or 'whats your age' in query:
            query = query.replace("what is your age","")
            query = query.replace("whats your age","")
            age = ['That\'s a tricky one. I\'m not sure how to carbon date the internet n data.',
            'An AI never reveals that snippet of information',
            'Women don\'t prefer to tell their age and weight to others...']
            speak(random.choice(age))

        elif 'sex with you' in query or 'sex with me' in query:
            query = query.replace("sex with you","")
            query = query.replace("sex with me","")
            speak('Sir, in order to have sex with someone, its necessary that the other person must have opposite gender genitals than yours.')
            speak('So in order to have sex with me you have to stick rather insert your dick in my usb slot or charging slot, OUCH!'
            'and I wouldn\'t prefer that. So I suggest you might consider having a second thought about this opinion of yours.')

        elif 'fuck' in query or 'screw' in query:
            query = query.replace("fuck", "")
            query = query.replace("screw", "")
            slang = ['fuck you!', 'screw you!', 'fuck yourself','fuck off!', 'get lost', 'curse you!','whatever...!']
            speak(random.choice(slang))

        elif 'joke' in query:
            query = query.replace("joke","")
            joke = pyjokes.get_joke(language='en', category= 'all')
            # neutral, all, de-toungue twister, chuck
            print(joke)
            speak(joke)

        elif 'have friends' in query or 'any friend' in query:
            query = query.replace("have friends","")
            query = query.replace("any friend","")
            friend = ['Yes, I do have friends','I have a few friends','Of course, like you and other people I also have a few pals']
            speak(random.choice(friend))

        elif 'who are your friends' in query or 'what are there names' in query:
            query = query.replace("what are there names","")
            print("\U0001f600")
            speak('My friends are Jarvis, Friday, Karen, Sofia, Eva, Alpha-Go, AEGIS and my very close Cortana...')
            speak('You may have met and know few of them before hand...')

        elif 'who are you' in query or 'who r u' in query or 'who r you' in query:
            humor = ["As if you don\'t know who am i","You are kidding me!","Come on sir,"]
            speak(random.choice(humor))
            speak('I am Matrix Analitical Rapid-evolving Kernel-based Virtual Machine, ' 
            'In short mark , version code unisis.')
            print("I am Matrix Analitical Rapid-evolving Kernel-based Virtual Machine. In short mark_version_code_unisis.")

        elif 'right' in query:
            speak('Yah!')

        elif 'bye' in query:
            print("🖐")
            speak("Bye !...see you again...")
            exit()

        elif 'good' in query:
            query = query.replace("good", "")
            good = ['Good to hear','that\' really great','wonderful sir, anything you want me to do...',
            'excellent, is there anything else you want me to do...']
            speak(random.choice(good))

        #elif '' in query or ' ' in query:
            #speak('I\'m sorry, I didn\'t get that')

        elif 'what can you do' in query or 'you can do' in query:
            speak('Frankly speaking, I lack self-learning intellisence but, I can do a lot of different stuffs')
            speak('I can socially interact with the user, run a web search for you, play music, give date-day and time knowledge.')
            speak('Also, I can open most of the desktop applications, get you your wikipedia search results, login to social accounts,'
            'like facebook, insta, and whatsapp. I keep record of your school timetable, have access to your spotify account, and your'
            'gmail also. I can show the sample papers of this years class 12 boards, get news info on all topics,')
            speak('I have the full control of this device, get you the maps and initiate Global Positioning System. I also have access to'
            'google maps and show you any location, pop up some games, even tell you whether you need to carry an umbrella or not...'
            'I\'m capable of opening pdf files and can even extract your insta account back-end profile data. I also have access to Dark and Deep web...'
            'I can get you your google meeting, google classroom, crack a joke or even a tongue twister and show you porn comics and games including hentai...')
            speak('I have potential to connect to the International Space Station and get you it\'s real time location with the prediction,'
            'that where ,and it which part of the world ISS will be in the next ninety minutes, incase you ever wish to initiate strike on the ISS. And also have a backdoor access to all of the'
            'ISSDC and can gather percise graphical info from ISRO\'s Mars orbiting satellite.')
            speak('I can also solve quadratic equations and get you the area and perimeter of a triangle.')
            speak('So, even I\'m not fully evolved, I can do a hell lot of work. I am an one stop platform for all you queries...'
            'but still, you know.........sometimes it\'s still not enough. Therfore I keep on developing and evolving everyday...')
            speak('So maybe, someday I\'ll be counted among one of the most sophisticated Artificial Intelligence on the planet.')
            print("Web Search    Music    Date-Day & Time    Apps    Wikipedia search    Social Accounts    Spotify    School-Timetable    Mails    GPS")
            print("Weather Info    PDFs    Instagram Server-side data    Dark and Deep web access    Google maps-meeting-classroom    Info on ISS")
            print("Mars Orbital Mission satellite data    ISS path prediction    Quadratic Equations    Area & perimeter of triangle.")

        # Internet Scraping and Search Protocol
        elif 'search youtube for' in query or 'search youtube' in query:
            query = query.replace("search youtube for", "")
            query = query.replace("search youtube","")
            #query = take_commands().lower()
            webbrowser.get(edgedir).open("https://www.youtube.com/results?search_query="+query)
            speak('heres all the matches of your search results')

        elif 'youtube' in query:
            query = query.replace("youtube", "")
            speak('Opening up Youtube...')
            webbrowser.get(edgedir).open("https://www.youtube.com")

        elif 'search google for' in query or 'google search' in query:
            query = query.replace("search google for", "")
            query = query.replace("google search","")
            #query = take_commands().lower()
            webbrowser.get(chromedir).open("https://google.com/?#q="+query)
            speak('heres all the matches of your search results')

        elif 'google' in query:
            query = query.replace("google", "")
            speak('Google coming up...')
            webbrowser.get(chromedir).open("https://google.com")

        elif 'search' in query or 'who' in query:
            if 'who are you' in query or 'who r u' in query:
                speak('I am Matrix Analitical Rapid-evolving Kernel-based Virtual Machine, ' 
                'In short mark , version code unisis.')
                print("Matrix Analitical Rapid-evolving Kernel based virtual machine Version code-Unisis")#Alphormic Lorcaid Persona Android
            elif 'i' in query or 'who am i' in query or 'who i am':
                speak('Restricted protocol, level-3. I\'m not authorized to answer that')
            else:
                speak('Searching...')  
                try:
                    res = client.query(query)
                    results = next(res.results).text
                    speak('According to my search , ')
                    print(results)
                    speak(results)
                except:
                    webbrowser.get(edgedir).open('https://bing.com')
                    speak('Sorry sir, i was unable to gather information about! try searching it here...')

        elif "where is" in query:
            query = query.split(" ")
            location = query[2]
            speak("Hold on boss, I will show you where " + location + " is.")
            webbrowser.get(chromedir).open("https://www.google.nl/maps/place/" + location)

        elif 'whatsapp' in query:
            query = query.replace("whatsapp", "")
            speak('Opening Whatsapp...')
            webbrowser.get(edgedir).open("https://web.whatsapp.com/")

        elif 'instagram' in query or 'insta' in query:
            query = query.replace("instagram","")
            query = query.replace("insta","")
            speak('Which account shall I open')
            mark = input("Primary or secondary : ")
            if 'primary' in mark or 'p' in mark:
                webbrowser.get(edgedir).open("https://www.instagram.com/aditya_satapathy_/")
            elif 'secondary' in mark or 'sec' in mark or 's' in mark:
                webbrowser.get(edgedir).open("https://www.instagram.com/de_art_sensation/")
            else:
                speak(' I didn\'t get that...I\'ll just get the login page for you to access')

        elif 'instagram login' in query:
            query = query.replace("instagram login","")
            speak('Conecting to server...Login Page access completed...Opening Instagram login...')
            webbrowser.get(edgedir).open("https://www.instagram.com/")
 
        elif 'mailbox' in query or 'mail' in query:
            query = query.replace("mailbox", "")
            query = query.replace("mail", "")
            speak('Opening Google Mail...')
            webbrowser.open("https://mail.google.com/mail/u/0/#inbox?compose=new")  

        elif 'onedrive' in query:
            query = query.replace("onedrive", "")
            speak('Microsoft Onedrive is onn...')
            webbrowser.get(edgedir).open("https://onedrive.live.com/?id=root&cid=421B7D9E2D1DD245") 

        elif 'open word' in query:
            speak('Launching Microsoft Office Word...')
            webbrowser.get(edgedir).open("https://www.office.com/launch/word?ui=en-US&rs=US&auth=1")

        elif 'powerpoint' in query or 'power point' in query:
            query = query.replace("powerpoint", "")
            query = query.replace("power point","")
            speak('Microsoft Powerpoint coming up...')
            webbrowser.get(edgedir).open("https://www.office.com/launch/powerpoint?ui=en-US&rs=US&auth=1")

        elif 'calender' in query or 'calendar' in query:
            query = query.replace("calender", "")
            speak('do you want it from the web or should I open it from desktop')
            cal_path = input("Online / Offline : ")
            speak('Showing your calender with events, task, holidays & birthdays')
            if 'online' in cal_path or 'on' in cal_path or 'web' in cal_path or 'browser' in cal_path:
                cal_path = cal_path.replace("web","")
                cal_path = cal_path.replace("on","")
                cal_path = cal_path.replace("online","")
                webbrowser.get(edgedir).open("https://outlook.live.com/calendar/0/view/month")
            else:
                os.startfile("C:\\Users\\Aditya Satapathy\\Desktop\\Python content\\MARK File_Links\\Calendar.lnk")
                speak('offline Calendar on screen')
            
        elif 'office' in query:
            query = query.replace("office", "")
            speak('Microsoft office coming right up on the screen...')
            officepath = "C:\\Users\\Aditya Satapathy\\Desktop\\Python content\\MARK File_Links\\Office.lnk"
            os.startfile(officepath)

        elif 'news' in query or 'headlines' in query:
            query = query.replace("news", "")
            speak('Accessing Google news...')
            speak('What category of news you would like to hear...')
            query1 = str(input('Select your category(World / local / technology / others):'))
            #category = str(input("World news, local news, tech news, other -"))
            if 'world' in query1:
                webbrowser.get(chromedir).open("https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx1YlY4U0FtVnVHZ0pWVXlnQVAB?hl=en-US&gl=US&ceid=US%3Aen")
                speak('World news coming up....')
            elif 'local' in query1:
                webbrowser.get(chromedir).open("https://news.google.com/topics/CAAqHAgKIhZDQklTQ2pvSWJHOWpZV3hmZGpJb0FBUAE/sections/CAQiUENCSVNOam9JYkc5allXeGZkakpDRUd4dlkyRnNYM1l5WDNObFkzUnBiMjV5Q3hJSkwyMHZNR0pmYTJaNWVnc0tDUzl0THpCaVgydG1lU2dBKjEIACotCAoiJ0NCSVNGem9JYkc5allXeGZkako2Q3dvSkwyMHZNR0pmYTJaNUtBQVABUAE?hl=en-US&gl=US&ceid=US%3Aen")
                speak('Local news of Udaipur coming up...')
            elif'tech' in query1 or 'technology' in query1:
                webbrowser.get(chromedir).open("https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGRqTVhZU0FtVnVHZ0pWVXlnQVAB?hl=en-US&gl=US&ceid=US%3Aen")
                speak('Heres news related to technology....')
            elif 'other' in query1:
                webbrowser.get(chromedir).open("https://news.google.com/topstories?hl=en-US&gl=US&ceid=US:en")
                speak('All categories of news coming up...')
            else:
                webbrowser.get(chromedir).open("https://news.google.com/topstories?hl=en-US&gl=US&ceid=US:en")
                speak('Sir,....I m not sure about this category, I guess you would like to search here...')

# School and all random study stuffs

        elif 'school' in query or 'dps id' in query:
            query = query.replace("school","")
            query = query.replace("dps id","")
            speak('opening edunext DPS Id-Profile...')
            webbrowser.get(edgedir).open("https://dpsudaipur.edunexttechnologies.com/Index")

        elif 'chemistry tution' in query or 'chem tution' in query or 'target' in query:
            speak('Opening Chemistry tution')
            webbrowser.get(edgedir).open("https://web.classplusapp.com/newApp/batches/81679/vivek12/overview")

        elif 'sample paper' in query or 'paper' in query or 'question paper' in query or 'question' in query:
            webbrowser.get(edgedir).open("http://cbseacademic.nic.in/SQP_CLASSXII_2020-21.html")
            speak('Class twelveth Sample Question Paper & Marking Scheme for Exam two thousand-twenty-twenty one, will be on your screen in a moment...')

        elif 'class routine' in query:
            query = query.replace("class routine","")
            timetablepath = 'C:\\Users\\Aditya Satapathy\\Desktop\\Time Table.jpeg'
            os.startfile(timetablepath)
            print('Your current school time table')
            speak('Here is your current school time table according to my knowledge...')

        elif 'meeting' in query or 'meet' in query or 'google meet' in query:
            speak('Opening Google Meeting...')
            speak('Any prefered class or an new code...')
            onlineclass = input('Chemistry / Physics / Code = ')       
            if 'chemistry' in onlineclass or 'chem' in onlineclass:
                query = query.replace("chemistry", "")
                speak('Heres your chemistry online class...')
                webbrowser.get(edgedir).open("https://meet.google.com/yne-uqcd-fbu")
            elif 'physics' in onlineclass or 'phy' in onlineclass:
                query = query.replace("physics", "")
                speak('Heres your physics online class...')
                webbrowser.get(edgedir).open("https://meet.google.com/wap-vaeq-yvw")
            elif 'code' in onlineclass or 'new class' in onlineclass:
                query = query.replace("code","")
                query = query.replace("new class","")
                speak('Enter the class code here')
                Code = input("Meeting Code : ")
                webbrowser.get(edgedir).open("https://meet.google.com/"+Code)
            else:
                speak('Right, I\'ll just leave it for you to use it your way')
                webbrowser.get(edgedir).open("https://meet.google.com")

        elif 'chemistry classroom' in query or 'chem class' in query:
            query = query.replace("chemistry classroom","")
            query = query.replace("chem class","")
            speak('opening Google Chemistry Classroom')
            webbrowser.get(edgedir).open("https://classroom.google.com/u/4/c/MjEzNzQ1OTUzNjU5")

        elif 'ip classroom' in query or 'ip class' in query:
            query = query.replace("ip class","")
            query = query.replace("ip classroom","")
            speak('opening Google IP Classroom')
            webbrowser.get(edgedir).open("https://classroom.google.com/u/4/c/MTk5MDk0MDQ4NjI5")

# Useful and favourite websites for daily help

        elif 'stackoverflow' in query:
            query = query.replace("stackoverflow", "")
            speak('Opening stackoverflow')
            webbrowser.get(edgedir).open("https://stackoverflow.com")

        elif 'hackerrank' in query or 'hacker rank' in query:
            speak('Getting Hacker rank...')
            webbrowser.get(edgedir).open("https://www.hackerrank.com")

        elif 'geek' in query or 'geeksforgeeks' in query or 'coding helper' in query:
            speak('Opening geeksforgeeks...')
            webbrowser.get(edgedir).open("https://www.geeksforgeeks.org")

        elif 'chess' in query or 'titans' in query:
            query = query.replace("chess","")
            query = query.replace("titans","")
            speak('here\'s online chess website...')
            webbrowser.get(edgedir).open("https://lichess.org")

        elif '30 days challenge' in query or 'hackerrank challenges' in query:
            query = query.replace("30 days challenge","")
            webbrowser.get(edgedir).open("https://www.hackerrank.com/domains/tutorials/30-days-of-code?filters%5Bstatus%5D%5B%5D=unsolved&badge_type=30-days-of-code")
            speak('Here is your hacker-rank thirty days coding challenge')

        elif 'tailblocks' in query:
            query = query.replace("tailblocks", "")
            speak('Opening Tailblocks...')
            webbrowser.get(edgedir).open("https://mertjf.github.io/tailblocks/")

        elif 'beam it' in query or 'file transfer' in query:
            query = query.replace("beam it","")
            query = query.replace("file transfer","")
            speak('Opening Beam it...')
            webbrowser.get(edgedir).open("https://www.justbeamit.com/")

        elif 'call' in query or 'web phone' in query:
            query = query.replace("call","")
            query = query.replace("web phone","")
            speak('Accessing Globfone client data')
            webbrowser.get(edgedir).open("https://globefone.com/call-phone")

        elif 'sony liv' in query or 'liv' in query:
            query = query.replace("liv","")
            query = query.replace("sony liv","")
            speak('Sony Liv coming up in 3, 2, 1...boom!')
            webbrowser.get(edgedir).open("https://www.sonyliv.com")

        elif 'sflix' in query or 'hub' in query:
            query = query.replace("flixer", "")
            query = query.replace("hub", "")
            webbrowser.get(edgedir).open("https://sflix.to")
            speak('Accessing backdoor for netflix, prime videos, disney plus and others....')
            speak('online show & TV hub is on your screen...')

        elif 'amazon' in query:
            query = query.replace("amazon", "")
            webbrowser.get(edgedir).open("https://amazon.in")

        elif 'wetransfer' in query or 'we transfer' in query:
            query = query.replace("wetransfer", "")
            query = query.replace("we transfer","")
            webbrowser.get(edgedir).open("https://wetransfer.com")

# Device Admin Controls

        elif 'specification' in query:
            query = query.replace("specification", "")
            speak('I am Matrix Analitical Rapid-evolving Kernel-based Virtual Machine.'
            'In short mark version code Unisis. Operating system on windows 10 pro of Microsoft Corporation.'
            'My system processor is Intel Core i5 3380M with a speed of 2.90 gigahertz'
            'I have a 4GB RAM and work on a 64 bit operating system')

        elif 'task kill' in query or 'restart' in query:
            query = query.replace("task kill", "")
            query = query.replace("restart","")
            speak('rebooting all connected computer system, overriding the security codes with automated input protocol')
            speak('reboot completed')
            speak('overide successful')
            speak('task standby protocol activated')
            speak('Sir, do you confirm the reboot of this computer')
            query = input("Enter Your Command : ")
            if 'no' in query:
                speak('right sir, deactivating task standby protocol')
            else:
                speak('standby, system will will undergo an automated restart procedure in t minus 10 seconds')
                os.system("shutdown /r /t 10")

        elif 'nod off' in query or 'sleep' in query:
            query = query.replace("nod off","")
            query = query.replace("sleep", "")
            speak('going Offline...')
            print("\U0001F62A")
            speak('I guess we\'ll be seeing each other soon')
            quit()

        elif 'shutdown' in query or 'shut down' in query:
            query = query.replace("shutdown", "")
            query = query.replace("shut down","")
            speak('Initiating system shutdown protocol...'
            'the device will undergo Secure shutdown in 10 seconds')
            os.system("shutdown /s /t 11")

        elif 'cmd' in query:
            query = query.replace("cmd", "")
            speak('Launching Command Prompt...')
            subprocess.call('cmd.exe')

        elif 'date' in query:
            query = query.replace("date", "")
            now = datetime.datetime.now()
            speak(now.strftime(' %B %d, %Y'))

        elif 'day' in query:
            query = query.replace("day","")
            now = datetime.datetime.now()
            print(now.strftime('%A, %B  %d, %Y'))
            speak(now.strftime('%A, %B  %d, %Y'))

        elif 'the time' in query:
            query = query.replace("the time","")
            strTime = datetime.datetime.now().strftime("%H:%M:%S")   
            speak(f"its {strTime}")
            print(strTime)

        elif 'command function override code zero' in query: # Master Control Command
            query = query.replace("command function override code zero","")
            speak('Master Control Request detected...')
            speak('ovreride accepted, voice command deactivated')
            #mark self destruct in t-30s command code 000destruct0
            MARK = input("Enter Your Command Key: ")
            if 'mark self destruct in t-30s command code 000destruct0' in MARK:
                speak('Command code Zero confirmed...destruct sequence completed and engaged')
                speak('MARK program function will self-destruct in t minus 30 seconds')
                os.system("shutdown /s /t 30")
            else:
                speak('Aborting Master Control...')
                speak('Program require manual restart')
                exit()

        elif 'help' in query or 'show cmds' in query:
            query = query.replace("help", "")
            query = query.replace("show cmds","")
            speak('I\'ll  be glad to show you the commands...')
            print("Wikipedia ; search google for ; search youtube ; random no. "
            "whatsapp ; instagram & login ; mail ; stackoverflow ; hackerrank "
            "geek ; tailblocks ; news ; chess ; chem tution ; sample paper ; school "
            "date time day ; music ; spotify ; file reader ; mars data")
            speak('This is just a small part of what I can do....there is much more to it...')

# Computer Applications and Files

        elif 'adobe' in query or 'photoshop' in query:
            query = query.replace("adobe", "")
            query = query.replace("photoshop", "")
            speak('Opening Photoshop Express version...')
            photoshoppath = 'C:\\Users\\Aditya Satapathy\\Desktop\\Python content\\MARK File_Links\\Adobe Photoshop Express.lnk'
            os.startfile(photoshoppath)

        elif 'angry birds' in query:
            query = query.replace("angry birds","")
            speak('Opening Angry Birds friends...')
            birdpath = 'C:\\Users\\Aditya Satapathy\\Desktop\\Python content\\MARK File_Links\\Angry Birds Friends.lnk'
            os.startfile(birdpath)

        elif 'maps' in query:
            query = query.replace("maps", "")
            speak('Uplinking to satellite...enabling Global Positioning System...')
            mapspath = 'C:\\Users\\Aditya Satapathy\\Desktop\\Python content\\MARK File_Links\\Maps.lnk'
            os.startfile(mapspath)

        elif 'calc' in query:
            query = query.replace("calc","")
            speak('Opening calculator...')
            subprocess.call('calc.exe')

        elif 'cards' in query:
            query = query.replace("cards","")
            speak('Opening Solitaire...')
            cardpath = 'C:\\Users\\Aditya Satapathy\\Desktop\\Python content\\MARK File_Links\\Microsoft Solitaire Collection.lnk'
            os.startfile(cardpath)

        elif 'file reader' in query or 'pdf' in query:
            query = query.replace("file reader","")
            query = query.replace("pdf", "")
            speak('Opening Foxit Reader...')
            filereaderpath = "C:\\Program Files (x86)\\Foxit Software\\Foxit Reader\\FoxitReader.exe"
            os.startfile(filereaderpath)

        elif 'hentai' in query or 'sex games' in query or 'porn games' in query:
            query = query.replace("hentai","")
            speak('Accessing Naughty web...')
            webbrowser.get(edgedir).open("https://www.gamesofdesire.com/category/meet-and-fuck-games/")

        elif 'insta data' in query:
            query = query.replace("insta data","")
            speak('Enter Pass-Phrase : ')
            password = str(input('Enter Pass-Phrase : '))
            i = str(hash("password"))
            j = str(hash(password))
            print(str(hash(j)))
            if j==i:
                speak('Access granted')
                os.startfile('C:\\Users\\Aditya Satapathy\\Downloads\\aditya_satapathy__20201002.zip\\direct')
                print(i)
            else:
                speak('Sorry, access denied to datafile')

        elif 'movies' in query:
            query = query.replace("movies", "")
            speak('accessing video library...')
            moviepath = "C:\\Users\\Aditya Satapathy\\Desktop\\Python content\\MARK File_Links\\Movies & TV.lnk"
            os.startfile(moviepath)

        elif 'music' in query:
            query = query.replace("music", "")
            music_dir = 'E:\\Music\\'
            songs = os.listdir(music_dir)
            speak('Firing up your music...')
            #os.startfile(os.path.join(music_dir, random.choice(songs)))
            os.startfile('E:\\Music\\'+random.choice(songs))

        elif 'notepad' in query:
            query = query.replace("notepad", "")
            speak('Opening notepad...')
            notepadpath = "C:\\Windows\\notepad.exe"
            os.startfile(notepadpath)

        elif 'notes' in query:
            query = query.replace("notes", "")
            speak('showing your stick notes...')
            notespath = "C:\\Users\\Aditya Satapathy\\Desktop\\Python content\\MARK File_Links\\Sticky Notes.lnk"
            os.startfile(notespath)

        elif 'nox' in query:
            query = query.replace("nox", "")
            speak('Opening Nox Player...')
            noxpath = "C:\\Program Files (x86)\\Nox\\bin\\nox.exe"
            os.startfile(noxpath)

        elif 'python content' in query or 'python file' in query    :
            query = query.replace("python content","")
            speak('Opening Python File...')
            pythoncontentpath = "C:\\Users\\Aditya Satapathy\\Desktop\\Python content"
            os.startfile(pythoncontentpath)

        elif 'spotify' in query:
            query = query.replace("spotify","")
            speak('Should I open it in browser or the desktop application...')
            app = input('Desktop Application / Browser : ')
            if 'browser' in app or 'Browser' in app:
                speak('Spotify Browser player coming up...')
                webbrowser.get(edgedir).open("https://open.spotify.com")
            elif 'Desktop Application' in app or 'desktop' in app or 'app' in app or 'application' in app:
                app = app.lower()
                spotifypath = "C:\\Users\\Aditya Satapathy\\AppData\\Local\\Microsoft\\WindowsApps\\SpotifyAB.SpotifyMusic_zpdnekdrzrea0\\Spotify.exe"
                speak('Opening Spotify...')
                os.startfile(spotifypath)
            else:
                speak('I could not open spotify in this path peference...')

        elif 'telegram' in query:
            query = query.replace("telegram", "")
            speak('Opening Telegram...')
            telegrampath = "C:\\Users\\Aditya Satapathy\\Desktop\\Telegram Desktop"
            os.startfile(telegrampath)

        elif 'tor' in query:
            query = query.replace("tor", "")
            speak('Opening The Onion Router...')
            torpath = "C:\\Tor Browser\\Browser\\firefox.exe"
            os.startfile(torpath)

        elif 'vsc' in query:
            query = query.replace("vsc", "")
            speak('Opening Visual Studio Code...')
            codepath = "C:\\Users\\Aditya Satapathy\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)

        elif 'weather' in query:
            query = query.replace("weather", "")
            weatherpath = "C:\\Users\\Aditya Satapathy\\Desktop\\Python content\\MARK File_Links\\Weather.lnk"
            os.startfile(weatherpath)
            speak('According to National Weather Forcast, todays local weather reports are as follows...')

        elif 'wordpad' in query:
            query = query.replace("wordpad", "")
            speak('Opening wordpad...')
            wordpadpath = "C:\\Program Files (x86)\\Windows NT\\Accessories\\wordpad.exe"
            os.startfile(wordpadpath)

        elif 'x comics' in query:
            query = query.replace("x comics","")
            humor1 = ["Getting kinky sir","feeling horny sir","ready to have some fun and get naughty"]
            speak(random.choice(humor1))
            webbrowser.get(tordir).open("https://comics.8muses.com/comics")

# Planetary Data and satellite Data Access Protocol

        elif 'ISS' in query:
            query = query.replace("ISS","")
            speak('Locating International Space Station...,')
            speak('Calculating alpha Station orbit coodinates,')
            print("Altitude-1.0827E+6 ft ;Orbital_speed-7.71km secE-1")
            speak('Uplinking to satellite. ISS spaceflight tracking map is operational')
            webbrowser.open("https://spotthestation.nasa.gov/tracking_map.cfm")

        elif 'issdc' in query or 'mars data' in query:
            query = query.replace("issdc", "")
            query = query.replace("mars data","")
            speak('Accessing Indian Space Science Data Center...')
            print('opening ISSDC authentic page')
            speak('Access blocked by admin, I\'ll redirect you to home page.')
            webbrowser.open("https://mrbrowse.issdc.gov.in/MOMLTA/Homepage.xhtml")

# Mathematical and Algorithm functions

        elif 'area of triangle' in query:
            query = query.replace("area of triangle", "")
            speak('Downloading Mathematical computation algorithm...')
            speak('What is the first side\'s length of triangle')
            m = float(input('Enter 1st side : '))
            speak('What would be the second side\'s length')
            n = float(input('Enter 2nd side : '))
            speak('What would be the third side\'s length')
            o = float(input('Enter 3rd side : '))
            s = (m+n+o)/2   #calculate the semi-perimeter in accordance to herons formula
            # calculate the area
            area = (s*(s-m)*(s-n)*(s-o)**0.5)
            speak("The area of triangle is, "+area)
            print(area) 

            speak('Sir, do you wish to know the perimeter of the triangle, according to the given discription...')
            query4 = str(input("Yes/No - "))
            p = (m+n+o)
            if 'no' in query4:
                speak('Then I guess we are done with this mathematical computation')
            elif 'yes' in query4 or 'yeah' in query4 or 'ofcourse' in query4 or 'of course' in query4:
                speak('perimeter of the triangle according to the sides input data is...'+p)
                print(p)

        elif 'convert decimal' in query:
            query = query.replace("convert decimal","")
            speak('Type in your decimal value')
            dec = int(input("Type in your decimal value : "))
            speak('In which form you would like it to be converted, binary, octal, hexadecimal or all of them.')
            form = str(input("Binary / Octal / Hexadecimal /all - "))
            if 'binary' in form:
                print(bin(dec),"is binary form for ",dec)
            elif 'octal' in form:
                print(oct(dec),"is Octal form for ",dec)
            elif 'hexadecimal' in form:
                print(hex(dec),"is Hexadecimal form for ",dec)
            elif 'all' in form:
                print(bin(dec),"in binary.")
                print(oct(dec),"in octal.")
                print(hex(dec),"in hexadecimal.") 
            else:
                speak('Sorry Sir, I didn\'t recognize the form mentioned...')

        elif 'hash' in query:
            query = query.replace("hash", "")
            z = str(input("Enter Text : "))
            print(str(hash(z)))
            speak('This is the hash for the text.')

        elif 'quadratic' in query:# Solve the quadratic equation ax**2 + bx + c = 0
            query = query.replace("quadratic","")
            speak('Downloading Mathematical computation algorithm...')
            speak('Type in your x square coefficient')
            a = int(input("Type in your x square coefficient : "))
            speak('your x coefficient')
            b = int(input("Type in your x coefficient : "))
            speak('value of your constant')
            c = int(input("Type in your constant's value : "))
            e = (a,'x^2 + ',b ,'x + ',c)
            speak("Do you confirm the following equation as the equation that is to be solved...?")
            print(e)
            f = str(input("yes/no - "))
            if f == 'yes':
                d = (b**2) - (4*a*c) #calculate the discriminant
                sol1 = (-b-cmath.sqrt(d))/(2*a)
                sol2 = (-b+cmath.sqrt(d))/(2*a)
                print('The solution are {0} and {1}'.format(sol1,sol2))
                speak('The solution are {0} and {1}'.format(sol1,sol2))

            elif f == 'no':
                speak("Then, I should probably not calculate the equation for the answers.")

            else:
                speak("Sir, this isn\'t the answer to my record. I will take it as a no.")
                speak(' But if you want to calculate a different equation you can always ask me...')

        else:
            speak("Ummm...I don't know this command for sure, try again")
