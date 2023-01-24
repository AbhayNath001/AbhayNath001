import datetime
from Speak import Say

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