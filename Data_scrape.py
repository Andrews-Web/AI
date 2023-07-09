from fileSorting import find_word
from Secrets import Listnotes_API
import requests
import numpy as np
import speech_recognition as sr
import pprint
import nltk
import wave
from os import path
import subprocess

listennotes_Link = "https://listen-api.listennotes.com/api/v2/episodes"

API = {"X-ListenAPI-Key": Listnotes_API}

def get_Transcript(id):
    url = listennotes_Link+"/"+id
    response = requests.request('GET',url, headers=API)
    data = response.json()
    return data['audio']

#f = open("ID.txt", "r")
#arr_id = f.readlines()


#for i in arr_id:
#audio_url = get_Transcript("i")

#print("Downloading...")
#
#doc = requests.get(audio_url)
#with open('mp3_file.mp3', 'wb') as w_Mp3:
#    w_Mp3.write(doc.content)
#
#print("Converting .Mp3 to .Wav")
#    #if path.isfile("mp3_file.mp3") == True:
#with open('mp3_file.mp3', 'rb') as r_Mp3:
#            
#  
# convert mp3 to wav file
#    subprocess.call(['ffmpeg', '-i', 'mp3_file.mp3','ScrapingAudio.wav'])

obj = sr.AudioFile("ScrapingAudio.wav")
wave_obj = wave.open("ScrapingAudio.wav", "rb")



r = sr.Recognizer()
count = 59
while True:
    print("Starting to scrape...")
    with obj as source: 
        audio = r.record(source, offset=count, duration = 10)
        count += 10

    print("Got Audio now to transcribe it...")
    # recognize speech using Google Speech Recognition
    value = r.recognize_google(audio)
    f = open("microphone-results.wav", "wb")
    f.write(audio.get_wav_data())
    print(value)

    wordbag = nltk.word_tokenize(value)
    count = 0
    dir = ""

    for i in wordbag:
        count += 1
        find_word(i,count, "")
    f.close()