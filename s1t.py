import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.setProperty('rate',100)
while True:
    data = input("enter your text:")
    if data == "exit":
        engine.say("ok bye")
        engine.runAndWait
        break
    engine.say(data)
    engine.runAndWait()