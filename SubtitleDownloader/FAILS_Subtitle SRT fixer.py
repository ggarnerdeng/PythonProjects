import subprocess
import re
import os


link = "https://www.youtube.com/watch?v=vZ4kOr38JhY&ab_channel=AndrewHuberman"
output_str = subprocess.check_output(['youtube-dl', '--skip-download', '--write-sub', '--sub-format', 'vtt', '--sub-lang', 'en', '-o', '%(title)s.vtt', link])
x = output_str.decode().strip()
print(x)
subprocess.call(['youtube-dl', '--skip-download', '--write-sub', '--sub-format', 'vtt', '--sub-lang', 'en', '-o', '1', link])
#####

# specify the input file name
input_file = "1.en.vtt"

# check if the input file exists
if not os.path.exists(input_file):
    print(f"Error: {input_file} not found.")
    exit()

# specify the output file name
output_file = "1.srt"

# open the input and output files
with open(input_file, "r") as input_f, open(output_file, "w") as output_f:
    # counter for the caption number
    caption_num = 1
    # flag to check if current line is the caption content
    is_caption_content = False
    # iterate through the lines in the input file
    for line in input_f:
        # remove the leading and trailing whitespaces
        line = line.strip()
        # check if the line is the start of a caption
        if "-->" in line:
            # write the caption number
            output_f.write(str(caption_num) + "\n")
            # write the start and end times
            output_f.write(line + "\n")
            # set the flag to indicate that the next line is the caption content
            is_caption_content = True
        elif is_caption_content:
            # write the caption content
            output_f.write(line + "\n")
            # increment the caption number
            caption_num += 1
            # reset the flag
            is_caption_content = False
        # ignore other lines
        else:
            continue
        # print a message to confirm completion
    print(f"{input_file} has been converted to {output_file}.")