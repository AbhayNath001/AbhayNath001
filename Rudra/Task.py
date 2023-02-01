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
import docx                                                 #pip install docx
import pdfreader                                            #pip install pdfreader
import zipfile                                              #pip install zip-files

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
    try:
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
    except:
        Say("Be sure the link is valid and from youtube.")

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
    
def file_reader():
    try:
        Just_Say("enter the file name")
        x = input("enter the file name: ") 
        x = x.replace(".pdf","").replace(".docx","").replace(".txt","")
        try:
            pdfFileObj = open(x+".pdf", 'rb')
            pdfReader = PyPDF2.PdfReader(pdfFileObj)
            Say("ok I read it.")
            zread = ""
            for page in pdfReader.pages:
                zread += page.extract_text() + "\n"
            Say(zread)
        except:
            print("")    
        try:
            doc = docx.Document(x+".docx")
            Say("ok I read it.")
            zread = ""
            for para in doc.paragraphs:
                zread += para.text + "\n"
            Say(zread)
        except:
            print("")
        try:
            z = open(x+".txt", "r")
            Say("ok I read it.")
            zread = z.read()
            Say(zread)
        except:
            print("")
    except:
        Say("unsupported file format or the file is not present")
        
def unzip():
    Just_Say("Enter the zip file name")
    x = input("Enter the zip file name: ")
    x = x.replace(".zip","")
    file_name = x+".zip"
    try:
        Say("start unzipping...")
        with zipfile.ZipFile(file_name, 'r') as zip_ref:
            zip_ref.extractall()
            Say("Successfully unzip")
    except:
        Say("Not found the zip file or anything else")
        
def zip_file(file_path, zip_folder_path):
    Just_Say("Enter the number of files")
    num_files = int(input("Enter the number of files: "))
    file_paths = []
    Just_Say("Enter the file name with extension")
    for i in range(num_files):
        file_path = input("Enter the file name with extension: ")
        file_paths.append(file_path)
    try:
        Just_Say("Enter the zip folder name")
        zip_folder_path = input("Enter the zip folder name: ")
        zip_folder_path = zip_folder_path.replace(".zip","") + ".zip"
        zip_file = zipfile.ZipFile(zip_folder_path, 'w')
        for file_path in file_paths:
            zip_file.write(file_path, os.path.basename(file_path))
        zip_file.close()
    except:
        print("some of the files are not found")
    Say("Successfully zipped")
    
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
                try:
                    parse(pdf_file, word_file, start=0, end=None)
                    Say("Done")
                except:
                    Say("Be sure that you put the proper pdf file.")
            elif 'pdf to txt' in query2:
                x = input("Enter your file name: ")
                x = x.replace('.pdf','')
                pdf_file = x+'.pdf'
                y = input("Give a name of your output file: ")
                y = y.replace('.txt','')
                word_file = y+'.txt'
                try:
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
                except:
                    Say("Be sure that you put the proper pdf file.")    
            elif 'pdf to jpeg' in query2:
                x = input("Enter your file name: ")
                x = x.replace('.pdf','')
                pdf_file = x+'.pdf'
                Say("converting...")
                try:
                    images = convert_from_path(pdf_file)
                    for image in images:
                        image.save(f"{images.index(image)}.jpg", "JPEG")   
                    Say("Done")
                except:
                    Say("Be sure that you put the proper pdf file.")        
            elif 'docx to pdf' in query2:
                docx_file = input("Enter your file name: ")
                docx_file = docx_file.replace('.docx','')
                docx_file = docx_file + ".docx"
                Say("Please wait, it may take some time")
                Say("converting...")
                try:
                    convert(docx_file)  
                    Say("Done")
                except:
                    Say("Be sure that you put the proper docx file.")    
                
    elif "video_downloader" in tag:
        video_downloader()
        
    elif "extract_audio" in tag:
        extract_audio()

    elif "file_reader" in tag:
        file_reader()
        
    elif "unzip" in tag:
        unzip()
        
    elif "zip_file" in tag:
        zip_file("","")    