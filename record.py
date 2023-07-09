import pyaudio
import wave
import math
import numpy as np
import speech_recognition as sr

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
        signal_wave = obj.readframes(n_samples)
signal_array = np.frombuffer(signal_wave, dtype=np.int16)"""


"""obj = wave.open('Recording.wav', 'rb')


sample_freq = obj.getframerate()

n_samples = obj.getnframes()

t_audio = n_samples/sample_freq



frames = obj.readframes(obj.getnframes())

obj.close()


new_frames = []
seconds = 0.4
num_frames = 0


for j in range(0,math.ceil(t_audio/0.2)):
    current_frame = math.ceil((j*0.2)*sample_freq)
    next_frame = math.ceil(((j*seconds)+seconds)*sample_freq)
    if frames[current_frame] > 200:
        num_frames += 1
        print(num_frames)
        new_word = wave.open(f"new_file{num_frames}.wav",'wb')
        new_word.setnchannels(1) # mono
        new_word.setsampwidth(2)
        new_word.setframerate(sample_freq)
        new_word.writeframes(frames[current_frame:next_frame])
        new_word.close()"""

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