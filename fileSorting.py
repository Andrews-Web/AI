import speech_recognition as sr
import os
import wave
import math
import numpy as np
from pydub import AudioSegment
from pydub.playback import play

def tokenize(sent):
    word_bag = []
    word = ""
    for i in sent:
        if i != " ":
            word+=i
        else:
            word_bag.append(word)
            word = ""
    if word != "" or word != " ":
        word_bag.append(word)
        
            
    return word_bag

    

def find_response(sentence):
    wordbag = tokenize(sentence)

    count = 0
    dir = ''
    for i in wordbag:
        path += i+"/"

    if not os.path.exists(f"Responses/{path}") :
        os.makedirs(f"Responses/{path}")
        newfile = open(f"Responses/{path}/response.txt","w")
        new_response = listen()
        newfile.write(new_response)
    else:
        f = open(f"Responses/{path}/response.txt", "r")
        response = tokenize(f.readline)
        for word in response:
            find_word(dir,word)
            sound = AudioSegment.from_wav(f"{dir}/{word}.wav")
            play(sound)

#def save_word(dir):
#    f = open(f"{dir}/similar.txt","w+")

            
def find_word(word,count, audio):  
    bag = ""
    word_dir = ""
    if word[-1] == "s":
        word = word[:len(word)-1]

    for i in word:
        bag+=i.lower()
        word_dir+= bag + "/" 
    if not os.path.exists(f"Allfiles/{word_dir}") :
        os.makedirs(f"Allfiles/{word_dir}")
        #save_word(dir)
        print("Saving")
        save_word_audio(word_dir,word , count,audio)
    if not os.path.exists(f"Allfiles/{word_dir}{word}.wav"):
        save_word_audio(word_dir,word , count,audio)

def find_change_frame(arr,currentFrame):
    inc_frame = arr[currentFrame]+1000
    dec_frame = arr[currentFrame]-1000
    count = 0
    for frame in arr[currentFrame:-1]:
        if frame > 150:
            if frame >= inc_frame:
                #next_frame = len(arr[currentFrame:frame])
                break
            else:
                count+=1
    print(count)
    return count

def save_word_audio(dir, word,Count,audio_file):
    print("Saving audio...")
    #if audio_file == "":
    obj = wave.open('microphone-results.wav', 'rb')
    #else:
    #    obj = wave.open(audio_file, 'rb')


    sample_freq = obj.getframerate()
    n_samples = obj.getnframes()
    t_audio = n_samples/sample_freq
    frames = obj.readframes(obj.getnframes())

    obj.close()

    signal_array = np.frombuffer(frames, dtype=np.int16)
    seconds = 0.8
    num_frames = 0

    
    for j in range(0,math.ceil(t_audio/seconds)):
        current_pos = math.ceil((j*seconds)*sample_freq)
        word_num_frames = find_change_frame(signal_array,current_pos)
        next_pos = math.ceil((j*seconds)+(word_num_frames/sample_freq)*sample_freq)
        if signal_array[current_pos] > 100 and Count == num_frames:
            num_frames += 1
            print(signal_array[current_pos])
            print(num_frames)
            with wave.open(f"Allfiles/{dir}{word}.wav",'wb') as new_word:
                new_word.setnchannels(1) # mono
                new_word.setsampwidth(2)
                new_word.setframerate(sample_freq)
                new_word.writeframes(frames[current_pos:next_pos])
        elif signal_array[current_pos] > 100:
            num_frames += 1
    
    #obj = sr.AudioFile("microphone-results.wav")
    #r = sr.Recognizer()
    #count = 59
    #print("Starting to scrape...")
    #with obj as source: 
    #    audio = r.record(source, offset=count, duration = 1)
    #    count += 0.5
#
    #print("Got Audio now to transcribe it...")
    ## recognize speech using Google Speech Recognition
    #try:
    #    value = r.recognize_google(audio)
    #    if value == word:
    #        with open(f"Allfiles/{dir}{word}.wav",'wb') as new_word:
    #            new_word.write(audio.get_wav_data())
    #except:
    #    print("no audio")

def listen():
    r = sr.Recognizer()
    m = sr.Microphone()

    print("A moment of silence, please...")
    with m as source: 
        r.adjust_for_ambient_noise(source)
    while True:
            
            try:
                print("Say something!")
                with m as source: 
                    audio = r.listen(source, timeout=2)

                
                print("Got it! Now to recognize it...")
                # recognize speech using Google Speech Recognition
                value = r.recognize_google(audio)
                print(value)
                with open("microphone-results.wav", "wb") as f:
                    f.write(audio.get_wav_data())
                return value
            except:
                print("You did not say anything")
                break

def start():   
    sentence = listen()
    wordbag = tokenize(sentence)
    count = 0
    for i in wordbag:
        count += 1
        find_word( i,count, "")























#Copyright 2023, Andrew Owens, All rights reserved.