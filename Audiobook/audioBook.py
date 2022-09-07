import pyttsx3

print("Audio book is ready to listen")
mybook = open("info.txt", "r", encoding= 'utf-8')
mybook_text = mybook.readlines()
engine = pyttsx3.init()
for i in mybook_text:
    engine.say(i)
    engine.runAndWait()
