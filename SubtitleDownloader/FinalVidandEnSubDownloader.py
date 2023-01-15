import pytube
import subprocess

#This Link WORKS FOR BOTH. Don't know why.
link = "https://www.youtube.com/watch?v=nm1TxQj9IsQ&t=70s"

#This Link works ONLY FOR THE VIDEO DOWNLOAD. Don't know why.
#link = "https://www.youtube.com/watch?v=rBdhqBGqiMc&ab_channel=AndrewHuberman"

yt = pytube.YouTube(link)

# Get all the available streams
streams = yt.streams.filter(progressive=True)

# Find the stream with 720p resolution
stream = streams.filter(resolution='720p').first()

# Download the video
stream.download()

#subprocess.call(['youtube-dl', '--skip-download', '--write-sub', '--sub-format', 'vtt', '--sub-lang', 'en', '-o', '%(title)s.vtt', link])
subprocess.call(['youtube-dl', '--skip-download', '--write-sub', '--sub-format', 'vtt', '--sub-lang', 'en', '-o', '%(title)s', link])

