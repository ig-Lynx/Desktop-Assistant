import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random
import pywhatkit as kit
import sys
import pyautogui
import time
import requests
import customtkinter as ctk
import threading
import tkinter as tk
from PIL import Image, ImageTk

# Initialize text-to-speech engine with exception handling
try:
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[0].id)
    engine.setProperty("rate", 150)
except Exception as e:
    print(f"Error initializing text-to-speech engine: {e}")
    sys.exit(1)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("Ready To Comply. What can I do for you?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query       

import subprocess

# Other imports and functions remain unchanged

def play_music_on_spotify(song_name):
    webbrowser.open(f"https://open.spotify.com/search/{song_name}")

def play_music_on_apple_music(song_name):
    webbrowser.open(f"https://music.apple.com/search?term={song_name}")

def process_query(query):
    if "wikipedia" in query:
        speak("Searching Wikipedia...")
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        print(results)
        speak(results)

    elif "channel analytics" in query:
        webbrowser.open("") #your channel statistics link

    elif "search on youtube" in query:
        query = query.replace("search on youtube", "")
        webbrowser.open(f"www.youtube.com/results?search_query={query}")

    elif "open youtube" in query:
        speak("What would you like to watch?")
        qrry = takeCommand().lower()
        kit.playonyt(f"{qrry}")

    elif "who are you" in query:
        print("My Name Is Echo")
        speak("My Name Is Echo")
        print("I can Do Everything that my creator programmed me to do")
        speak("I can Do Everything that my creator programmed me to do")

    elif "who created you" in query:
        print("I Do not Know His Name, I was created with Python Language, in Visual Studio Code.")
        speak("I Do not Know His Name, I was created with Python Language, in Visual Studio Code.")

    elif "type" in query:
        query = query.replace("type", "")
        pyautogui.write(f"{query}")

    elif 'open google' in query:
        speak("What should I search for?")
        qry = takeCommand().lower()
        webbrowser.open(f"{qry}")
        results = wikipedia.summary(qry, sentences=2)
        speak(results)

    elif 'close google' in query:
        os.system("taskkill /f /im msedge.exe")

    elif 'play music' in query:
        speak("Do you want to play music on Spotify or Apple Music?")
        service = takeCommand().lower()
        if "spotify" in service:
            speak("What song would you like to play?")
            song_name = takeCommand().lower()
            play_music_on_spotify(song_name)
        elif "apple music" in service:
            speak("What song would you like to play?")
            song_name = takeCommand().lower()
            play_music_on_apple_music(song_name)
        else:
            speak("I didn't understand the music service. Please say Spotify or Apple Music.")

    elif 'play video' in query:
        npath = r"" # add your local path to the mp4 file
        os.startfile(npath)

    elif 'close movie' in query:
            os.system("taskkill /f /im vlc.exe")

    elif 'close music' in query:
            os.system("taskkill /f /im vlc.exe")

    elif 'the time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"Sir, the time is {strTime}")

    elif "shut down the system" in query:
        os.system("shutdown /s /t 5")

    elif "restart the system" in query:
        os.system("shutdown /r /t 5")

    elif "lock the system" in query:
        os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

    elif "open command prompt" in query:
        os.system("start cmd")

    elif "close command prompt" in query:
        os.system("taskkill /f /im cmd.exe")

    elif "go to sleep" in query:
        speak('Alright then, I am switching off')
        sys.exit()

    elif "take screenshot" in query:
        # here the screenshot is being saved in the current working directory itself
        speak('Tell me a name for the file')
        name = takeCommand().lower()
        time.sleep(3)
        img = pyautogui.screenshot()
        img.save(f"{name}.png")
        speak("Screenshot saved")

    elif "what is my ip address" in query:
        speak("Checking")
        try:
            ipAdd = requests.get('https://api.ipify.org').text
            print(ipAdd)
            speak("Your IP address is")
            speak(ipAdd)
        except Exception as e:
            speak("Network is weak, please try again sometime later")

    elif "volume up" in query:
        pyautogui.press("volumeup", presses=2)

    elif "volume down" in query:
        pyautogui.press("volumedown", presses=2)

    elif "refresh" in query:
        pyautogui.moveTo(1551, 551, 2)
        pyautogui.click(x=1551, y=551, clicks=1, interval=0, button='right')
        pyautogui.moveTo(1620, 667, 1)
        pyautogui.click(x=1620, y=667, clicks=1, interval=0, button='left')

    elif "scroll down" in query:
        pyautogui.scroll(1000)

    elif "drag visual studio to the right" in query:
        pyautogui.moveTo(16, 31, duration=2)
        pyautogui.dragRel(1857, 31, duration=2)

    elif "open notepad" in query:
        pyautogui.hotkey('win')
        time.sleep(1)
        pyautogui.write('notepad')
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(1)
        pyautogui.write("BMS Institute", interval=0.1)

    elif "close notepad" in query:
        os.system("taskkill /f /im notepad.exe")

def listen_loop():
    while True:
        query = takeCommand().lower()
        if query != "none":
            process_query(query)

def start_assistant():
    wishMe()
    listen_loop()

def start_assistant_thread():
    thread = threading.Thread(target=start_assistant)
    thread.start()

# GUI setup with customtkinter
def gui_start():
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    root = ctk.CTk()
    root.title("Voice Assistant")
    root.geometry("400x600")

    frame = ctk.CTkFrame(master=root)
    frame.pack(pady=20, padx=20, fill="both", expand=True)

    label = ctk.CTkLabel(master=frame, text="Voice Assistant", font=("Arial", 24))
    label.pack(pady=20)

    start_button = ctk.CTkButton(master=frame, text="Start Assistant", command=start_assistant_thread, font=("Arial", 18))
    start_button.pack(pady=20)

    exit_button = ctk.CTkButton(master=frame, text="Exit", command=root.quit, font=("Arial", 18))
    exit_button.pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    gui_start()



