from gtts import gTTS
import os
text = """ Sir, I have complied a report of your friend search query, named Avisikta Sena. I learned that this friend of yours did recieve education from BDMI.Your friend also mentions you as stupid and me a "shitty typer". """
file = gTTS(text=text, lang='en', slow=False )
file.save('text_to_mp3.mp3')
os.system('start text_to_mp3.mp3')