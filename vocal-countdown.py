import time
import pyttsx3

def countdown():
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    # Choose a voice that sounds more natural (experiment with different indices)
    natural_voice = voices[0]
    engine.setProperty('voice', natural_voice.id)

    for i in range(10, 0, -1):
        print(i)
        engine.say(str(i))
        engine.runAndWait()
        time.sleep(1)

    print("Blastoff!")
    engine.say("Blastoff!")
    engine.runAndWait()

countdown()