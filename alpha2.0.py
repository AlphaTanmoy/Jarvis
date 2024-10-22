import speech_recognition as sr  # recognise speech
import playsound  # to play an audio file
from gtts import gTTS  # google text to speech
import random
import time
from time import ctime  # get time details
import webbrowser  # open browser
import yfinance as yf  # to fetch financial data
import ssl
import certifi
import time
import os  # to remove created audio files
import subprocess
from os import sys
import wikipedia
from pynput.mouse import Button, Controller
from pynput import keyboard
import numpy

browser = "chrome.exe"


#declearation of mouse and keyboard
mouse = Controller()
key = keyboard.Controller()


class person:
    name = ''

    def setName(self, name):
        self.name = name

def there_exists(terms):
    for term in terms:
        if term in voice_data:
            return True



r = sr.Recognizer()  # initialise a recogniser
# listen for audio and convert it to text:


def record_audio(ask=False):
    with sr.Microphone() as source:  # microphone as source
        if ask:
            speak(ask)
        audio = r.listen(source)  # listen for the audio via source
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)  # convert audio to text
        except sr.UnknownValueError:  # error: recognizer does not understand
            speak('what should i do')
        except sr.RequestError:
            # error: recognizer is not connected
            speak('Sorry, the service is down')
        print(f">> {voice_data.lower()}")  # print what user said
        return voice_data.lower()

# get string and make a audio file to be played

def speak(audio_string):
    tts = gTTS(text=audio_string, lang='en')  # text to speech(voice)
    r = random.randint(1, 20000000)
    audio_file = 'audio' + str(r) + '.mp3'
    tts.save(audio_file)  # save as mp3
    playsound.playsound(audio_file)  # play the audio file
    print(f"Alpha: {audio_string}")  # print what app said
    os.remove(audio_file)  # remove audio file



def respond(voice_data):

#manners
    if there_exists(["wait for","weight for"]):
        search_term = voice_data.split("for")[-1]
        speak(f'Ok sir i will not interuppting you for {search_term} minuits')
        time.sleep(int(search_term)*60)
        speak(f'Sir, are u free now?')
    
    if there_exists(["no"]) and (["more"]):
        search_term = voice_data.split("more")[-1]
        speak(f'Ok sir i will not interuppting you for {search_term} minuits')
        time.sleep(int(search_term)*60)
        speak(f'Sir, are u free now?')
    
    if there_exists(["yes"]) and (["am"]) and (["i"]) and (["free"]):
        speak(f'ok sir, always at your service')


    # introoooooooooooooo.................................................????????>>>>>>>>>>>>>>>>>>>>>
    # 0: Introduction
    if there_exists(["alpha"]):
        speak("Yes Sir, i'm your personal P.C Assistent!. Alpha....... . Checking for System Being online...... . All set!.... Good to go sir!....")

    # 0: vertion
    if there_exists(["vertion", "version"]):
        speak("currently i'm Alpha 2.0. Later vertions are Alpha! Alpha 1.0! Alpha 1.1.0! Alpha 1.2!")

    # 0: vertion
    if there_exists(["introduction", "intro"]):
        speak("currently i'm Alpha 2.0. Later vertions are Alpha! work as a chat bot! Alpha 1.0! modified youtube search. Alpha 1.1.0! modified google search. Alpha 1.2!modified tiem and os capability")

    # 1: greeting
    if there_exists(['hey', 'hay', 'hi', 'hello']):
        greetings = [f"hey, how can I help you {person_obj.name}", f"hey, what's up? {person_obj.name}",
                     f"I'm listening {person_obj.name}", f"how can I help you? {person_obj.name}", f"hello {person_obj.name}"]
        greet = greetings[random.randint(0, len(greetings)-1)]
        speak(greet)

    # 2: name
    if there_exists(["what is your name", "what's your name", "tell me your name", "Who are you"]):
        if person_obj.name:
            speak("my name is Alpha. Version 2.OO !")
        else:
            speak("my name is Alpha.")

    if there_exists(["my name is"]):
        person_name = voice_data.split("is")[-1].strip()
        speak(f"okay, i will remember that {person_name}")
        person_obj.setName(person_name)  # remember name in person object

    if there_exists(["whta is my name"]):
        person_name = voice_data.split("is")[-1].strip()
        speak(f"Sir, your name is {person_name}")
        person_obj.setName(person_name)

    # 3: greeting
    if there_exists(["how are you", "how are you doing"]):
        speak(f"I'm very well, thanks for asking {person_obj.name}")

    # introoooooooooooooo.................................................????????>>>>>>>>>>>>>>>>>>>>>

    # 4: time
    if there_exists(["what's the time", "tell me the time", "what time is it"]):
        time1 = ctime().split(" ")[3].split(":")[0:2]
        if time1[0] == "00":
            hours = '12'
        else:
            hours = time1[0]
        minutes = time1[1]
        time1 = f'{hours} {minutes}'
        speak(time1)

    # 5: search google
    if there_exists(["search for"]) and 'youtube' not in voice_data:
        search_term = voice_data.split("for")[-1]
        url = f"https://google.com/search?q={search_term}"
        webbrowser.get().open_new_tab(url)
        speak(f'Here is what I found for {search_term} on google')

    # 6.1: search youtube
    if there_exists(["play my song"]):
        webbrowser.get().open_new_tab(
            "https://www.youtube.com/watch?v=mRvKlUcD8vs&list=RDmRvKlUcD8vs&start_radio=1")
        speak(f'Playing songs from youtube!')

    # 6.2: Open Facebook
    if there_exists(["open facebook"]):
        webbrowser.get().open_new_tab("https://www.facebook.com/")
        speak(f'Opened FaceBook for you Sir')

    # 6.2: Open WhatsAPP
    if there_exists(["open whatsapp"]):
        webbrowser.get().open_new_tab("https://web.whatsapp.com/")
        speak(f'Opened WhatsApp for you Sir')

    # 6.3: Open Gmail
    if there_exists(["open my gmail"]):
        webbrowser.get().open_new_tab("https://mail.google.com/mail/u/0/#inbox")
        speak(f'Opened Your Gmail for you Sir')

    # 6.3: Open Dad Gmail
    if there_exists(["open dad gmail"]):
        webbrowser.get().open_new_tab("https://mail.google.com/mail/u/1/#inbox")
        speak(f'Opened Dads Gmail for you Sir')

    # 6.3: Open Javatpoint
    if there_exists(["open java t point"]):
        webbrowser.get().open_new_tab("https://www.javatpoint.com/")
        speak(f'Opened javatpoint for you Sir')

    # 6.3: Open Dad Gmail
    if there_exists(["open tutorialspoint"]):
        webbrowser.get().open_new_tab("https://www.tutorialspoint.com/index.htm")
        speak(f'Opened tutorialspoint for you Sir')

    # 6.3: Open greeksforgreeks Gmail
    if there_exists(["open greeks for greeks", "open greeksforgreeks", "open greekforgreek", "greekforgreeks"]):
        webbrowser.get().open_new_tab("https://www.geeksforgeeks.org/")
        speak(f'Opened geeksforgeeks for you Sir')

    # 7: search wikipedia
    if there_exists(["wikipedia for"]):
        search_term = voice_data.split("for")[-1]
        url = f"https://en.wikipedia.org/wiki/{search_term}"
        webbrowser.get().open_new_tab(url)
        speak(wikipedia.summary(search_term, sentences=2))

    # 8 Controlling Youtube........................................................................?>>>>>>>>>>>>>>>>>>>>>>>>>

    # 6: search youtube
    if there_exists(["open youtube for"]):
        search_term = voice_data.split("for")[-1]
        url = f"https://www.youtube.com/results?search_query={search_term}"
        webbrowser.get().open_new_tab(url)
        speak(f'Here is what I found for {search_term} on youtube')

    # 8.1 Youtube next video
    if there_exists(["next video"]):
        mouse.position = (202, 883)
        mouse.click(Button.left, 1)
        speak(f'Skip to Next Video, sir ')

    # 8.2 Youtube previous video
    if there_exists(["previous video"]):
        mouse.position = (132, 883)
        time.sleep(1)
        mouse.click(Button.left, 1)
        time.sleep(1)
        mouse.click(Button.left, 1)
        speak(f'Skip to Previous Video, sir ')

    # 8.2 Youtube previous video
    if there_exists(["skip add", "skip adds", "keep ad"]):
        mouse.position = (1315, 808)
        mouse.click(Button.left, 1)
        speak(f'Add skipped, sir')

    # 8.3 Youtube pouse
    if there_exists(["pose video", "pause video"]):
        mouse.position = (164, 883)
        mouse.click(Button.left, 1)
        speak(f'Pouse Video, sir ')

    # 8.4 Youtube play video
    if there_exists(["play video"]):
        mouse.position = (164, 883)
        mouse.click(Button.left, 1)
        speak(f'Playing Video, sir ')

    # 8.5 Youtube mute
    if there_exists(["mute video"]):
        mouse.position = (243, 885)
        mouse.click(Button.left, 1)
        speak(f'Mute Video sound, sir ')

    # 8.6 Youtube unmute
    if there_exists(["sound on"]):
        mouse.position = (243, 885)
        mouse.click(Button.left, 1)
        speak(f'un Mute Video sound, sir ')

    # 8.7 Fullscreen
    if there_exists(["full screen"]):
        mouse.position = (964, 586)
        mouse.click(Button.left, 2)
        speak(f'Move to Full Screen Display')

    # 8.7 Normallscreen
    if there_exists(["normal screen"]):
        mouse.position = (964, 586)
        mouse.click(Button.left, 2)
        speak(f'Move to Normal Screen Display')

    # 8.8 Open youtube Menu
    if there_exists(["youtube menu"]):
        mouse.position = (28, 125)
        mouse.click(Button.left, 1)
        speak(f'Youtube menu open for you sir')

    # 8.9 Open youtube Trending
    if there_exists(["youtube trending"]):
        mouse.position = (77, 227)
        mouse.click(Button.left, 1)
        speak(f'Youtube Trending section open for you sir')

    # 8.9 Open youtube Home
    if there_exists(["youtube home"]):
        mouse.position = (71, 201)
        mouse.click(Button.left, 1)
        speak(f'Youtube Home section open for you sir')

    # 8.9 Open youtube History
    if there_exists(["youtube history"]):
        mouse.position = (91, 377)
        mouse.click(Button.left, 1)
        speak(f'Youtube History section open for you sir')

    # 8.10 select something from search lists
    if there_exists(["show 1st one","show first one"]):
        time.sleep(1)
        mouse.position = (565, 291)
        mouse.click(Button.left, 1)
        speak(f'Showing 1st result')
    
    if there_exists(["show 2nd one","show second one"]):
        time.sleep(1)
        mouse.position = (522, 437)
        mouse.click(Button.left, 1)
        speak(f'Showing 2nd result')
    
    if there_exists(["show 3rd one","show third one"]):
        time.sleep(1)
        mouse.position = (567, 574)
        mouse.click(Button.left, 1)
        speak(f'Showing 3rd result')

    if there_exists(["show forth one","show fourth one"]):
        time.sleep(1)
        mouse.position = (586, 769)
        mouse.click(Button.left, 1)
        speak(f'Showing 4th result')

    if there_exists(["show fifth one","show fifth one"]):
        time.sleep(1)
        mouse.position = (541, 923)
        mouse.click(Button.left, 1)
        speak(f'Showing 5th result')

    if there_exists(["youtube search bar","youtube touch bar"]):
        mouse.position = (638, 130)
        time.sleep(1)
        mouse.click(Button.left, 1)


    # 8 Controlling Youtube........................................................................?>>>>>>>>>>>>>>>>>>>>>>>>>


    # 9 VPN on off...............................................................................>>>>>>>>>>>>>>>>>>>>>
    # on vpn
    if there_exists(["on vpn"]):
        mouse.position = (344, 820)
        mouse.click(Button.left, 2)
        mouse.position = (1166, 627)
        time.sleep(2)
        mouse.click(Button.left, 1)
        time.sleep(5)
        mouse.position = (1456, 422)
        mouse.click(Button.left, 1)
        speak(f'turned on Hotspot Shield VPN for you sir')

    # off vpn
    if there_exists(["off vpn"]):
        mouse.position = (344, 820)
        mouse.click(Button.left, 2)
        time.sleep(1)
        mouse.position = (1172, 908)
        mouse.click(Button.left, 1)
        time.sleep(3)
        mouse.position = (1456, 422)
        mouse.click(Button.left, 1)
        speak(f'turned off Hotspot Shield VPN for you sir')

    # 9 VPN on off...............................................................................>>>>>>>>>>>>>>>>>>>>>

    # 10 Switching tabs...............................................................>>>>>>>>>>>>>>>>>>>>>
    if there_exists(["page 1", "page one"]):
        mouse.position = (166, 5)
        mouse.click(Button.left, 1)
        mouse.click(Button.left, 1)
        speak(f'switch to tab 1')

    if there_exists(["page 2", "page to"]):
        mouse.position = (388, 5)
        mouse.click(Button.left, 1)
        mouse.click(Button.left, 1)
        speak(f'switch to tab 2')

    if there_exists(["page 3", "page three"]):
        mouse.position = (606, 5)
        mouse.click(Button.left, 1)
        mouse.click(Button.left, 1)
        speak(f'switch to tab 3')

    if there_exists(["page 4", "page four"]):
        mouse.position = (847, 5)
        mouse.click(Button.left, 1)
        mouse.click(Button.left, 1)
        speak(f'switch to tab 4')

    if there_exists(["page 5", "page five"]):
        mouse.position = (1075, 5)
        mouse.click(Button.left, 1)
        mouse.click(Button.left, 1)
        speak(f'switch to tab 5')

    if there_exists(["page 6", "page six", "page pic"]):
        mouse.position = (1317, 5)
        mouse.click(Button.left, 1)
        mouse.click(Button.left, 1)
        speak(f'switch to tab 6')

    if there_exists(["page 7", "page seven", "page saven", "page sevan", ]):
        mouse.position = (1511, 5)
        mouse.click(Button.left, 1)
        mouse.click(Button.left, 1)
        speak(f'switch to tab 7')

    # 10 Switching tabs...............................................................>>>>>>>>>>>>>>>>>>>>>

    # 11 Minimize
    if there_exists(["minimize", "minimise"]):
        mouse.position = (1800, 14)
        mouse.click(Button.left, 1)
        mouse.click(Button.left, 1)
        speak(f'minimized displaying window')

    # 12 Scorling
    if there_exists(["scroll down","roll down","troll down"]) and "present page" not in voice_data:
        mouse.position = (1915, 1030)
        time.sleep(1)
        mouse.click(Button.left, 4)

    if there_exists(["scroll down present page","roll down preasent page","troll down preasent page"]):
        mouse.position = (1915, 1030)
        time.sleep(1)
        mouse.click(Button.left, 20)
    
    if there_exists(["scroll up","troll up","roll up"]) and "present page" not in voice_data:
        mouse.position = (1908, 113)
        time.sleep(1)
        mouse.click(Button.left, 4)
    
    if there_exists(["scroll up present page","troll up preasent page","roll up preasent page"]):
        mouse.position = (1908, 113)
        time.sleep(1)
        mouse.click(Button.left, 20)
    

    # 13 Typping
    if there_exists(["type"]):
        search_term = voice_data.split("type")[-1]
        #keyboard.Controller.write(search_term)
        while there_exists(["ok"]):
            mouse.position = (1221, 128)
            time.sleep(1)
            mouse.click(Button.left, 1)
            break
        



    if there_exists(["exit", "quit", "shutdown"]):
        speak("going offline........ ")
        exit()


time.sleep(3)

person_obj = person()


speak("Hello Tanmoy. Alpha....... . Checking for System Being online...... . All set!.... Good to go sir!....")
while(1):
    voice_data = record_audio()  # get the voice input
    respond(voice_data)  # respond
