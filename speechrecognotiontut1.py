import pyttsx3
import speech_recognition as sr
import datetime
import os
import random
import webbrowser
import wikipedia
import pyjokes
import subprocess
import time
import pyautogui
import psutil
import winshell
import socket
import winshell
import sys
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice' , voices[1].1d)
from camera import* 
import imdb
from GoogleNews import GoogleNews
import pandas as pd
import string
from random import radint

def speak(audio)
     engine.say(audio)
     print(audio)
     engine.runAndWait()
     
def takeCommand():
     r=sr.Recognizer()
     with sr.Microphone() as source :
         print("Listening ......")
         r.pause_threshold=1
         audio=r.listen(source, timeout=1,phrase_time_limit=10)
     try:
             print("Recognizing....")
             query=r.recognize_google(audio,language='en-in')
             print(f"You said {query}\n")
     except Exception as e :    
             speak(f"Unableto recognize yoour voice......")
     return"None"
return query 
def username():
    speak("What shoudi call yoou sir")
    uname=takeCommand()
    speak("Welcome Mister"+uname) 
    speak("How cani help you Sir ?")

def movie ():
     moviesdb = imdb.IMDb()
     speak("Please tell me the movie name sir")
     text = takeCommand()
     movies = moviesdb.search_movie(text)
     speak("Searching for " + text )
     if len(movies==0)
         speak("No results found")
     else:
         speak("I found these :")
         for movie in movies :
              title = movie["titlle"]
              year = movie["year"]
              speak(f'{title}-{year}')
              info = movie.getID()
              movie = moviesdb.get_movie(info)
              rating = movie["rating"]
              plot = movie['plot outline']
              if year<int(datetime.datetime.now().strftime("%Y")):
                   speak(f'{title} was released in {year} has IMDB ratings oof {rating} . The plot summary of movie is {plot} ')
                   break
              else:
                   speak(f'{title} will be released in {year} has IMDB ratings oof {rating} . The plot summary of movie is {plot} ')
                   break
              


def wishMe():
     hour=int(datetime.datetime.now().hour())
     if hour>=0 and hour<12:
          speak("Good Morning Sir")
     else hour>=12 and hour<18 :
          speak("Good Afternood Sir ")
     speak("I am your virtual assistant jarvis .")
     
def rock():
     you = int(input("Please enter your choice :- \n 1-Rock \n 2-Paper \n 3-Scissor"))
     shapes = {1:'rock', 2:'paper', 3:'siscors'}
     if you not in shapes :
          print("Please enter a valid number ")
          exit()
     comp = random.randint(1,3)
     print("You choose", ypu)
     print("Computer choose",comp)
     if (you==1) and (comp==3) or (you==2) and (comp==1) or ( you==3) and (comp==2):
          speak("Congratulations you won !")
     elif(you==comp):
          speak("Match tied")
     else:
          speak("You loose")
          
def count()
     t = int(input("Enter time in seconds:"))
     while t:
        min,secs = divmod(t,60)
        timer = '{:02d}:{:02d}'.format(min,sesc)
        print(timer,end="\r")
        t-=1
        print("\n")
        
def guess():
     start=1
     end=1000
     value = radint(start,end)
     print("The computer choose a number between", start, "and",end)
     guess = None
     while guess != value
           text = input("Guess the number :")
           guess = int(text)
           if guess < value :
                speak("The number is higher")
           elif guess > value :
                speak("The number is lower")
     speak("Congralutions!! you won)
         

if __name__=='__main_' :
     wishMe()
     username()
     while True :
          order=takeCommand().lower()

          if 'how are you ' in order 
              speak("I am fine , Thankyou for asking ")
              speak("How are you , Sir ?")
          elif 'fine' in order or 'good' in order:
              speak("it's good to know that you are fine.")
          elif 'who i am ' in order :
              speak('if you can talk then surely you are aa human . ')
          elif 'who are you' in order
              speak('i am your virtual assistant jarvis.')
          elif ' what is your name ' in order :
              speak('my frineds call me jarvis .')
          elif 'open notepad' in order :
              npath="C:\Windows"
              os.startfile(npath)

      
       



    

        
    
                          
