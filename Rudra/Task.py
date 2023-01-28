import datetime                                             #pip install DateTime
from Speak import Say, Just_Say
import wikipedia                                            #pip install wikipedia
import qrcode                                               #pip install qrcode
import pyautogui                                            #pip install PyAutoGUI
import speedtest                                            #pip install speedtest-cli
import os                                                   #pip install os-sys
from pdf2docx import parse                                  #pip install pdf2docx   #pip install parse
import PyPDF2                                               #pip install PyPDF2
from pdf2image import convert_from_path                     #pip3 install pdf2image #choco install poppler
from docx2pdf import convert                                #pip install docx2pdf
import urllib.request                                       #pip install urllib3
from pytube import YouTube                                  #pip install pytube
from moviepy.video.io.VideoFileClip import VideoFileClip    #pip install moviepy

def Time():
    hours = datetime.datetime.now().strftime("%H")
    minutes = datetime.datetime.now().strftime(":%M %p")
    hours = int(hours)
    if hours > 12:
        hours = hours-12
        time = str(hours) + minutes
        Say(time)
        
    else:
        time = str(hours) + minutes
        Say(time)
    
def Date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    date = (str(int(date))+"/"+str(int(month))+"/"+str(int(year)))
    Say(date)
    
def Day():
    day = datetime.datetime.now().strftime("%A")
    Say(day)
    
def video_downloader():
    Just_Say("put the link")
    Link = input("put the link: ")
    yt = YouTube(Link)
    Say("Downloading...")
    streams = yt.streams.filter(progressive=True, file_extension='mp4').all()
    stream = streams[0]
    retries = 3
    while retries:
        try:
            stream.download()
            Say("Successfully Downloaded")
            break
        except urllib.error.URLError as e:
            retries -= 1
            if retries == 0:
                Say(f"Error: {e}")
            else:
                Say(f"Retrying... {retries} attempts left") 

def extract_audio():
    Just_Say("Enter the video name")
    v_p = input("Enter the video name: ")
    v_p = v_p.replace(".mp4","").replace(".mp3","").replace("avi","")
    video_path = v_p + '.mp4'
    audio_path = v_p + '.mp3'
    video = VideoFileClip(video_path)
    audio = video.audio
    audio.write_audiofile(audio_path) 
    Say("Done")
    
#All non input functions are here___________________________________________________________________________________________________________________   
    
def NonInputExecution(query):
    query = str(query)
    
    if "time" in query:
        Time()
        
    elif "date" in query:
        Date()
        
    elif "day" in query:
        Day()  
        
    elif "screenshot" in query:
        im = pyautogui.screenshot()
        Say('Done')
        Just_Say("give a name")
        ss = input("give a name: ")
        im.save(ss + ".png")
        Say("successfully save") 

    elif "internet_speed" in query:
        print("Please wait, it may take some time....")
        Just_Say("Please wait, it may take some time")
        wifi = speedtest.Speedtest()
        upload_net = wifi.upload()/1048576
        format_upload_net = "{:.2f}".format(upload_net)
        download_net = wifi.download()/1048576
        format_download_net= "{:.2f}".format(download_net)
        Say("upload speed is: " + str(format_upload_net) + " Mbps")
        Say("download speed is: " + str(format_download_net) + " Mbps")
        
    elif 'clear_browser_history' in query:
            Say("take a second")
            pyautogui.press('super')
            pyautogui.write("chrome")
            pyautogui.press('enter')
            pyautogui.sleep(5)
            pyautogui.press('tab')
            pyautogui.press('enter')
            pyautogui.hotkey('ctrl','h')
            pyautogui.sleep(1)
            pyautogui.press('tab')
            pyautogui.hotkey('ctrl','a')
            pyautogui.sleep(1)
            pyautogui.press('delete')
            pyautogui.sleep(1)
            pyautogui.press('enter')
            pyautogui.hotkey('alt','f4')
            Say("Removed all history")
            
    elif 'close' in query:
        pyautogui.hotkey('alt','f4')
        Say("close")
                
#All input functions are here_______________________________________________________________________________________________________________________                

def InputExecution(tag,query):
    
    if "wikipedia" in tag:
        name = str(query).replace("who is","").replace("about","").replace("what is","").replace("wikipedia","")
        Just_Say("How many lines I read?")
        l_n = input("How many lines I read: ")
        try:
            result = wikipedia.summary(name, sentences=l_n)
            Say(result)
        except:
            Say("No Speakable Data Available!")
        
    elif "qr_code" in tag:
            Just_Say("please put the link what you want!")
            link = input("please put the link what you want: ")
            qr=qrcode.QRCode (version=1,
                              error_correction=qrcode.constants.ERROR_CORRECT_H, 
                              box_size=18, 
                              border=10,)
            qr.add_data(link)
            qr.make(fit=True)
            img=qr.make_image (fill_color="red", back_color="white")
            Just_Say("enter the name of your QR code")
            qr_name = input("enter the name of your QR code: ")    
            img.save(qr_name + ".png")
            Say("Done")  

    elif "file_convert" in tag:
            Say("which type of convertion")
            query2 = input("pdf to docx / pdf to txt / pdf to jpeg / docx to pdf: ")
            if 'pdf to docx' in query2:
                x = input("Enter your file name: ")
                x = x.replace('.pdf','')
                pdf_file = x+'.pdf'
                y = input("Give a name of your output file: ")
                y = y.replace('.docx','')
                word_file = y+'.docx'
                Say("converting...")
                parse(pdf_file, word_file, start=0, end=None)
                Say("Done")
            elif 'pdf to txt' in query2:
                x = input("Enter your file name: ")
                x = x.replace('.pdf','')
                pdf_file = x+'.pdf'
                y = input("Give a name of your output file: ")
                y = y.replace('.txt','')
                word_file = y+'.txt'
                pdfFileObject = open(pdf_file,'rb')
                Say("converting...")
                pdfReader = PyPDF2.PdfFileReader(pdfFileObject)
                print (f"No of Pages: {pdfReader.numPages}")
                pageObject = pdfReader.getPage(0)
                text = pageObject.extractText()
                pdfFileObject.close()
                with open(word_file,"w") as file:
                    file.writelines(text)    
                Say("Done")  
            elif 'pdf to jpeg' in query2:
                x = input("Enter your file name: ")
                x = x.replace('.pdf','')
                pdf_file = x+'.pdf'
                Say("converting...")
                images = convert_from_path(pdf_file)
                for image in images:
                    image.save(f"{images.index(image)}.jpg", "JPEG")   
                Say("Done")  
            elif 'docx to pdf' in query2:
                docx_file = input("Enter your file name: ")
                docx_file = docx_file.replace('.docx','')
                docx_file = docx_file + ".docx"
                Say("Please wait, it may take some time")
                Say("converting...")
                convert(docx_file)  
                Say("Done")
                
    elif "video_downloader" in tag:
        video_downloader()
        
    elif "extract_audio" in tag:
        extract_audio()    