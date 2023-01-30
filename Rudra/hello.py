from pytube import YouTube                              #pip install pytube

def video_downloader():
    Link = input("put the link: ")
    yt = YouTube(Link)
    print("Downloading...")
    streams = yt.streams.filter(progressive=True, file_extension='mp4').all()
    stream = streams[0]
    stream.download()
    print("Successfully Downloaded")

video_downloader()