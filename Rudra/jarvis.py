import random                                                               #pip install random2
import json
import torch                                                                #pip install torch
from brain import NeuralNet
from NeuralNetwork import bag_of_words, tokenize
import datetime                                                             #pip install DateTime

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
with open("intents.json",'r') as json_data:
    intents = json.load(json_data)
FILE = "TrainingData.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data["all_words"]
tags = data["tags"]
model_state = data["model_state"]

model = NeuralNet(input_size,hidden_size,output_size).to(device)
model.load_state_dict(model_state)
model.eval()

name = "Rudra"

from Listen import Listen, Text
from Speak import Say
from Task import NonInputExecution
from Task import InputExecution

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        Say("Good Morning!")

    elif hour>=12 and hour<18:
        Say("Good Afternoon!")

    else:
        Say("Good Evening!")
wishMe()        

def Main():
    sentence = Listen() #Text()
    sentence = tokenize(sentence)
    X = bag_of_words(sentence,all_words)
    X = X.reshape(1,X.shape[0])
    X = torch.from_numpy(X).to(device)
    output = model(X)
    _ , predicted = torch.max(output,dim = 1)
    tag = tags[predicted.item()]
    probs = torch.softmax(output,dim=1)
    prob = probs[0][predicted.item()]
    if prob.item() > 0.50:
        for intent in intents['intents']:
            if tag == intent["tag"]:
                reply = random.choice(intent["responses"])
                
#Get from json file ______________________________________________________________ 
               
                if "bye" in reply:
                    exit()
               
                elif "time" in reply:
                    NonInputExecution(reply)
                    
                elif "date" in reply:
                    NonInputExecution(reply)
                    
                elif "day" in reply:
                    NonInputExecution(reply) 
                    
                elif "task" in reply:
                    NonInputExecution(reply)

                elif "screenshot" in reply:
                    NonInputExecution(reply)

                elif "internet_speed" in reply:
                    NonInputExecution(reply)
                    
                elif "clear_browser_history" in reply:
                    NonInputExecution(reply)
                    
                elif "close" in reply:
                    NonInputExecution(reply)

                elif "wikipedia" in reply:
                    InputExecution(reply,sentence)

                elif "qr_code" in reply:
                    InputExecution(reply,sentence)
                    
                elif "file_convert" in reply:
                    InputExecution(reply,sentence)
                    
                elif "video_downloader" in reply:
                    InputExecution(reply,sentence)

                elif "extract_audio" in reply:
                    InputExecution(reply,sentence)
                    
                elif "file_reader" in reply:
                    InputExecution(reply,sentence)

                elif "unzip" in reply:
                    InputExecution(reply,sentence)
                    
                elif "zip_file" in reply:
                    InputExecution(reply,sentence)  

                elif "Motion_Detect" in reply:
                    InputExecution(reply,sentence) 
                
                else:    
                    Say(reply) 
while True:                
    Main()                
    