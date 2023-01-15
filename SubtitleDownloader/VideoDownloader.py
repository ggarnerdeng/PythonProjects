import pytube

link = "https://www.youtube.com/watch?v=vZ4kOr38JhY&ab_channel=AndrewHuberman"
yt = pytube.YouTube(link)

# Get all the available streams
streams = yt.streams.filter(progressive=True)

# Find the stream with 720p resolution
stream = streams.filter(resolution='720p').first()

# Download the video
stream.download()


