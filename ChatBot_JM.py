import webbrowser
import collections
import smtplib

import random

from datetime import datetime

import os

import sys

from weather import Weather

import urllib
import requests


import urllib2

import time

from bs4 import BeautifulSoup

import speech_recognition as sr

from playsound import playsound

import wikipedia

import urllib3

import pyttsx3

from googlesearch import search


engine = pyttsx3.init('dummy')

voices = engine.getProperty('voices')

engine.setProperty('voice', voices[len(voices) - 1].id)


def speak(audio):
    print('Computer: ' + audio)

    engine.say(audio)

    engine.runAndWait()


def greetMe():
    now = datetime.now()

    currentH = int(now.strftime("%H"))

    if currentH >= 0 and currentH < 12:
        speak('Good Morning!')

    if currentH >= 12 and currentH < 18:
        speak('Good Afternoon!')

    if currentH >= 18 and currentH != 0:
        speak('Good Evening!')


greetMe()

speak('Hello Sir, I am your POWER')

speak('How may I help you?')


def myCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:

        print("Listening...")

        r.pause_threshold = 1

        audio = r.listen(source)

    try:

        query = r.recognize_google(audio, language='en-in')

        print('User: ' + query + '\n')



    except sr.UnknownValueError:

        speak('Sorry sir! I didn\'t get that! Try typing the command!')

        query = str(input('Command: '))

    return query


def acess():
    query = myCommand()

    query = query.lower()


if __name__ == '__main__':

    query = myCommand()

    query = query.lower()

    while "hi" in query:

        while True:

            query = myCommand()

            query = query.lower()

            if 'open youtube' in query:

                speak('okay')

                webbrowser.open('www.youtube.com')

                speak("what can i do ")

                flag = 0

                http = urllib3.PoolManager()

                query1 = myCommand()

                url = "https://www.youtube.com/results?search_query=" + query1

                webbrowser.open(url)

                acess()

                speak("pls give acess code")





            elif 'open google' in query:

                speak('okay')

                webbrowser.open('hiwww.google.co.in')

                acess()

                speak("pls give acess code")

            elif 'open gmail' in query:

                speak('okay')

                webbrowser.open('www.gmail.com')

                acess()



            elif 'how are you' in query:

                stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy']

                speak(random.choice(stMsgs))

                acess()

                speak("pls give acess code")

            elif "what is your name" in query:

                speak("I am your assistant,my name is POWER")

                acess()

                speak("pls give acess code")





            elif 'nothing' in query or 'abort' in query or 'stop' in query:

                speak('okay')

                speak('Bye Sir, have a good day.')

                sys.exit()



            elif 'hello' in query:

                speak('Hello Sir')

                acess()



            elif 'bye' in query:

                speak('Bye Sir, have a good day.')

                sys.exit()

            elif 'play music' in query:

                speak("what song i would play")

                song_name = myCommand()

                song_name = song_name.replace(' ', '%20')

                url = 'https://gaana.com/search/{}' + song_name

                webbrowser.open(url)

                speak('Okay, here is your music! Enjoy!')

                acess()

                speak("pls give acess code")

            else:

                query = query

                speak('Searching...')

                results = wikipedia.summary(query, sentences=2)

                speak('Got it.')

                speak('WIKIPEDIA says - ')

                speak(results)

                acess()

                speak("pls give acess code")

        speak('Next Command! Sir!')

    else:

        speak("sorry sir i did get acess code")

