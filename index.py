import speech_recognition as sr
import nltk
import pyaudio

def listen():
    r = sr.Recognizer()
    m = sr.Microphone()

    print("A moment of silence, please...")
    with m as source: r.adjust_for_ambient_noise(source)
    while True:
        print("Say something!")
        with m as source: audio = r.listen(source)
        print("Got it! Now to recognize it...")
        # recognize speech using Google Speech Recognition
        try:
            value = r.recognize_google(audio)
            return value
        except:
            print("You did not say anything")
            break


def get_response(sentence):
    wordbag = nltk.word_tokenize("I like cars")#Seperates every word from sententence
    count = 0
    file = ""
    response = ""
    for i in wordbag:
        count = 0
        print(i)
        f = open(f"TXTfiles/{i[0]}.txt", "w+")
        line = f.readlines()
        while f:      
            if len(line) > 0:                                   #runs through the file and finds the word
                if i == line[count].split(",")[0]:
                    file = line[count].split(",")[1]
                    print(file)
                elif i != line[count].split(",")[0]:
                    count = count+1
                if line[count] == line[-1]:
                    print("Enter file location:")
                    file = input()
                    f.write(i+","+file)
        
        try:
            f = open(f"{file}.txt","w+")
            list = []
            define = ""
            fileLine = f.readlines()
            count = 0
            while f:
                list.clear
                list = fileLine[count].split("-")
                if list[1] == i:
                    define = list[2]
                    break
                else:
                    count = count+1
                print("Enter definition:")
                define = input()
            if file == "Greeting":
                response = "Hello\n"
        except:
            f = open(f"{file}.txt", "w")
            print("Enter definition:")
            define = input()
            f.write(i+"-"+define)
            

string = ""
get_response(string)


        

