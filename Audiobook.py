import pyttsx3
import PyPDF2
from tkinter.filedialog import *

audio = pyttsx3.init()
rate = audio.getProperty('rate')
audio.setProperty('rate',185)

book = askopenfilename()
reader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPage
audio.say("hello! the selected file contains" + str(pages) +"pages")
print("Total no of pages: "+str(pages))

audio.say("Now is there any particular pages you want me to read out or should i start from beginning"
"going throught and reading out all the pages")
pagequery = input("Beginning / All Pages / Particular page no. =>")
query = pagequery.lower()
if 'beginning' in query:
    query = query.replace("beginning","")
    text = pages.extractText()
    audio.say(text)
    audio.runAndWait()
elif 'all' in query:
    query = query.replace("all","")
