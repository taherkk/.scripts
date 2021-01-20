#!/usr/bin/env python3

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import sys
import os
import shutil
import traceback
import argparse
from os import path

from datetime import date

text_in_image = r'.*\/(.*?)-\d+'
date_today = str(date.today())
workspace_dir = "/home/taher/Workspace/kktjewel/" + date_today
from_dir = workspace_dir + "/org/"
out_dir = workspace_dir + "/edited/"


def update_price(f, percent):
    filename = path.splitext(f)
    try:
        print_name = filename[0].split("-")[0]
        org_price = int(filename[0].split('-')[1])
    except Exception:
        print("\nPrice might not be updated in filename")
        return f

    cost_price = org_price // 4
    selling_price = cost_price + ((cost_price * percent) // 100)
    return print_name + "-" + str(selling_price) + "_edited" + filename[1]


if "edited" not in os.listdir(workspace_dir):
    os.mkdir(out_dir)


def delete_edited_files():
    for root, _, files in os.walk(out_dir):
        for f in files:
            os.remove(os.path.join(root, f))


def main(percent, fs):
    if fs == None:
        fs = os.listdir(from_dir)

    for f in fs:
        f = os.path.basename(f)
        if f.endswith('.jpg'):
            img = Image.open(from_dir+f)
            draw = ImageDraw.Draw(img)
            font = ImageFont.truetype(
                '/usr/share/fonts/ubuntu-font-family-0.83_/Ubuntu-M.ttf', 60)
            draw.text((0, 0), date_today+f.split('-')
                      [0], (255, 255, 255), font=font)
            out_name = update_price(f, percent)
            print(f+" "+out_name)
            continue
            img.save(out_dir+out_name)
    # delete_edited_files()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="write photograph name to the image")
    parser.add_argument("-percent", type=int,
                        help="Provide the profit percentage", default="35")
    parser.add_argument("-f", help="Provide individual files", default=None)
    args = parser.parse_args()
    main(args.percent, args.f)
