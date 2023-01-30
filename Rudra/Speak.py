import pyttsx3                          #pip install pyttsx3==2.7

#speak

def Say(Text):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate',170)
    print(f"Rudra: {Text}")
    engine.say(text=Text)
    engine.runAndWait()
    print(" ")  
    
def Just_Say(Text):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate',170)
    engine.say(text=Text)
    engine.runAndWait() 
    print(" ")     