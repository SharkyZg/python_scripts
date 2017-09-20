from PIL import Image
import os, sys
from os import listdir
from os.path import isfile, join
import argparse

parser = argparse.ArgumentParser(description='Process PNG imgages in folder.')
parser.add_argument('folder', type=str,
                   help='Path to folder in witch PNG images are located.')

args = parser.parse_args()

FOLDER_PATH = sys.argv[1]

if not os.path.exists(FOLDER_PATH):
    print("Directory named ", FOLDER_PATH, " does not exist, please enter a valid directory name.")
    sys.exit()

onlyfiles = [f for f in listdir(FOLDER_PATH) if isfile(join(FOLDER_PATH, f))]


for filename in onlyfiles:
    only_filename, file_extension = os.path.splitext(filename)
    if file_extension == '.png':
        filename = FOLDER_PATH + filename
        print("Image converted: ", filename)
        im = Image.open(filename)
        rgb_im = im.convert('RGB')
        if not os.path.exists(FOLDER_PATH+"converted"):
            os.makedirs(FOLDER_PATH+"converted")
        rgb_im.save(FOLDER_PATH + "converted/" + only_filename + '.jpg')
print("All .PNG images have been converted, you can find them in: ",join(FOLDER_PATH, "converted/"))
