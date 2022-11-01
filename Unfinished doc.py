import pyttsx3 #pip install pyttsx3

#methord to analize the input
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)

#commanding engine
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


speak("Welcome to Universal Forces Insight Page ")
print("Welcome to Universal Forces Insight Page ")
speak("Enter your code name ")
Name = str(input("Enter your code name = "))
print("Welcome",Name)
password = str(input("Enter your login password = "))
print("Authenticating login sequence...")
if password == 'cosmorationdisoveride' :
  print("password verified")
  speak("password verified")
else:
  print("Access Denied")
  speak("Access Denied")
  quit()
print(hash ('password'))
print("Login Accepted. Access Granted")
speak("Login Accepted. Access Granted")
while True:
  
  z = str(input("Enter command = "))
  speak("Enter command")
  if "current status of the operation" in z:
    z = z.replace("current status of the operation","")
    print("Operation 101:Ghost Protocol is a 8-years project undertaken by Universal Forces and United Nations."
        "This operation gathers information both from the UF Agents and satellite based imaging and pattens created by hi-speed computers, of both the population of homo-sapians and paranormal and unexplained activities around the world .")
    print("Operation 101:Ghost Protocol is at its Second-year of functioning and till now had targeted around 1000 minor target and some major targets around the world out of which some are hunted by govt."
        "of some powerful countries of the world and even Interpol."
        "The major target list contains names of the identities who posses serious threat to mankind with malicious plans")
    speak("Operation 101:Ghost Protocol is a 8-years project undertaken by Universal Forces and United Nations."
        "This operation gathers information both from the UF Agents and satellite based imaging and pattens created by hi-speed computers, of both the population of homo-sapians and paranormal and unexplained activities around the world .")
    speak("Operation 101:Ghost Protocol is at its Second-year of functioning and till now had targeted around 1000 minor target and some major targets around the world out of which some are hunted by govt."
        "of some powerful countries of the world and even Interpol."
        "The major target list contains names of the identities who posses serious threat to mankind with malicious plans")
  elif z == "insight algorithm":
    print("The twenty-first century is a technological book. Universal Forces taught the world how to read it."
              "Your bank records, medical histories, voting patterns, e-mails, phone calls, your SAT scores... Insight Algorithm evaluates people's past and analyse their present to predict future.")
    print("Insight Algorithm was a program written by Henry Larenson to identify targets by analysing people's data available online, including private data, to predict whether they currently posed a threat for the organization."
              "It was used in the framework of Operation 101:Ghost protocol.") 
  elif z == "capabilities of ghost protocol":
    print("Insight Algorithm was designed to review large amounts of personal information and to process it in a very short time in order to access whether an individual was a potential threat to Universal Forces or satisfy the target list."
              "The algorithm analyzed data from various subjects: financial records, medical histories, voting patterns, phone conversations as well as all electronic messages.")
  elif z == "how does operation 101:ghost protocol works":
    print("Universal Forces engineered special aircrafts combinedly called '101 Air force' to initiate the attack sequence of Insight Algorithm."
              "This air force include specially designed helicarriers named 4LTD, DCM, GLITE, Blues; that can reach upto an alltitude of 34,000 feet."
              "When deployed by the 101 Air Force helicarriers, Insight Algorithm would lock approx 70,000 targets at a time, making it the most powerful and versatile weapon in todays date.")
  elif z == 'what is mission report 9':
    print("Mission Report 9 is a level 7 classified file.")
    print("Please enter access password")
    password = str(input("Enter access password = "))
    if password == "cosmorationdisoveride":
      print("Access granted")
      print("Mission Report 9 is a classified operation undertaken by UF in the year 1955. At that time it was known by the name-'Joint Peace Alliance'."
                "It is the only Mission Report that contains only investigation operation of the main target of Operation 101:Ghost Protocol."
                "In 1955, satellites picked up images of the Northern region of Siberia, on 13 March, Friday around 1900 hrs."
                "Russian Joint Peace Alliance sent top rank commands and highly trained soilders to investigate the scene."
                "At around 2010 hrs the last transmission came from the soilders saying'Too much casulaties had took place. No sign of movement or human activity. Hold on... we see a shadow in the raining snow." 
                "The mercyless and awful scene can be the result of his.....'. The transmission ended mysteriously without describing what exactly happned there."
                "At around 2030hrs, when the satellite came over the location the images were horrible.")
      print("Analysis of the mission revealed about a person with super-soilder strength, and .")
    else:
      print("Access Denied")
  elif z == 'What 101 Air Force':
    print("101 Air Force is a group of next generation flight vehicles used by the Universal Forces personally. These contain 4 advance Helicarriers designed"
            "by Airbus and equipped with advance technology of UF. These helicarriers can reach upto an alltitude of 40,000ft and is impossible to target these"
            "aircraft by any means of weapon available on ground. These helicarriers are not the only member of 101 Air Force, they are accompanied by a few other"
            "types of aircraft that are only one of their kind. They are named as SoundWave, BattleShip, 5-F22 Raptors, and helicarrier Sandisk.")
  elif z == 'what is ghost protocol':
    print("Operation 101:Ghost protocol was an mission initiated by Universal Forces current director in the")
    ("year 1996 to takedown the German NAZI science research branch HYDRA. This operation was led by two of the")
    ("best soilders of UF, Sergent Paul Jackson and Captain Soap McTavish. The aim of the operation was to ")
    ("takedown hydra and put it out of existance. Their leader 'Arnim Zola', a great scientist and genius of the")
    ("era made a crucial plan to takedown the operation undertaken by UF. He drew his plans against the motion ")
    ("of Operation 101: Ghost Protocol and fail it. Zola's algorithms were so perfectly designed that it failed")
    ("the functional of Operation 101:Ghost Protocol.")
  elif z == 'the new ghost protocol':
    print("The new Operation 101:Ghost Protocol was launched in 2015. This operation undertaken by UF ensures ")
    print("the fall of HYDRA within 8 years of it's initiation. Operation 101:Ghost Protocol was re-intiated")
    print("by Special Task Force(STF) agent Michael Maxx. He was the operation leader in redesign of Ghost Protocol.")
    print("He along with highly specialized software programming engineers designed the protocol is a way that")
    print("HYDRA leader wouldn't try to penetrate the security. If he tries to do so he wound end up currpting")
    print("his own computer software due to the pre-installed high damage virus.")
  elif z == 'what is shield':
    print("SHIELD stands for Supreme Headquaters of International Espionage and Law-enforcement Division.")
    print("")
  else:
    print("Command request didn't match")
