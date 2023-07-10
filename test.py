import pyaudio
import wave
import math
import numpy as np
import speech_recognition as sr
import matplotlib.pyplot as plt

"""obj = wave.open('microphone-results.wav', 'r')

sample_freq = obj.getframerate()

n_samples = obj.getnframes()

t_audio = n_samples/sample_freq
num_frames = 0
sample_rate = 16000.0
total = math.ceil(t_audio/0.5)
print(total)

r = sr.Recognizer()
m = sr.Microphone()

with sr.WavFile("microphone-results.wav") as source: 
    for j in range(0,total):
        num_frames += 1
        audio = r.record(source, offset = 0.4, duration=j)
        try:   
            with open(f"new_file{num_frames}.wav", "wb") as f:
                f.write(audio.get_wav_data())
        except:
            pass
        
"""


obj = wave.open('microphone-results.wav', 'rb')

sample_freq = obj.getframerate()
n_samples = obj.getnframes()
frames = obj.readframes(n_samples)
obj.close()

t_audio = n_samples/sample_freq


signal_array = np.frombuffer(frames, dtype=np.int16)
for i in signal_array[0:400]:
    print(i)

times = np.linspace(0, t_audio, num=n_samples)

plt.figure(figsize=(20,5))
plt.plot(times, signal_array)
plt.title("Audio")
plt.ylabel("Frames")
plt.xlabel("Time")
plt.xlim(0, t_audio)
plt.show()


#new_frames = []
#seconds = 1
#num_frames = 0

#T = seconds/[current_frame:next_frame]
#freq = 1/T
#with wave.open(f"new_file.wav",'wb') as new_word:
#        new_word.setnchannels(1) # mono
#        new_word.setsampwidth(2)
#        new_word.setframerate(sample_freq)
#        for i in range(0, math.ceil(t_audio)):
#            new_word.writeframes(frames)
#        new_word.close()

#for j in range(0,math.ceil(t_audio)):
#    current_frame = math.ceil((j*seconds)*sample_freq)
#    next_frame = math.ceil(((j*seconds)+seconds)*sample_freq)
#    if current_frame > 200:
#        num_frames += 1
#        print(num_frames)
#        new_word = wave.open(f"new_file{num_frames}.wav",'wb')
#        new_word.setnchannels(1) # mono
#        new_word.setsampwidth(2)
#        new_word.setframerate(sample_freq)
#        new_word.writeframes(frames[current_frame:next_frame])
#        new_word.close()

"""r = sr.Recognizer()
m = sr.Microphone()

print("A moment of silence, please...")
with m as source: 
    r.adjust_for_ambient_noise(source, duration=0.5)
while True:
        print("Say something!")
        with m as source: 
            audio = r.record(source, duration=5)

        
        print("Got it! Now to recognize it...")
        # recognize speech using Google Speech Recognition
        try:
            value = r.recognize_google(audio)
            print(value)
            with open("microphone-results.wav", "wb") as f:
                f.write(audio.get_wav_data())
        except:
            print("You did not say anything")
            break"""