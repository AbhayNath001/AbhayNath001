import datetime
from Speak import Say
import wikipedia

def Time():
    time = datetime.datetime.now().strftime("%H:%M %p")
    Say(time)
    
def Date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    date = (str(int(date))+"/"+str(int(month))+"/"+str(int(year)))
    Say(date)
    # Say(int(month))
    # Say(int(year))
    
def Day():
    day = datetime.datetime.now().strftime("%A")
    Say(day)
    
    
def NonInputExecution(query):
    query = str(query)
    
    if "time" in query:
        Time()
        
    elif "date" in query:
        Date()
        
    elif "day" in query:
        Day()  

def InputExecution(tag,query):
    
    if "wikipedia" in tag:
        name = str(query).replace("who is","").replace("about","").replace("what is","").replace("wikipedia","")
        result = wikipedia.summary(name)
        Say(result)