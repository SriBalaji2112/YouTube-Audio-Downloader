#python code for YOUTUBE DOWNLOADER

from pytube import YouTube

yt_link = input("Enter your video URL: ")
video = YouTube(yt_link)   #check in Youtube

print("Loading....\n".center(20))
print("Wait for 5 Seconds...".center(20))       # Just as a user friendly
print("Video Title : "+ video.streams[0].title)
print("DOWNLOADING AUDIO...".center(20))

stream = video.streams.filter(only_audio=True).first()
stream.download("youtubeVideo/")

print("\n***SUCCESSFULLY DOWNLOADED***".center(20))


