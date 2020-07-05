import os
import playsound
import time
from gtts import gTTS
import random
import speech_recognition as sr
from tkinter import *
import datetime
import webbrowser

date = datetime.datetime.now()



saved_f = list(range(1,1000))
rand = random.choice(saved_f)
ran1 = random.choice(saved_f)



openApp = ["Just a minute","Ok I'll open it","As you say Gaurav"]
greet = ['Whatsup','Yo','I am good']

def say(text):
    tts = gTTS(text=text,lang='en')
    filename = f"{rand}.mp3"
    tts.save(filename)
    playsound.playsound(filename)


def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio_data = r.listen(source,timeout=5,phrase_time_limit=5)
        said = ""
        try:
            
            said = r.recognize_google(audio_data)
            print(said)
        except Exception as e:
            print("Error:-"+str(e))
    return said.lower()

def make_note():
    say("Yes What do you want to write")
    text1 = get_audio()
    file=open(f"{ran1}.txt",'w')
    file.write(text1)
    file.write(f"       (Time of writing:{date})")
    file.close()
    
    
def google_search():
    say("What do you want to search")
    search = str(get_audio())
    que = "https://google.com/?#q="
    webbrowser.open(que+search,new=2)
    os.remove(f"{rand}.mp3")
def main_function():
    
    text = get_audio()
    if 'name' in text:
        say("Hi Gaurav, I am your assistant Friday")
        
    elif 'steam' in text:
        say(random.choice(openApp))
        os.system('E:\Steam\Steam.exe') 
        
    elif 'whatsapp' in text:
        say(random.choice(openApp))
        os.system('Whatsapp.exe')
    
    elif 'date' in text:
        say("Today is "+str(date)[0:10])
    
    
    elif 'make note' in text:
        make_note()
        
    elif 'Hi' or 'how are you' or 'kya haal chaal' in text:
        say(random.choice(greet))
    
        
        
    os.remove(f"{rand}.mp3")

def play_song():
    hindi_songs = ['https://www.youtube.com/watch?v=tUi01BXRwdo','https://www.youtube.com/watch?v=yUu26tcUri0','https://www.youtube.com/watch?v=YSWMbwQuWAY','https://www.youtube.com/watch?v=zNUs54J3mKo']
    eng_songs = ['https://www.youtube.com/watch?v=jzD_yyEcp0M','https://www.youtube.com/watch?v=m7Bc3pLyij0','https://www.youtube.com/watch?v=FM7MFYoylVs','https://www.youtube.com/watch?v=fLexgOxsZu0']
    tot_song = hindi_songs+eng_songs
    
    so = str(get_audio())
    say('ok playing your song')
    if 'hindi song' in so:
        webbrowser.open(random.choice(hindi_songs))
    elif 'english song' in so:
        webbrowser.open(random.choice(eng_songs))
    else:
        webbrowser.open(tot_song)
    os.remove(f"{rand}.mp3")

root=Tk()
root.title("")
root.geometry("250x250")
root.resizable(0,0)


assistant_btn = Button(root,text="Ask Friday",command=main_function)
assistant_btn.grid(columnspan=2)

search_btn = Button(root,text="Search Google",command=google_search)
search_btn.grid(row=1,columnspan=2)

play_songs = Button(root,text="Play Songs",command=play_song).grid(row=2,columnspan=2)

root.mainloop()
    



