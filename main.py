
from pytube import YouTube

def main():
    url= input("Url:")
    path= input("Dowloand adress:")
    yt= YouTube(url)
    mp4_files = yt.streams.filter(file_extension="mp4")
    mp4_720p_files= mp4_files.get_by_resolution("720p")
    mp4_720p_files.download(path)

if __name__ == '__main__':
    main()

