import subprocess
import os
import time

SCRIPT = """/usr/bin/osascript<<END
tell application "Finder"
set desktop picture to POSIX file "%s"
end tell
END"""
folder = "/Users/suchitvemula/Desktop/Coding/DynamicWallpaper/video/"

frame_rate = 24

def set_desktop_background(filename):
    print(SCRIPT%filename)
    subprocess.Popen(SCRIPT%filename, shell=True)

folder_list = os.listdir(folder)
folder_list.sort()
folder_list.pop(0)

while True:
    for filename in folder_list:
        set_desktop_background(folder+filename)
        time.sleep(1/frame_rate)