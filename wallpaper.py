from appscript import app, mactypes
import os
import time
from pathlib import Path

folder = os.path.join(Path.cwd(), 'video', )

frame_rate = 2

def set_desktop_background(filename):
    app('Finder').desktop_picture.set(mactypes.File(filename))

folder_list = os.listdir(folder)
folder_list.sort()
folder_list.pop(0)

while True:
    for filename in folder_list:
        set_desktop_background(folder+filename)
        time.sleep(1/frame_rate)