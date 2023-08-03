#Code
import pyttsx3
import speech_recognition as sr
def instruction():
    # initializing speech_recognition
    z = sr.Recognizer()
    # opening physical microphone of computer
    with sr.Microphone() as datasource:
        print('Listening')
        z.pause_threshold = 0.7
        audio = z.listen(datasource)
        try:
            print("Recognizing")
            Query = z.recognize_google(audio)
            print("the query is printed='", Query, "'")
        except Exception as e:
            print(e)
            print("Say that again sir")
            return "None"
    return Query
    

def recite(sound):
    r=pyttsx3.init()
    r.say(sound)
    r.runAndWait()
    

if __name__ == '__main__':
    while True:
        command=instruction()
        if "exit" in command:
            recite("Yes i will exit the page")
            break
        if "insta" in command:
            recite("I will open the insta id for you sir")
            
        if "youtube" in command:
            recite("yes you will be there soon")
        if "hotstar" in command:
            recite("Have a good entertainment")
        if "isro" in command:
            recite("Good choice, It is appreciable")
        if "codepen" in command:
            recite("So you will build something today")
        if "pocketfm" in command:
            recite("it is very good if you listen it at the time of speaking")
            
        
            
        
