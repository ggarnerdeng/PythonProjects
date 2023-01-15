#This module downloads the subtitle of a youtube video link in english, as a .vtt file.

import subprocess
link = "https://www.youtube.com/watch?v=nm1TxQj9IsQ&t=70s"
#link = "https://www.youtube.com/watch?v=4b6bwcWK6GE&ab_channel=AndrewHuberman"

subprocess.call(['youtube-dl', '--skip-download', '--write-sub', '--sub-format', 'vtt', '--sub-lang', 'en', '-o', '%(title)s.vtt', link])