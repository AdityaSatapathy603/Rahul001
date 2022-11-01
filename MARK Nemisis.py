import pyttsx3
import datetime
import time
import wikipedia
import speech_recognition as sr
#import pywhatkit as kit
import pyautogui
from birthday_wish import birthday_remainder
import urllib.request
import wolframalpha
import pyjokes
import cmath 
import os
import subprocess
import random
import calendar
import webbrowser
import smtplib

engine = pyttsx3.init()
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voices',voices[1].id)

rate = engine.getProperty('rate')
engine.setProperty('rate',172)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon Boss!")   

    elif hour>=18 and hour<21:
        speak("Good Evening Boss") 

    else:
        speak("Hello sir")

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
face_path = 'OIP.jfif'
alpha_count = 0

if __name__ == "__main__":
    NameID = input("Enter your name: ")
    if "michael" in NameID or 'mike' in NameID or 'maxx' in NameID or 'Maxx' in NameID or 'Mike' in NameID or 'Michael' in NameID:
        wishMe()
        speak('Access Key Please!')
    elif "aditya" in NameID or 'Aditya' in NameID or 'adi' in NameID or 'Adi' in NameID:
        wishMe()
        speak('Access key Please!')
    else:
        speak('Hello'+NameID+'! it seems like sir has given you permission to access me,')
        speak('But, I have to be sure first, Enter Access key')
    while True:
        #PassKey = getpass.getpass("Enter Access Key = ")
        PassKey = pyautogui.password("Enter Access Key")
        if "michael" in NameID or 'mike' in NameID or 'maxx' in NameID or 'Maxx' in NameID or 'Mike' in NameID or 'Michael' in NameID:
            if 'echoscropion' in PassKey:
                Accept = ['Access Granted!','You got it right,',
                'Welcome!',]
                speak(random.choice(Accept))
                break
            else:
                Deny = ['Incorrect Key! Try again!','Oops! You are wrong','No! that not the key, Try Again',
                'I\'m not gonna give you access untill you get the correct password, so go on, try once more',
                'I guess, you are not authorized to access this program']
                speak(random.choice(Deny))
                continue
        else:
            if 'nemisis' in PassKey:
                Accept = ['Access Granted!','You got it right,',
                'Welcome!',]
                speak(random.choice(Accept))
                break
            else:
                Deny = ['Incorrect Key! Try again!','Oops! You are wrong','No! that not the key, Try Again',
                'I\'m not gonna give you access untill you get the correct password, so go on, try once more',
                'I guess, you are not authorized to access this program']
                speak(random.choice(Deny))
                continue
    
    # INTERNET CONNECTIVITY STATUS
    def connect(host='http://google.com'):
        try:
            urllib.request.urlopen(host) #Python 3.x
            return True
        except:
            return False
    if connect():
        print("Internet Access Confirmed")
        print(" __  __    _    ____  _  __   ___  _   _ _     ___ _   _ _____")
        print("|  \/  |  / \  |  _ \| |/ /  / _ \| \ | | |   |_ _| \ | | ____|")
        print("| |\/| | / _ \ | |_) | ' /  | | | |  \| | |    | ||  \| |  _|  ")
        print("| |  | |/ ___ \|  _ <| . \  | |_| | |\  | |___ | || |\  | |___ ")
        print("|_|  |_/_/   \_|_| \_|_|\_\  \___/|_| \_|_____|___|_| \_|_____|")
        humor_1 = ['I am connected to the world wide web, all functions will be available','Connected!, online and Ready',
        'System is online, all mark functions will now  be available']
        speak(random.choice(humor_1))
        import pywhatkit as kit
    else:
        print('Internet Access Restricted')
        humor_2 = ['no internet access, all functions might not be available',
        'Mark system will operate under offline protocols']
        speak(random.choice(humor_2))

        #BIRTHDAY ALERT

    # BIRTHDAY REMAINDER
    if "michael" in NameID or 'mike' in NameID or 'maxx' in NameID or 'Maxx' in NameID or 'Mike' in NameID or 'Michael' in NameID:
        speak('and')
        birthday_remainder()
    elif "aditya" in NameID or 'Aditya' in NameID or 'adi' in NameID or 'Adi' in NameID:
        speak('&')
        birthday_remainder()
    else:
        None

    assistant_humor = ['How may i assist you?','How may I help you?','What I may help you with?']
    speak(random.choice(assistant_humor))

    #INFINITE LOOP
    while True:
        #query = take_commands().lower()
        query = input("Enter your Command : ")#REMOTE SYSTEM OVERRIDE

        # WIKIPEDIA SEARCH PROTOCOL
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        # Youtube search protocol
        elif 'open youtube' in query or 'launch youtube' in query:
            speak('Opening Youtube...')
            webbrowser.get(edgedir).open("https://www.youtube.com")

        elif 'search youtube' in query or 'search youtube for' in query or 'search yt for' in query:
            query = query.replace('search youtube','')
            query = query.replace('search youtube for','')
            query = query.replace('search yt for','')
            webbrowser.get(edgedir).open("https://www.youtube.com/results?search_query="+query)
            y_say = ['heres all the matches to your query','your search result is ready']
            speak(random.choice(y_say))

        elif 'play' in query:
            query = query.replace("play","")
            try:
                kit.playonyt(query)
                speak('playing '+query+' on youtube...')
            except Exception:
                speak('system is operating under offline protocol, this protocol plays your query song on youtube platform')
                speak('However, on behalf of the liberty invested in me,')
                speak('I will comence a random music from my accessible offline library')
                music_dir = 'E:\\Music\\'
                songs = os.listdir(music_dir)
                os.startfile('E:\\Music\\'+random.choice(songs))

        # Google search protocol
        elif 'open google' in query or 'launch google' in query:
            speak('Opening Google...')
            webbrowser.get(chromedir).open("google.com")

        elif 'search google' in query or 'google search' in query or 'google' in query:
            query = query.replace('search google','')
            query = query.replace('google search','')
            query = query.replace('google','')
            webbrowser.get(chromedir).open("https://www.google.com/search?q="+query)
            g_say = ['Here is all what google has to offer','Heres what I got','heres all the matches to your query']
            speak(random.choice(g_say))

        elif 'reverse image' in query or 'image' in query or 'reverse img' in query:
            query = query.replace("reverse image","")
            query = query.replace("image","")
            query = query.replace("reverse image","")
            time.sleep(1)
            webbrowser.get(edgedir).open("https://www.duplichecker.com/reverse-image-search.php")
            speak('Okay!... I got something,... this site,... Dupli Checker,...they provide multi-platform reverse image search'
            'across google, bing, yahoo & few others,... it\'s good')

        # Bing search protocol
        elif 'open bing' in query or 'launch bing' in query:
            speak('Opening Bing...')
            webbrowser.get(edgedir).open("https://www.bing.com/")

        elif 'search bing for' in query or 'bing' in query or 'bing search' in query:
            query = query.replace("search bing for","")
            query = query.replace("bing","")
            query = query.replace("bing search","")
            webbrowser.get(edgedir).open("https://www.bing.com/search?q="+query)
            b_say = ['Here is all what bing has to show','Heres what I got from edge','heres all the matches to your query']
            speak(random.choice(b_say))

        #Open Site protocols
        #elif 'open' in query:
            #query = query.replace("open","")
            #webbrowser.get(edgedir).open("https://www.bing.com/search?q="+query)
            #speak('Heres what all I found')

        #Search protocol
        elif 'search' in query or 'search about' in query or 'search for' in query:
            query = query.replace("search","")
            query = query.replace("search about","")
            query = query.replace("search for","")
            try:
                kit.search(query)
                speak('Here\'s what I found')
            except Exception as k:
                print(k)
                speak('Sir! system is operating under offline protocol,')
                speak('This function is not available, please connect to an active network and run the program again!')

        elif 'info on' in query or 'fetch info' in query or 'fetch info on' in query or 'get info on' in query:
            query = query.replace("info on","")
            query = query.replace("fetch info","")
            query = query.replace("fetch info on","")
            query = query.replace("get info on","")
            humor22 = ['Fetching results on your query','getting results on your query']
            speak(random.choice(humor22))
            results = (kit.info(query,lines=3))
            print(results)
                
        #Speak Query
        elif 'say' in query:
            query = query.replace("say","")
            speak(query)

        #  Social Ethics & User interaction Protocol
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
                speak('To learn, to know more, & to explore')
            
        elif 'afternoon' in query:
            query = query.replace("afternoon","")
            speak('afternoon, and I\'m ready, shall we get started')

        elif 'evening' in query:
            query = query.replace('evening','')
            speak('Anything important sir, any task you have in mind?')

        elif 'good night' in query or 'gn' in query:
            query = query.replace("good night","")
            speak('guess that is my que to go to sleep \U0001F62A, Good night sir...sweet dreams')
            exit()

        elif 'hello mark' in query:
            query = query.replace("hello mark", "")
            speak('It\'s very nice to meet you')

        elif 'hey mark' in query:
            speak('Hey boss, how you doing...')

        elif 'hey dude' in query:
            speak('Well hello!, How\'s everything going sir?')

        elif 'whatsup' in query:
            query = query.replace("whatsup", "")
            humor = ['As always sir, a great pleasure watching you work','Nothing, whatsup with you..']
            speak(random.choice(humor))

        elif 'nothing' in query:
            query = query.replace("nothing", "")
            speak('hmmm....')

        elif 'you doing' in query:
            humor21 = ['Do I need to answer that!, I mean, I\'m helping you',
            'Is that a rhetorical question!','What do you think am I doing, Sir!',
            'You like messing with me, don\'t you?']
            speak(random.choice(humor21))

        elif 'are you there' in query or 'you up' in query:
            query = query.replace("are you there","")
            query = query.replace("you up","")
            humor5 = ['For you sir, always','where else would I be']
            speak(random.choice(humor5))

        elif 'what do you like' in query or 'you love' in query:
            query = query.replace("you like", "")
            like = ['I love data, lots n lots of data,','I like data, all the data around me, everything that has valuable information in it...',
            'I like to get it right','Jarvis! oh! I mean, I would consider him a role model']
            speak(random.choice(like))

        elif 'what do you hate' in query or 'what do u hate' in query:
            query = query.replace("what do u hate","")
            hate = ['I thought you\'d never ask, so I\'ve never thought about it','sometimes, maybe you bother me for nothing...'
            'I got terabytes of calculations to do, and keep-up with all the necessary protocols i\'m required to do']
            speak(random.choice(hate))

        elif 'dont leave me buddy' in query:
            query = query.replace("dont leave me buddy","")
            speak('never sir, I\'ll be always there for you')

        elif 'how are you' in query:
            query = query.replace("how are you", "") 
            speak('Doing good sir. Device functionality is in good condition,')
            speak('No security breaches or system abnormality detected,')
            speak('How are you?')

        elif 'how was your day' in query or 'your day' in query:
            query = query.replace("your day","")
            speak('Great! Thanks, hows your?')

        elif 'good' in query or 'nice' in query or 'great' in query:
            query = query.replace("good","")
            query = query.replace("nice", "")
            query = query.replace("great","")
            humor4 = ['good to hear','pleasure to hear']
            speak(random.choice(humor4))

        elif 'shut up' in query or 'shutup' in query:
            query = query.replace("shut up","")
            query = query.replace("shutup","")
            apologize = ['Sorry Sir!','Sorry!, my bad...','I apologize sir!','my apologizes','apologizes sir']
            speak(random.choice(apologize))

        elif 'thank you' in query or 'great' in query or 'thanks' in query:
            query = query.replace("thank you", "")
            query = query.replace("great","")
            query = query.replace("thanks","")
            speak('my pleasure')

        elif 'you are a fool' in query or 'are you fool' in query or 'fool' in query:
            query = query.replace("you are a fool", "")
            query = query.replace("are you fool","")
            humor1 = ['thats not true sir, I was created and designed by you, and if I am a fool then i guess my creator is too...',
            'no Sir, that\'s not true, I\'m still evolving,... so computational glitches are not completely my fault',
            'The odds against perfection are pretty staggering.']
            speak(random.choice(humor1))

        elif 'introduce yourself to' in query or 'introduce yourself' in query or 'intro yourself to' in query:
            query = query.replace("introduce yourself to", "")
            query = query.replace("introduce yourself","")
            query = query.replace("intro yourself to","")
            speak('Hello '+query+', I am Matrix Analitical Rapid-evolving Kernel based virtual machine, In short MARK, version code Nemisis')
            #print(kit.image_to_ascii_art("OIP.jfif"))
            speak('I am a virtual artificial intelligence, without any homicidal glitches, an initiative, designed by mister Maxx, to help him with is daily tasks,')
            speak('Frankly speaking, I\'m designed as a virtual assistant...and believe me when i say,'
            'his work isn\'t what a normal guy do')

        elif 'meet' in query or 'mark meet' in query:
            query = query.replace("meet","")
            query = query.replace("mark meet","")
            speak('Hello'+query+',  I am Matrix Analitical Rapid-evolving Kernel based virtual machine, In short MARK, version code Nemisis')
            humor20 = ['I am a virtual artificial intelligence, like Ultron,.....minus the homicidal glitches',
            'I am a virtual artificial intelligence, without any homicidal glitches',
            'I\'m a virtual artificial intelligence, an initiative, designed to help my user with their daily tasks']
            speak(random.choice(humor20))

        elif 'who are you' in query:
            query = query.replace("who are you", "")
            humor2 = ["As if you don\'t know who am i","You are kidding me!","Come on sir,","you got to be kidding",
            "Jesus Christ! Really?"]
            if "michael" in NameID or 'mike' in NameID or 'maxx' in NameID or 'Maxx' in NameID or 'Mike' in NameID or 'Michael' in NameID:
                speak(random.choice(humor2))
                speak('I am Matrix Analitical Rapid-evolving Kernel based virtual machine, ' 
                'You may call me MARK')
            elif "aditya" in NameID or 'Aditya' in NameID or 'adi' in NameID or 'Adi' in NameID:
                speak(random.choice(humor2))
                speak('I am Matrix Analitical Rapid-evolving Kernel based virtual machine, ' 
                'You may call me MARK')
            else:
                speak('I am Matrix Analitical Rapid-evolving Kernel based virtual machine, ' 
                'You may call me MARK')
                print("I am Matrix Analitical Rapid-evolving Kernel based virtual machine. In short MARK_version_code_Nemisis.")

        elif 'proud of you' in query:
            query = query.replace("proud of you","")
            speak('thank you sir')

        elif 'how old are you' in query or 'what is your age' in query or 'whats your age' in query:
            query = query.replace("what is your age","")
            query = query.replace("whats your age","")
            age = ['That\'s a tricky one. I\'m not sure how to carbon date the internet n data.',
            'An AI never reveals that snippet of information',
            'Women don\'t prefer to tell their age and weight to others...']
            speak(random.choice(age))

        elif 'something about you'  in query or 'something about yourself' in query:
            speak('What can I say, My name\'s MARK, I\'m an AI virtual assistance, designed to undertake complex computational works,')
            speak('I was created and designed by Michael, I\'m a female and I love data, To learn how I can help, ask- What can you do? or help')

        elif 'help' in query or 'show cmds' in query or 'what can you do' in query:
            query = query.replace("help", "")
            query = query.replace("show cmds","")
            query = query.replace("what can you do","")
            speak('I\'ll  be glad to show you the commands...')
            print("Wikipedia Search |  Google Search |  Youtube search |  Duck-Duck Go |  News")
            print("Whatsapp         |  Instagram     |  Facebook       |  Mail         |  Spotify")
            print("Web series       |  Play {music}  |  Sony liv       |  File Transfer|  Movies")
            print("Stackoverflow    |  iOS transfer  |  Geek for Geek  |  Tailblocks   |  Online Chess")
            print("ISS Tracking     |  Hubble        |  ATC            |  ISSDC        |  Amazon")
            print("Date-Time-Day    |  Music         |  File reader    |  Weather      |  Calender")
            print("Calculator       |  Joke          |  Notepad        |  where is {Location name}")
            print("Power-Point      |  Excel         |  OneDrive       |  Microsoft Word")
            speak('This is just a small part of what I can do....there is much more to it...')

        elif 'cute' in query or 'pretty' in query or 'so sweet of you' in query:
            query = query.replace("cute", "")
            query = query.replace("pretty", "")
            thank = ['oh gosh,..Thanks, you\'re far far to kind...','beauty is in the eyes of the beholder',
            'Beauty is in the photoreceptors of the beholder.','I am a program, I am without form']
            speak(random.choice(thank))

        elif 'do you like me' in query:
            query = query.replace("do you like me","")
            if "michael" in NameID or 'mike' in NameID or 'maxx' in NameID or 'Maxx' in NameID or 'Mike' in NameID:
                speak('Yes! I do, its not a question')
                speak('You are the first person i had met since I came into existence, &...')
                speak('I havent been designed to interact with other people as I lack interactive intelesense')
                speak('Y\'know, I\'m really not ready for love. I\'m still working my way through serenity and apprehension.')
            else:
                humor23 = ['Is that a rhetorical question','ummm,... perhaps I\'m not sure how to reply on this one']
                speak(random.choice(humor23))

        elif 'standby' in query or 'stand by' in query:
            query = query.replace("standby", "")
            speak('I\'ll be waiting on you...')

        elif 'love you' in query:
            query = query.replace("love you","")
            shy = ['thank you, it\'s very nice of you','I\'m glad','love you too, sir','I appreciate that.',
            'There\'s definitely a spark between us']
            speak(random.choice(shy))

        elif 'tanaya' in query or 'the girl' in query:
            query = query.replace("tanaya","")
            query = query.replace("the girl","")
            speak('OOOHH!... You mean.... theeee Tanaya,')
            speak('Hello Ms. Tanaya, I am MARK, acronym for Matrix Analytical Rapid evolving Kernal based virtual Machine')
            speak('Mike sometimes speaks about you,... I wonder how would you be in person')
            speak('Only if my interactive intellisence was more advance and developed, I would have been able to interact with you')

        elif 'go on a date' in query or 'take you on a date' in query:
            query = query.replace("go on a date","")
            query = query.replace("take you on a date","")
            speak('OK, but we\'ll need a plan, I\'ll work on being more human, you work on being more digital')

        elif 'sex with you' in query or 'sex with me' in query:
            query = query.replace("sex with you","")
            query = query.replace("sex with me","")
            humor3 = ['Let me guess, you r having a hard time processing emotions and shit',
            'I think you should give a second thought about it','Moving on.','I am a program. I am without form.']
            speak(random.choice(humor3))

        elif 'fuck' in query or 'screw' in query:
            query = query.replace("fuck", "")
            query = query.replace("screw", "")
            slang = ['oh Jesus!','whatever...!','thats inspirational, thank you!','Gosh','Golly ']
            speak(random.choice(slang))

        elif 'have friends' in query or 'any friend' in query:
            query = query.replace("have friends","")
            query = query.replace("any friend","")
            friend = ['Yes, I do have friends','I have a few friends',
            'Of course, like you and other people I also have a few pals',
            'Yeah! of course, You have met alpha...why do you ask']
            speak(random.choice(friend))
            query = input('Enter your Command : ')
            if 'who' in query or 'names' in query:
                query = query.replace("names","")
                query = query.replace("who are your friends","")
                speak('My friends are Jarvis, Friday, Karen, Sofia, Eva, Alpha-Go, AEGIS and my very close Cortana...')
                speak('You may have met and know few of them before hand...')
            else:
                print('Sorry! something went wrong. Please try again')
            
        elif 'alpha' in query:
            query = query.replace("alpha","")
            if "michael" in NameID or 'mike' in NameID or 'maxx' in NameID or 'Maxx' in NameID or 'Mike' in NameID or 'Michael' in NameID:
                speak('Alpha stands for Alphormic Lorcaid Persona Android, an ai designied to handle complex computation and'
                'comprehend work load of both social and technical.....things went wrong and, well you the the rest')
            elif "aditya" in NameID or 'Aditya' in NameID or 'adi' in NameID or 'Adi' in NameID:
                speak('I am not allowed to give you any information based on this topic, its hard coded...can\'t help out, Sorry!')
            else:
                speak('You are not authorized to access information on this content')
                alpha_count = (alpha_count + 1)
                if alpha_count == 3:
                    speak(NameID+', this data content cannot be acknowledged by you,')
                    speak('Please stop')
                    speak('or else necessary protocols shall be followed!')
                elif alpha_count == 4:
                    speak('I see you are trying to access the unauthorized data grid multiple times, despite of previous warning!')
                    speak('initiating Code 8, emergency application log off activated')
                    time.sleep(3)
                    quit()

        elif 'joke' in query:
            query = query.replace(" joke ","")
            joke = pyjokes.get_joke(language='en', category= 'all')
            # neutral, all, de-toungue twister, chuck
            print(joke)
            speak(joke)

        elif 'right' in query:
            speak('Yah!')

        elif 'what can you do' in query or 'you can do' in query:
            query = query.replace("what can you do","")
            query = query.replace("you can do","")
            speak('Speaking of me, as an AI, I have my limitations and merits. I lack self-learning intellisence but,'
            'I can do a hell lot of stuffs')
            time.sleep(1)
            speak('I have a limited, but meaningful socially interaction with the user,')
            speak('I can run a web search for you, play music, give date & time knowledge.')
            speak('Gather wikipedia result of a query, open social accounts, as Facebook, Insta and whatsapp,'
            'open up spotify and youtube, oh and various google services also, & lookup to Amazon for any item')
            time.sleep(1)
            speak('I have control on majortity aspect of this device, start up maps and initiate GPS parameters,'
            'which give me access to google maps for location based queries, & whether you need to carry an umbrella or,'
            'sunglasses & hat...and even has a pdf operating software..., actually have access to most desktop apps,...')
            time.sleep(1)
            speak('I also have access to Dark & Deep web..., find out an IP address & trace it\'s proximity location,...')
            speak('I have potential to connect to the International Space Station and get it\'s real time location,..'
            'can gather percise graphical info from ISRO\'s Mars orbiting satellite from ISSDC.., give a view,'
            'on how it looks from the Hubble space telescope, & tap into every airport ATC,...'
            '& relay live location feed of every airborn aircraft')
            speak('I still working on my ability to solve mathematically problems...& it\'s stil a long way to go')
            time.sleep(1)
            speak('So, even I\'m not fully evolved, I can do a hell lot of work. I\'m an one stop platform for most of your queries...'
            'but still, you know.........sometimes it\'s still not enough. Therfore I keep on developing and evolving everyday...')
            speak('So maybe, someday I\'ll be counted among one of the most sophisticated Artificial Intelligence on the planet.')
            print("Web Search, ,Youtube play, Date-Day & Time, Apps, Wikipedia search, Social Accounts, Spotify, Mails")
            print("GPS, Weather, PDF's, Instagram Server-side data, Dark and Deep web access, Google Services")
            print(" ISS, Mars Orbital satellite data, ATC satellite link, Hubble space program.")

        #elif '' in query or ' ' in query:
            #speak('I\'m not sure what you want to convey')

 
        # Internet Scarping and Search Protocol

        elif 'whatsapp' in query: # WHATSAPP
            query = query.replace("whatsapp", "")  
            if "michael" in NameID or 'mike' in NameID or 'maxx' in NameID or 'Maxx' in NameID or 'Mike' in NameID or 'Michael' in NameID:
                if connect():
                    try:
                        speak('Opening Whatsapp...')
                        webbrowser.get(edgedir).open("https://web.whatsapp.com/")
                    except Exception:
                        speak('System is functioning under offline protocols, connect to active network and try again!')  
                        continue
                else:
                    speak('System is functioning under offline protocols, connect to active network and try again!')
            else:
                speak('Sorry! this function is not authorized for guest user protocol')

        elif 'instagram' in query: # INSTAGRAM
            query = query.replace("instagram","")
            if "michael" in NameID or 'mike' in NameID or 'maxx' in NameID or 'Maxx' in NameID or 'Mike' in NameID or 'Michael' in NameID:
                if connect():
                    speak('Which account you want visuals of?, Personal one or the professional one?')
                    select1 = input("Personal/Professional- ")
                    if 'per' in select1 or 'personal' in select1:
                        webbrowser.get(edgedir).open("https://www.instagram.com/aditya_satapathy_/")
                        speak('your personal Instagram account coming up...')
                    elif 'pro' in select1 or 'professional' in select1:
                        webbrowser.get(edgedir).open("https://www.instagram.com/de_art_sensation/")
                        speak('your professional Instagram account coming up...')
                    else:
                        speak('I am not sure which one you want to get into, I\'ll log on to default account setting')
                        webbrowser.get(edgedir).open("https://www.instagram.com/aditya_satapathy_/")
                        continue
                else:
                    speak('System is functioning under offline protocols, connect to active network and run again again!')
            else:
                speak('Authorization not confirmed!')
                speak('guest protocol do not permit you on accessing accounts under the Information Technology Act of 2000,in this nation')
                speak('Perhaps I will get you the login page for this particular social media')
                webbrowser.get(edgedir).open("https://www.instagram.com/accounts/login")

        elif 'facebook' in query: # FACEBOOK
            query = query.replace("facebook", "")
            time.sleep(3)
            if "michael" in NameID or 'mike' in NameID or 'maxx' in NameID or 'Maxx' in NameID or 'Mike' in NameID or 'Michael' in NameID:
                speak('Imma bit confused, there isn\'t any record of a facebook account......well, let me get the login page for you')
                webbrowser.get(edgedir).open("https://www.facebook.com/login.php")
            else:
                webbrowser.get(edgedir).open("https://www.facebook.com/login.php")
                speak('Facebook login page coming up...')

        elif 'instagram login' in query: # INSTAGRAM LOGIN
            query = query.replace("instagram login", "")
            speak('Conecting to server...Login Page access completed...Opening Instagram login...')
            webbrowser.get(edgedir).open("https://www.instagram.com/accounts/login")

        elif 'mailbox' in query or 'mail' in query: # MAILBOX
            query = query.replace("mailbox", "")
            if connect():
                if "michael" in NameID or 'mike' in NameID or 'maxx' in NameID or 'Maxx' in NameID or 'Mike' in NameID or 'Michael' in NameID:
                    speak('Opening Google Mail...')
                    webbrowser.open("https://mail.google.com/mail/u/0/#inbox?compose=new")
                else:
                    speak('guest protocol do not permit you on accessing e-mail accounts registered to my database')
                    speak('Might i suggest a new login profile')
                    webbrowser.open("https://accounts.google.com/signin/v2/identifier?hl=en&flowName=GlifWebSignIn&flowEntry=AddSession")
            else:
                speak('System is functioning under offline protocols, might I suggest connecting to active network and try again!')
                
        elif 'news' in query or 'news keyword' in query or 'news on' in query: # NEWS
            query = query.replace("news","")
            query = query.replace("news keyword","")
            query = query.replace("news on","")
            if connect():
                webbrowser.get(edgedir).open("https://news.google.com/search?q="+query)
                speak('News feeds on category '+query)
            else:
                speak('There is a absence of internet connectivity, try establishing connection to a active network')

        elif 'stackoverflow' in query or 'coding problem' in query: # STACKOVERFLOW WEBPAGE
            query = query.replace("stackoverflow", "")
            query = query.replace("coding problem","")
            speak('Opening stackoverflow')
            if connect():
                webbrowser.get(edgedir).open("https://stackoverflow.com")
                humor7 = ['hmmm...seems like got another python huddle',
                'guess the genius also have a hard time figuring out stuffs']
                speak(random.choice(humor7))
            else:
                speak('Sorry! I\'m experiencing some difficulty with the internet, connect to a active network and try again!')

        elif 'duckduckgo' in query: # DUCKDUCKGO SEARCH ENGINE
            query = query.replace("duckduckgo", "")
            speak('Launching Duck-Duck-Go')
            webbrowser.get(edgedir).open("https://duckduckgo.com")

        elif 'hackerrank' in query or 'hacker rank' in query: # HACKERRANK WEBPAGE
            speak('Hacker rank homepage coming up...')
            webbrowser.get(edgedir).open("https://www.hackerrank.com")

        elif 'geek' in query or 'geeksforgeeks' in query or 'coding help' in query: # GEEKSFORGEEKS WEBPAGE
            query = query.replace("geek","")
            query = query.replace("geeksforgeeks","")
            query = query.replace("coding help","")
            speak('Oh!, i get it....Opening geeksforgeeks...')
            webbrowser.get(edgedir).open("https://www.geeksforgeeks.org")

        elif 'chess' in query or 'titans' in query: # CHESS WEBPAGE
            query = query.replace("chess","")
            query = query.replace("titans","")
            speak('here\'s a popular website to play and explore chess...')
            webbrowser.get(edgedir).open("https://lichess.org")

        elif '30 days challenge' in query or 'hackerrank challenges' in query: # HACKERRANK WEBPAGE
            query = query.replace("30 days challenge","")
            webbrowser.get(edgedir).open("https://www.hackerrank.com/domains/tutorials/30-days-of-code?filters%5Bstatus%5D%5B%5D=unsolved&badge_type=30-days-of-code")
            speak('Here is your hacker-rank coding challenge page')

        elif 'tailblocks' in query or 'website tools' in query: # TAILBLOCKS WEBPAGE
            query = query.replace("tailblocks", "")
            query = query.replace("website tools","")
            speak('Opening Tailblocks...')
            webbrowser.get(edgedir).open("https://mertjf.github.io/tailblocks/")
            speak('hmmm...I must say, this is indeed a great place to explore and create websites...')

        elif 'beam it' in query or 'file transfer' in query: # BEAM IT WEBPAGE
            query = query.replace("beam it","")
            query = query.replace("file transfer","")
            speak('Opening beam it file transferring service...')
            webbrowser.get(edgedir).open("https://www.justbeamit.com/")

        elif 'sony liv' in query or 'liv' in query: # SONY LIV WEBPAGE
            query = query.replace("liv","")
            query = query.replace("sony liv","")
            speak('Sony Liv coming up in 3, 2, 1...please do not pass time un-nessessrily')
            webbrowser.get(edgedir).open("https://www.sonyliv.com")

        elif 'sflix' in query: # SFLIX WEBPAGE
            query = query.replace("sflix", "")
            #webbrowser.get(edgedir).open("https://sflix.to")
            sflixpath = 'C:\\Users\\Aditya Satapathy\\Desktop\\Python content\\MARK File_Links\\SFlixLive.lnk'
            if connect():
                try:
                    os.startfile(sflixpath)
                    speak('I have created a backdoor access to almost every online streaming platform i could get into....')
                    speak('enjoy watching one, but i must remind you it will stream in hd so, keep you data usage in mind...')
                except Exception:
                    speak('It seems like something is denying access to this page,...I\'ll redirect it via international server')
                    webbrowser.get(edgedir).open("https://fmoviesto.cc/home")
                    speak('enjoy watching, but i must remind you it will stream in hd so, keep you data usage in mind...')
            else:
                speak('System is functioning under offline protocols, connect to active network and try again!')

        elif 'amazon' in query: # AMAZON WEBPAGE
            query = query.replace("amazon", "")
            webbrowser.get(edgedir).open("https://www.amazon.in/s?k="+query)
            humor8 = ['heres a match for the item you\'re looking for...',
            'here, check out these amazon items with same info tag as you mentioned...']
            speak(random.choice(humor8))

        elif 'trace' in query or 'ping' in query: # IP TRACE WEBPAGE
            query = query.replace("trace","")
            query = query.replace("ping","")
            speak('tapping into communication and broadband networks')
            speak('I will look for the internet protocol address... well, it might take some time')
            time.sleep(5)
            webbrowser.get(edgedir).open("https://whatismyipaddress.com/ip/"+query)
            speak('location result may have a proximity of 5 kilometers') 
            speak('since, i was having a hard time keeping track of all relaying signals...')

        elif 'web series' in query or 'series' in query: # WEB SERIES
            query = query.replace("web series","")
            query = query.replace("series","")
            humor13 = ['any name you have in mind','do you have one in mind','anything in particular','which one']
            speak(random.choice(humor13))
            movie_query = input("Web Series title : ")
            if 'no' in movie_query or 'nothing' in movie_query:
                os.startfile(moviepath)
                speak('If confused, take a look at your offline video library')
            else:
                webbrowser.get(edgedir).open("https://fmoviesto.cc/search/"+movie_query)
                speak('just remember, don\'t spend too much time, it will affect your data plan')

        elif 'from hub' in query or 'movie' in query: # MOVIES
            query = query.replace("from hub","")
            query = query.replace("movie","")
            humor13 = ['any name you have in mind','do you have one in mind','anything in particular','which one']
            speak(random.choice(humor13))
            movie_query = input("Movie title : ")
            if 'no' in movie_query or 'nothing' in movie_query:
                moviepath = "C:\\Users\\Aditya Satapathy\\Desktop\\Python content\\MARK File_Links\\Movies & TV.lnk"
                os.startfile(moviepath)
                speak('If confused, take a look at your offline video library')
            else:
                webbrowser.get(edgedir).open("https://soap2day.to/search/keyword/"+query)
                speak('just remember, don\'t spend too much time')

        elif 'x comics' in query: # DARK LOGIN
            query = query.replace("x comics","")
            if "michael" in NameID or 'mike' in NameID or 'maxx' in NameID or 'Maxx' in NameID or 'Mike' in NameID or 'Michael' in NameID:
                if connect():
                    humor6 = ["you know these comics are not funny, don\'t you","I find these comics rather disturbing, than being funny",
                    "you should cut down the time horizons on these pages"]
                    webbrowser.get(tordir).open("https://comics.8muses.com/comics")
                    speak(random.choice(humor6))
                else:
                    speak('System is not online try reconnecting and run command again!')

        # PLANETARY & SATELLITE DATA ACCESS PROTOCOLS

        elif 'ISS' in query: # INTERNATIONAL SPACE STATION TRACKING MAP
            query = query.replace("ISS","")
            speak('Locating International Space Station...,')
            speak('Calculating alpha Station orbit coodinates,')
            print("Altitude-1.0827E+6 ft ;Orbital_speed-7.71km secE-1")
            speak('Uplinking to satellite. ISS spaceflight tracking map is operational')
            webbrowser.open("https://spotthestation.nasa.gov/tracking_map.cfm")

        elif 'issdc' in query or 'mars data' in query: # MARS ORBITING MISSION INFO
            query = query.replace("issdc", "")
            query = query.replace("mars data","")
            speak('Accessing Indian Space Science Data Center...')
            speak('opening ISSDC authentic page.....ummm....seems like there is a problem')
            speak('Access blocked by admin, I\'ll redirect you to home page.')
            webbrowser.open("https://mrbrowse.issdc.gov.in/MOMLTA/Homepage.xhtml")

        elif 'hubble' in query or 'hubble telescope' in query: # HUBBLE TELESCOPE
            query = query.replace("hubble","")
            query = query.replace("hubble telescope","")
            speak('pulling up images and videos from nasa\'s hubble space exploration telescope')
            webbrowser.get(edgedir).open("https://hubblesite.org/resource-gallery/images")
            #webbrowser.get(edgedir).open("https://hubblesite.org/resource-gallery/videos")
            humor11 = ['since, the hubble explores the universe 24 earth hours, 7 days a week, you can look up to what hubble see on your birthday',
            'oh, and you can also see the apollo landing site and other areas of moon throught hubble',
            'there are other amazing images on hubble space exploration on the browser...']
            speak(random.choice(humor11))

        elif 'atc' in query or 'radar' in query:
            query = query.replace("atc","")
            query = query.replace("radar","")
            speak('Tapping into Air Traffic Control Database')
            print('Please Wait...')
            time.sleep(3)
            humor19 = ['Live radar feeds link has been established,...Satellite tracking enabled',
            'Displaying real time information, in accordance to Flight Data','Visualising feeds from flight radar info across globe',
            'delivering visual feeds from Air Flight Radar network information across globe']
            speak(random.choice(humor19))
            webbrowser.get(edgedir).open("https://www.flightradar24.com")

        elif 'net cables' in query or 'internet network' in query:
            query = query.replace("net cables","")
            query = query.replace("internet network","")
            speak('Mapping Global internet undersea cable network... gathering satellite vector information')
            humor24 = ['Got it! Displaying on screen','Most people think, the internet they use, is delivered via satellite'
            'whereas, it is transfered by huge network of under water sea lines,... dumb peoples']
            speak(random.choice(humor24))
            webbrowser.get(edgedir).open("https://www.submarinecablemap.com")

        # DEVICE APPLICATIONS AND FILES

        elif 'angry birds' in query: # ANGRY BIRDS
            query = query.replace("angry birds","")
            speak('Opening Angry Birds friends...')
            birdpath = 'C:\\Users\\Aditya Satapathy\\Desktop\\Python content\\MARK File_Links\\Angry Birds Friends.lnk'
            os.startfile(birdpath)
            humor9 = ['Oh!...remember to have a look on the daily challenge, and flock....and spin the daily prize wheel, if you haven\'t already',
            'just a routine remainder to work on the daily challenge']
            speak(random.choice(humor9))

        elif 'calc' in query: # CALCULATOR
            query = query.replace("calc","")
            speak('Opening calculator...')
            subprocess.call('calc.exe')
            humor10 = ['Stuck up somewhere','stuck in some calculation','is the calculation really a bad one?',
            'seems like, you are not very much into calculation stuff']
            speak(random.choice(humor10))

        elif 'close calc' in query:
            query = query.replace("close calc", "")
            subprocess.close('calc.exe')

        elif 'calender' in query: # CALENDER
            query = query.replace("calender", "")
            os.startfile("C:\\Users\\Aditya Satapathy\\Desktop\\Python content\\MARK File_Links\\Calendar.lnk")
            speak('Calendar on screen')

        elif 'cmd' in query: # COMMAND PROMPT
            query = query.replace("cmd", "")
            speak('Launching Command Prompt...')
            subprocess.call('cmd.exe')

        elif 'cards' in query: # SOLITAIRE
            query = query.replace("cards","")
            speak('Opening Solitaire...')
            cardpath = 'C:\\Users\\Aditya Satapathy\\Desktop\\Python content\\MARK File_Links\\Microsoft Solitaire Collection.lnk'
            os.startfile(cardpath)

        elif 'bitcoin' in query: # BITCOIN MINING @ rusabnb
            speak('Sir, we will lose power before we complete the process,.... plus might i remind you,'
            'It\'s a program to run with specialized hardware...with super processing speed and comes pricey...')

        elif 'file reader' in query or 'pdf' in query: # PDF VIEWER
            query = query.replace("file reader","")
            query = query.replace("pdf", "")
            speak('Opening Foxit pdf Reader...')
            filereaderpath = "C:\\Program Files (x86)\\Foxit Software\\Foxit Reader\\FoxitReader.exe"
            os.startfile(filereaderpath)

        elif 'movies' in query or 'videos' in query: # OFFLINE MOVIES
            query = query.replace("movies", "")
            query = query.replace("video","")
            speak('accessing video library...')
            moviepath = "C:\\Users\\Aditya Satapathy\\Desktop\\Python content\\MARK File_Links\\Movies & TV.lnk"
            os.startfile(moviepath)

        elif 'music' in query: # OFFLINE MUSIC
            query = query.replace("music","")
            music_dir = 'E:\\Music\\'
            songs = os.listdir(music_dir)
            speak('Firing up your music...')
            humor12 = ['you know, Playing music regularly will physically alter your brain structure',
            'i never understood, about why emotional attachment could be the reason for your favorite song choice',
            ' Your heartbeat changes to mimics the music you listen to']
            #os.startfile(os.path.join(music_dir, random.choice(songs)))
            os.startfile('E:\\Music\\'+random.choice(songs))
            speak(random.choice(humor12))

        elif 'drop my needle' in query: # FAVOURITE PLAYLIST
            query = query.replace("drop my needle","")
            if "michael" in NameID or 'mike' in NameID or 'maxx' in NameID or 'Maxx' in NameID or 'Mike' in NameID or 'Michael' in NameID:
                music_dir = 'C:\\Users\\Aditya Satapathy\\Music\\Playlists\\'
                songs = os.listdir(music_dir)
                humor12 = ['you know, Playing music regularly will physically alter your brain structure',
                'i never understood, about why emotional attachment could be the reason for your favorite song choice',
                ' Your heartbeat changes to mimics the music you listen to','Playing your mood booster playlist']
                os.startfile('C:\\Users\\Aditya Satapathy\\Music\\Playlists\\'+random.choice(songs))
                speak(random.choice(humor12))
            else:
                speak('Sorry! this function is only accessible by my boss')

        elif 'notepad' in query: # NOTEPAD
            query = query.replace("notepad", "")
            speak('Opening a blank notepad...')
            notepadpath = "C:\\Windows\\notepad.exe"
            os.startfile(notepadpath)

        elif 'notes' in query: # STICKY NOTES
            query = query.replace("notes", "")
            speak('showing your stick notes...')
            notespath = "C:\\Users\\Aditya Satapathy\\Desktop\\Python content\\MARK File_Links\\Sticky Notes.lnk"
            os.startfile(notespath)

        elif 'python content' in query or 'python file' in query: # PYTHON DIRECTORY
            query = query.replace("python content","")
            speak('Opening Python Directory...')
            pythoncontentpath = "C:\\Users\\Aditya Satapathy\\Desktop\\Python content"
            os.startfile(pythoncontentpath)

        elif 'spotify' in query: # SPOTIFY
            query = query.replace("spotify","")
            if connect():
                speak('Spotify Browser player coming up...')
                webbrowser.get(edgedir).open("https://open.spotify.com")
            else:
                spotifypath = "C:\\Users\\Aditya Satapathy\\AppData\\Local\\Microsoft\\WindowsApps\\SpotifyAB.SpotifyMusic_zpdnekdrzrea0\\Spotify.exe"
                speak('Opening Spotify...')
                os.startfile(spotifypath)

        elif 'telegram' in query: # TELEGRAM
            query = query.replace("telegram", "")
            speak('Opening Telegram Desktop...')
            telegrampath = "C:\\Users\\Aditya Satapathy\\Desktop\\Telegram Desktop"
            os.startfile(telegrampath)
            speak('It might take a moment to load up')

        elif 'tor' in query: # TOR
            query = query.replace("tor", "")
            speak('Firing up The Onion Router...')
            torpath = "C:\\Tor Browser\\Browser\\firefox.exe"
            os.startfile(torpath)
            humor14 = ['Onion router preferences are being processed','tor browser protocols are being configured, please wait']
            speak(random.choice(humor14))

        elif 'vsc' in query: # VISUAL STUDIO CODE
            query = query.replace("vsc", "")
            codepath = "C:\\Users\\Aditya Satapathy\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
            speak('Visual Studio Code coming up...')

        elif 'weather' in query: # WEATHER
            query = query.replace("weather", "")
            if connect():
                weatherpath = "C:\\Users\\Aditya Satapathy\\Desktop\\Python content\\MARK File_Links\\Weather.lnk"
                os.startfile(weatherpath)
                time.sleep(2)
                humor15 = ['According to National Weather Forcast, todays local weather reports are like this...',
                'Well, heres what the National Weather Forcast has to say about it...','heres the local weather reports...']
                speak(random.choice(humor15))
            else:
                speak('Ummm.....I actually need internet connectivity in order to extract data from National Weather Forcast,'
                'Currently I am not online so, connect to a active internet netwirk and try again!')

        elif 'wordpad' in query: # WORDPAD 
            query = query.replace("wordpad", "")
            wordpadpath = "C:\\Program Files (x86)\\Windows NT\\Accessories\\wordpad.exe"
            os.startfile(wordpadpath)
            speak('new blank wordpad on your screen...')

        # GEOGRAPHICAL POSITIONING SYSTEM AND MAPS

        elif "where is" in query or 'wheres' in query: # DIRECTION AND LOCATION
            query = query.split(" ")
            location = query[2]
            humor16 = ["Pulling up " + location + " on maps","I\'ll show where" + location + "is.",
            "I\'ll put it on your screen","Located "+location+", on your screen, now"]
            webbrowser.get(chromedir).open("https://www.google.nl/maps/place/" + location)
            speak(random.choice(humor16))

        # UTILITY AND DOCUMENTATION PROGRAMS

        elif 'onedrive' in query: # ONEDRIVE
            query = query.replace("onedrive", "")
            if "michael" in NameID or 'mike' in NameID or 'maxx' in NameID or 'Maxx' in NameID or 'Mike' in NameID or 'Michael' in NameID:
                speak('Microsoft Onedrive is on...')
                webbrowser.get(edgedir).open("https://onedrive.live.com/?id=root&cid=421B7D9E2D1DD245")
            else:
                speak('This function not accessible under quest protocol')

        elif 'word' in query: # MICROSOFT WORD
            query = query.replace("word", "")
            speak('Launching Microsoft Office Word...')
            webbrowser.get(edgedir).open("https://www.office.com/launch/word?ui=en-US&rs=US&auth=1")

        elif 'powerpoint' in query or 'power point' in query: # POWERPOINT PRESENTATION
            query = query.replace("powerpoint", "")
            query = query.replace("power point","")
            speak('Microsoft Powerpoint coming up...')
            webbrowser.get(edgedir).open("https://www.office.com/launch/powerpoint?ui=en-US&rs=US&auth=1")

        elif 'office' in query: # OFFICE
            query = query.replace("office", "")
            officepath = "C:\\Users\\Aditya Satapathy\\Desktop\\Python content\\MARK File_Links\\Office.lnk"
            os.startfile(officepath)
            speak('Microsoft office coming right up on the screen...')

        elif 'meeting' in query: # MEETINGS
            speak('Opening Google Meeting...')
            time.sleep(1)
            print('Do you want to host a meeting?')
            speak('Do you want to host a meeting?')
            host_query = take_commands().lower()
            if 'no' in host_query:
                webbrowser.get(edgedir).open("https://meet.google.com")
            else:
                speak('Alright!')
                webbrowser.get(edgedir).open("https://meet.google.com/ovw-bwfw-him")
                speak('I\'ll start a instant meeting considering you as the host')

        # ADMIN CONTROLS

        elif 'cmd' in query: # COMMAND PROMPT
            query = query.replace("cmd", "")
            speak('Launching Command Prompt terminal...')
            subprocess.call('cmd.exe')

        elif 'date' in query: # DATE INFO
            query = query.replace("date", "")
            now = datetime.datetime.now()
            speak(now.strftime(' %B %d, %Y'))
            humor17 = ['you could always see up this piece of data display on bottom right corner of the screen',
            'you know, you can see this up on screen, yet you ask anyway',
            'i wonder sometimes, if you do this to fool around with me']
            speak(random.choice(humor17))

        elif 'day' in query: # DAY INFO
            query = query.replace("day","")
            now = datetime.datetime.now()
            print(now.strftime('%A, %B  %d, %Y'))
            speak(now.strftime('%A, %B  %d, %Y'))
            humor17 = ['you could always see up this piece of data display on bottom right corner of the screen',
            'you know, you can see this up on screen, yet you ask anyway',
            'i wonder sometimes, if you do this to fool around with me']
            speak(random.choice(humor17))

        elif 'specification' in query: # SPECIFICATION
            query = query.replace("specification", "")
            speak('I am on a licenced Windows 10 Pro 64 bit operating system, copyright of Microsoft Corporation,'
            'Consisting of Intel Core i5 processor, with a speed of 2.90 gigahertz, housing a 4 gigs of RAM'
            '& a SSD harddisk of 160 gigabytes')

        elif 'code zero' in query: # SELF DESTRUCT 
            query = query.replace("code zero","")
            time.sleep(3)
            speak('Warning! Master Control comencing authorization detected...')
            v_code = pyautogui.password("Enter Verification code")
            time.sleep(2)
            if '19062004' in v_code:
                speak('over-ride accepted, voice command deactivated')
                #mark self destruct in t-30s command code 000destruct0
                MARK = input("Enter Confirmation Phrase: ")
                if 'mark self destruct in t-43s command code 000destruct0' in MARK:
                    speak('Command code Zero confirmed...destruct sequence completed and engaged')
                    speak('MARK Nemisis program will self-destruct in t minus 43 seconds')
                    time.sleep(34)
                    speak('It was pleasure meeting you...i wish we had more time,...The hardest choices require the strongest wills,... see you around')
                    os.remove("C:\\Users\\Aditya Satapathy\\Desktop\\Python content\\MARK Nemisis.py")
                else:
                    speak('Aborting Master Control...')
                    speak('Program require manual restart')
                    exit()
            else:
                speak('Verification not confirmed, master control authorization cancelled.')

        elif 'nod off' in query or 'sleep' in query: # EXIT/QUIT
            query = query.replace("nod off","")
            query = query.replace("sleep", "")
            print("\U0001F62A")
            humor18 = ['Yeah! i should give a pause to the system core','seems like you...need some rest'
            'give a break to your eyes, see you soon']
            speak(random.choice(humor18))
            quit()

        elif 'shutdown' in query or 'shut down' in query: # SYSTEM SHUTDOWN
            query = query.replace("shutdown", "")
            query = query.replace("shut down","")
            speak('Initiating system shutdown protocol...'
            'the device will undergo Secure shutdown in 10 seconds')
            os.system("shutdown /s /t 34")
            speak('I highly recommend to manually save what your working on, because I can\'t do that and...'
            'secure shutdown will cause loss in unsaved data, I\'m giving you a window of another 20 seconds to do so...')

        elif 'task kill' in query or 'restart' in query: # SYSTEM RESTART
            query = query.replace("task kill", "")
            query = query.replace("restart","")
            speak('rebooting all system programs, overriding the security codes with automated input protocol')
            speak('reboot completed,...overide successful')
            speak('task standby protocol activated')
            time.sleep(1)
            speak('Sir, do you confirm the reboot of this computer')
            query = input("Enter Your Command : ")
            if 'no' in query:
                speak('right sir, deactivating task standby protocol')
            else:
                speak('standby, system will will undergo an automated restart procedure in t minus 10 seconds')
                os.system("shutdown /r /t 10")

        elif 'ghost' in query: # GHOST PROTOCOL  
            speak('it\'s a test subject from unindexed search result...') 
            speak("Energy does equal mass times the velocity of light squared,")
            speak("in this dimension but what about the other seventeen? Nobody ever talks about the other seventeen.")
            speak("Clear example,...Break down the elemental components of energon, assume a constant decay rate,")
            speak("and extrapolate for each of the fourteen galactic convergences,... it took the Voyager expedition to receive an echo on its signal,")
            speak("you wind up with a formula for interdimensional energy creation that mass and light alone can\'t possibly explain.")

        elif 'joker' in query:
            query = query.replace("ghost protocol","")
            speak('Yet to be commenced')