import speech_recognition as sr         #pip install SpeechRecognition

def Listen():
    r = sr.Recognizer()
    with sr.Microphone(device_index=0) as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,4)
        print("Recognizing...")

    try:       
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}")

    except Exception as e:
        print(e)
        return "None"
    query = str(query)    
    return query.lower()
    
def Text():
    query = input("input: ")
    print(f"You said: {query}")