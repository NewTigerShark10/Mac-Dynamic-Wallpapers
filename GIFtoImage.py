from PIL import Image
import os
from pathlib import Path
import shutil

def gif_to_jpeg(input_gif, output_folder):
    shutil.rmtree(output_folder)
    os.mkdir(output_folder)
    try:
        im = Image.open(input_gif)
    except IOError:
        print("Can't load", input_gif)
        return

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    try:
        while True:
            im2 = im.convert('RGBA')
            im2.load()
            background = Image.new("RGB", im2.size, (255, 255, 255))
            background.paste(im2, mask=im2.split()[3])
            output_file = os.path.join(output_folder, f'frame_{im.tell():03d}.jpg')
            background.save(output_file, 'JPEG', quality=80)
            im.seek(im.tell() + 1)
    except EOFError:
        pass  # end of sequence


input_gif = input('Enter Path To GIF: ')
output_folder = os.path.join(Path.cwd(), 'video', )

gif_to_jpeg(input_gif, output_folder)
