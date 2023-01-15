import subprocess
import re


link = "https://www.youtube.com/watch?v=vZ4kOr38JhY&ab_channel=AndrewHuberman"
output_str = subprocess.check_output(['youtube-dl', '--skip-download', '--write-sub', '--sub-format', 'vtt', '--sub-lang', 'en', '-o', '%(title)s.vtt', link])
x = output_str.decode().strip()
print(x)
subprocess.call(['youtube-dl', '--skip-download', '--write-sub', '--sub-format', 'vtt', '--sub-lang', 'en', '-o', '1', link])
#####

# Open the input .vtt file
with open('1.en.vtt', 'r') as f:
    vtt_text = f.read()

# Remove the first line (WEBVTT) and any empty lines
vtt_text = re.sub(r'^WEBVTT\n', '', vtt_text, flags=re.MULTILINE)
vtt_text = re.sub(r'\n{2,}', '\n', vtt_text)

# Convert the timestamps from 00:00:00.000 to 00:00:00,000
vtt_text = re.sub(r'(\d\d:\d\d:\d\d)\.(\d{3})', r'\1,\2', vtt_text)

# Add a blank line after each subtitle block
vtt_text = re.sub(r'\n(?=\d\d:\d\d:\d\d,\d{3} -->)', '\n', vtt_text)

# Write the modified text to the output .srt file
with open('output.srt', 'w') as f:
    f.write(vtt_text)