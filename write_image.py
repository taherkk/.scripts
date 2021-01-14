# /usr/bin/env python3

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import sys
import os
from os import path

from datetime import date
text_in_image = r'.*\/(.*?)-\d+'

date_today = str(date.today())

workspace_dir = "/home/taher/Workspace/kktjewel/" + date_today
from_dir = workspace_dir + "/org/"
out_dir = workspace_dir + "/edited/"

if "edited" not in os.listdir(workspace_dir):
    os.mkdir(out_dir)

files = os.listdir(from_dir)

for file in files:
    if file.endswith('.jpg'):
        abs_file_path = from_dir+file
        print(abs_file_path)
        img = Image.open(abs_file_path)
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype(
            '/usr/share/fonts/ubuntu-font-family-0.83_/Ubuntu-M.ttf', 60)
        print(file.split('-'))
        draw.text((0, 0), date_today+file.split('-')
                  [0], (255, 255, 255), font=font)
        img.save(out_dir+path.splitext(file)[0]+"_edited.jpg")
