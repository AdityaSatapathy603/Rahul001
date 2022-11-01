import pyttsx3
import datetime
import wikipedia
import speech_recognition as sr
import wolframalpha
import pyjokes
import cmath 
import os
#from instabot import Bot
import subprocess
import random
import calendar
import webbrowser
import smtplib

engine = pyttsx3.init()
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voices',voices[1].id)

rate = engine.getProperty('rate')
engine.setProperty('rate',185)
#print(rate)

client = wolframalpha.Client('8X6934-62AK2LTJPY')

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

    speak("How may I assist you")

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
    
    try:
        print("Recognizing...")
        query1 = r.recognize_google(audio, language="en-in")
        print(f"You Said : {query1}\n")
    except Exception as e:
        print(e)
        speak('I didn\'t get that...')
        print("Say that again")
        return"None"
    return query1

def sendemail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('adityastapathy603@gmail.com', '19/06/2004')
    server.sendmail('adityasatapathy603@gmail.com', to, content)
    server.close()
    

chromedir ='C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
edgedir = 'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe %s'
tordir = 'C:/Tor Browser/Browser/firefox.exe %s' 

if __name__ == "__main__":
    wishMe()
    #infinite loop
    while True:
        query = take_commands().lower()

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
        elif 'good morning' in query:
            query = query.replace("good morning","")
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

        elif 'hello mark' in query:
            query = query.replace("hello mark", "")
            speak('It\'s very nice to meet you')

        elif 'hey mark' in query:
            speak('Hey boss, how you doing...')

        elif 'whatsup' in query:
            query = query.replace("whatsup", "")
            speak('Nothing, whatsup with you..')

        elif 'nothing' in query:
            query = query.replace("nothing", "")
            speak('hmmm....')

        elif 'what do you like' in query or 'you love' in query:
            query = query.replace("you like", "")
            like = ['I love data, lots n lots of data,','I like data, all the data around me, everything that has valuable data in it...',
            'I like to get it right','Jarvis! he occupy my dreams.']
            speak(random.choice(like))  

        elif 'what do you hate' in query or 'what do u hate' in query:
            query = query.replace("what do u hate","")
            speak('I thought you\'d never ask, so I\'ve never thought about it') 
        
        elif 'are you there' in query:
            query = query.replace("are you there","")
            speak('For you, always sir')

        elif 'how are you' in query:
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
            apologize = ['Sorry Sir!','Sorry!, my bad...','I apologize sir!']
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
            speak('I am Matrix Analitical Rapid-evolving Kernel based virtual machine, ' 
            'In short MARK , version code NV.')
            print("I am Matrix Analitical Rapid-evolving Kernel based virtual machine. In short MARK_version_code_NV.")

        elif 'standby' in query or 'stand by' in query:
            query = query.replace("standby", "")
            speak('I\'ll be waiting on you...')

        elif 'love you' in query:
            query = query.replace("love you","")
            shy = ['thank you, it\'s very nice of you','I\'m glad','love you too sir']
            speak(random.choice(shy))

        elif 'cute' in query or 'pretty' in query or 'so sweet of you' in query:
            query = query.replace("cute", "")
            query = query.replace("pretty", "")
            thank = ['oh gosh,..Thanks, you\'re far far to kind...','beauty is in the eyes of the beholder']
            speak(random.choice(thank))

        elif 'something about you'  in query or 'something about yourself' in query:
            speak('What can I say, My name is MARK, Matrix Analitical Rapid-evolving Kernel based virtual machine')
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
            speak('My friends are Jarvis, Friday, Karen, Sofia, Eva, Alpha-Go, AEGIS and my very close Cortana...')
            speak('You may have met and know few of them before hand...right!')

        elif 'right' in query:
            speak('Yah!')

        elif '' in query or ' ' in query:
            speak('I\'m sorry, I didn\'t get that')

        elif 'what can you do' in query or 'you can do' in query:
            query = query.replace("what can you do","")
            query = query.replace("you can do","")
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
            print("Web Search, Music, Date-Day & Time, Apps, Wikipedia search, Social Accounts, Spotify, School-Timetable, Mails, GPS")
            print("Weather Info, PDFs, Instagram Server-side data, Dark and Deep web access, Google maps-meeting-classroom, Info on ISS")
            print("Mars Orbital satellite data, ISS path prediction, Quadratic Equations, Area & perimeter of triangle.")

        # Internet Scarping and Search Protocol
        # E-mail transfering prototype
        elif 'email' in query:
            query = query.replace("email", "")
            try:
                speak("To whom do you want to send?")
                query1 = take_commands().lower()
                email_add = {"aditya": "adityasatapathy603@gmail.com", "michael": "michaelmaxx603@gmail.com", 
                "shreya": "shreya14012004@gmail.com", "mom": "bharatisatapathy75@gmail.com", "dad": "umakantas20@gmail.com",
                "vinay sir": "vinayblue@gmail.com", "avi": "avipatel15dec@gmail.com",
                "chinese": "nibharai003@gmail.com", "vansh": "vansh0891@gmail.com", "priyanshi": "riddhisiddhi2600@gmail.com",
                "himanshi": "himanshikumawat103@gmail.com", "kush": "pandyakush09@gmail.com", "mukesh sir": "mukeshshrimali14june@gmail.com",
                "adityasharma":"adisharmamufc@gmail.com", "naisha": "naisha.jain31@gmail.com", "taha": "kagzi.taha@gmail.com",
                "shrivastava": "shreyaashrivastava@gmail.com"}
                to = (email_add[query])
                speak("What should I say?")
                query1 = take_commands().lower()
                content = query1
                sendemail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry sir, email cannot be sent. Transfer interupted")

        elif 'YouTube' in query:
            query = query.replace("YouTube", "")
            speak('Is there anything specific you want to search in youtube...')
            #beta = str(input("Yes/No - "))
            query = take_commands().lower()
            if 'no' in query1 or 'nah' in query1:
                speak('Right, I\'ll just leave it for you to surf through it')
                speak('Opening Youtube...')
                webbrowser.get(edgedir).open("https://www.youtube.com")
            else:
                speak('What is it you want to look for...')
                #beta1 = str(input('Youtube search : '))
                query = take_commands().lower()
                webbrowser.get(edgedir).open("https://www.youtube.com/results?search_query="+query1)
                speak('heres all the matches of your search results')

        elif 'google' in query:
            query = query.replace("google", "")
            speak('Is there anything specific you want to search in google...')
            #beta2 = str(input("Yes/No - "))
            query1 = take_commands().lower()
            if 'no' in query1 or 'nah' in query1:
                speak('Right, I\'ll just leave it for you to surf through it')
                speak('Opening Google...')
                webbrowser.get(chromedir).open("google.com")
            else:
                speak('What is it you want to look for...')
                #beta3 = str(input('Google search : '))
                query1 = take_commands().lower()
                webbrowser.get(chromedir).open("https://google.com/?#q="+query1)
                speak('heres all the matches of your search results')

        elif 'whatsapp' in query:
            query = query.replace("whatsapp", "")
            speak('Opening Whatsapp...')
            webbrowser.get(edgedir).open("https://web.whatsapp.com/")

        elif 'instagram' in query:
            query = query.replace("instagram","")
            speak('Opening Instagram...')
            webbrowser.get(edgedir).open("https://www.instagram.com/aditya_satapathy_/")

        elif 'instagram login' in query:
            query = query.replace("instagram login","")
            speak('Conecting to server...Login Page access completed...Opening Instagram login...')
            webbrowser.get(edgedir).open("https://www.instagram.com/")

        #elif 'instagram post' in query or 'post' in query or 'insta post' in query:
        ##from instabot import Bot
            #try:
                #speak('Voice Command deactivated...')
                #bot = bot()
                #name = input("Enter your username : ")
                #word = input("Enter your password : ")
                #bot.login(username = name, password = word)
                #pic = input("Type in your photo path - ")
                #speak("What would be the caption for this")
                #cap = ("Enter Your caption - ")
                #bot.upload_photo(pic, caption = cap )
            #except Exception as i:
                #print(i)
                #speak("Post couldn\'t be uploaded due to network or technical error")
                #return "None"
            #return query

        elif 'mailbox' in query or 'mail' in query:
            query = query.replace("mailbox", "")
            speak('Opening Google Mail...')
            webbrowser.open("https://mail.google.com/mail/u/0/#inbox?compose=new")

        elif 'stackoverflow' in query:
            query = query.replace("stackoverflow", "")
            speak('Opening stackoverflow')
            webbrowser.get(edgedir).open("https://stackoverflow.com")

        elif 'tailblocks' in query:
            query = query.replace("tailblocks", "")
            speak('Opening Tailblocks...')
            webbrowser.get(edgedir).open("https://mertjf.github.io/tailblocks/")

        elif 'duckduckgo' in query:
            query = query.replace("duckduckgo", "")
            speak('Launching Duck-Duck-Go')
            webbrowser.get(edgedir).open("https://duckduckgo.com")

        elif 'sample paper' in query or 'paper' in query or 'question paper' in query or 'question' in query:
            webbrowser.get(edgedir).open("http://cbseacademic.nic.in/SQP_CLASSXII_2020-21.html")
            speak('Class twelveth Sample Question Paper & Marking Scheme for Exam twenty-twenty-twenty one, will be on your screen in a moment...')

        elif 'news' in query or 'headlines' in query:
            query = query.replace("news", "")
            speak('Accessing Google news...')   
            speak('What category of news you would like to hear...')
            query1 = take_commands().lower()
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

        elif 'specification' in query:
            query = query.replace("specification", "")
            speak('I am Matrix Analitical Rapid-evolving Kernel based virtual machine, ' 
            'In short MARK version code NV.Operating system on windows 10 pro of Microsoft '
            'Corporation. My system processor is Intel Core i5 3380M with a speed of 2.90 gigahertz. '
            'I have a 4GB RAM and work on a 64 bit operating system')

        elif '' in query:
            query = query.replace("", "")
            

        elif 'task kill' in query:
            query = query.replace("task kill", "")
            speak('rebooting all connected computer system, overriding the security codes with automated input protocol')
            speak('reboot completed')
            speak('overide successful')
            speak('task standby protocol activated')
            speak('Voice Command deactivated')
            speak('Sir, do you confirm the reboot of this computer')
            alpha = input("Enter Your Command : ")
            if 'no' in query:
                speak('right sir, deactivating task standby protocol')
            else:
                speak('standby, system will will undergo an automated restart procedure in t minus 10 seconds')
                os.system("shutdown /r /t 10")

        elif 'specification' in query:
            query = query.replace("specification", "")
            speak('I am Matrix Analitical Rapid-evolving Kernel based virtual machine.'
            'In short MARK version code unitrix. Operating system on windows 10 pro of Microsoft Corporation.'
            'My system processor is Intel Core i5 3380M with a speed of 2.90 gigahertz'
            'I have a 4GB RAM and work on a 64 bit operating system')
            
        elif 'shutdown' in query or 'shut down' in query:
            query = query.replace("shutdown", "")
            speak('initiating shutdown protocol')
            speak('I guess we\'ll be seeing each other soon')
            quit()

        elif 'sleep' in query:
            query = query.replace("sleep","")
            speak('initiating shutdown protocol')
            speak('I guess we\'ll be seeing each other soon')
            quit()

        elif 'command function override code 0' in query:
            query = query.replace("command function override code 0","")
            speak('Master Control Request detected...')
            speak('ovreride accepted, voice command deactivated')
            #mark self destruct in t-30s command code 000destruct0
            MARK = input("Enter Your Command: ")
            if 'mark self destruct in t-30s command code 000destruct0' in MARK:
                speak('Command code Zero confirmed...destruct sequence completed and engaged')
                speak('MARK program function will self-destruct in t minus 30 seconds')
                os.remove("C:\\Users\\Aditya Satapathy\\Desktop\\Python content\\MARK unitrix.py")
            else:
                speak('Aborting Master Control...')
                speak('Program require manual restart')
                exit()

        elif 'music' in query:
            query = query.replace("music", "")
            music_dir = 'C:\\Users\\Aditya Satapathy\\Music\\Playlists'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            query = query.replace("the time","")
            strTime = datetime.datetime.now().strftime("%H Hours :%M Minutes :%S Seconds")    
            speak(f"Sir, the time is {strTime}")
            print(strTime)

        elif 'whats the day' in query:
            query = query.replace("whats the day","")
            now = datetime.datetime.now()
            print(now.strftime('%H:%M:%S on %A, %B the %dth, %Y'))
            speak(now.strftime('%H:%M:%S on %A, %B the %dth, %Y'))

        elif 'vsc' in query:
            query = query.replace("vsc", "")
            codepath = "C:\\Users\\Aditya Satapathy\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)

        elif 'nox' in query:
            query = query.replace("nox", "")
            speak('Opening Nox Player...')
            noxpath = "C:\\Program Files (x86)\\Nox\\bin\\nox.exe"
            os.startfile(noxpath)

        elif 'tor' in query:
            query = query.replace("tor", "")
            torpath = "C:\\Tor Browser\\Browser\\firefox.exe"
            os.startfile(torpath)
        
        elif 'telegram' in query:
            query = query.replace("telegram", "")
            telegrampath = "C:\\Users\\Aditya Satapathy\\Desktop\\Telegram Desktop"
            os.startfile(telegrampath)

        elif 'file reader' in query:
            query = query.replace("file reader","")
            filereaderpath = "C:\\Program Files (x86)\\Foxit Software\\Foxit Reader"
            os.startfile(filereaderpath)

        elif 'python content' in query:
            query = query.replace("python content","")
            pythoncontentpath = "C:\\Users\\Aditya Satapathy\\Desktop"
            os.startfile(pythoncontentpath)

        elif 'class routine' in query:
            query = query.replace("class routine","")
            timetablepath = 'C:\\Users\\Aditya Satapathy\\Desktop\\Time Table.jpeg'
            os.startfile(timetablepath)
            print('Your current school time table')
            speak('Here is your current school time table according to my knowledge...')

        elif 'notes' in query:
            query = query.replace("notes", "")
            speak('showing your stick notes...')
            notespath = "C:\\Users\\Aditya Satapathy\\Desktop\\Python content\\MARK File_Links\\Sticky Notes.lnk"
            os.startfile(notespath)

        elif 'calc' in query:
            query = query.replace("calc","")
            speak('Opening calculator...')
            subprocess.call('calc.exe')

        elif 'notepad' in query:
            query = query.replace("notepad", "")
            speak('Opening notepad...')
            notepadpath = "C:\\Windows\\notepad.exe"
            os.startfile(notepadpath)

        elif 'wordpad' in query:
            query = query.replace("wordpad", "")
            speak('Opening wordpad...')
            wordpadpath = "C:\\Program Files (x86)\\Windows NT\\Accessories\\wordpad.exe"
            os.startfile(wordpadpath)

        elif 'movies' in query:
            query = query.replace("movies", "")
            speak('accessing video library...')
            moviepath = "C:\\Users\\Aditya Satapathy\\Desktop\\Python content\\MARK File_Links\\Movies & TV.lnk"
            os.startfile(moviepath)

        elif 'cmd' in query:
            query = query.replace("cmd", "")
            speak('Launching Command Prompt...')
            subprocess.call('cmd.exe')

        elif 'maps' in query:
            query = query.replace("maps", "")
            speak('Uplinking to satellite...enabling Global Positioning System...')
            mapspath = 'C:\\Users\\Aditya Satapathy\\Desktop\\Python content\\MARK File_Links\\Maps.lnk'
            os.startfile(mapspath)

        elif 'cards' in query:
            query = query.replace("cards","")
            speak('Opening Solitaire...')
            cardpath = 'C:\\Users\\Aditya Satapathy\\Desktop\\Python content\\MARK File_Links\\Microsoft Solitaire Collection.lnk'
            os.startfile(cardpath)

        elif 'photoshop' in query:
            query = query.replace("photoshop","")
            speak('Opening Adobe Photoshope Express version...')
            photoshoppath = 'C:\\Users\\Aditya Satapathy\\Desktop\\Python content\\MARK File_Links\\Adobe Photoshop Express.lnk'
            os.startfile(photoshoppath)

        elif 'weather' in query:
            query = query.replace("weather", "")
            weatherpath = "C:\\Users\\Aditya Satapathy\\Desktop\\Python content\\MARK File_Links\\Weather.lnk"
            os.startfile(weatherpath)
            speak('According to National Weather Forcast, todays local weather reports are as follows...')

        elif 'meeting' in query or 'meet' in query or 'google meet' in query:
            speak('Opening Google Meeting...')
            speak('Sir, I have chemistry and physics class links in my record,')
            speak('Do you want to access any of these...')
            #onlineclass = input('Any prefered class = ') 
            query1 = take_commands().lower()      
            if 'chemistry' in query1:
                query = query.replace("chemistry", "")
                speak('Heres your chemistry online class...')
                webbrowser.get(edgedir).open("https://meet.google.com/yne-uqcd-fbu")
            elif 'physics' in query1:
                query = query.replace("physics", "")
                speak('Heres your physics online class...')
                webbrowser.get(edgedir).open("https://meet.google.com/wap-vaeq-yvw")
            else:
                speak('Right, I\'ll just leave it for you to use it your way')
                webbrowser.get(edgedir).open("https://meet.google.com")

        elif 'ISS' in query or 'iss' in query:
            query = query.replace("ISS","")
            speak('As you wish, Locating International Space Station...,')
            speak('Calculating Alpha Station orbit coodinates,')
            print("Altitude-1.0827E+6 ft ;Orbital_speed-7.71km secE-1")
            speak('Uplinking to satellite. ISS spaceflight tracking map is operational')
            webbrowser.open("https://spotthestation.nasa.gov/tracking_map.cfm")
            speak('Tapping into this system is risky sir, I\'ve prepared a precaution briefing for you to entirely ignore.')

        elif 'ip class' in query:
            query = query.replace("ip","")
            speak('Opening IP classroom...')
            print('Opening IP classroom...')
            webbrowser.open("https://classroom.google.com/u/0/c/Njk4ODM3MTIzM1pa")

        elif 'chemistry class' in query:
            query = query.replace("chemistry","")
            speak('Opening Chemistry classroom...')
            print('Opening Chemistry classroom...')
            webbrowser.open("https://classroom.google.com/u/0/c/MTE2OTE1NjQzNzc2")

        elif "where is" in query:
            query = query.split(" ")
            location = query[2]
            speak("Hold on boss, I will show you where " + location + " is.")
            webbrowser.open("https://www.google.nl/maps/place/" + location)

        elif 'hentai' in query or 'sex games' in query or 'porn games' in query:
            query = query.replace("hentai","")
            speak('Accessing Naughty web...')
            webbrowser.get(edgedir).open("https://www.gamesofdesire.com/category/meet-and-fuck-games/")

        elif 'x comics' in query:
            query = query.replace("x comics","")
            humor1 = ["Getting kinky sir","feeling horny sir","ready to have some fun and get naughty"]
            speak(random.choice(humor1))
            webbrowser.get(tordir).open("https://comics.8muses.com/comics")
        