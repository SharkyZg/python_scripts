# Simple python script that converts all PNG files to JPG in one specific folder.
# Script created by Marko Sarkanj

from PIL import Image
import os, sys
from os import listdir
from os.path import isfile, join
import argparse

parser = argparse.ArgumentParser(description='Convert all PNG images to JPG in specified folder.')
parser.add_argument('folder', type=str,
                   help='Path to folder where PNG images are located.')

args = parser.parse_args()

folder_path = sys.argv[1]

if not os.path.exists(folder_path):
    print("Directory named ", folder_path, " does not exist, please enter a valid directory name.")
    sys.exit()

onlyfiles = [f for f in listdir(folder_path) if isfile(join(folder_path, f))]


for filename in onlyfiles:
    only_filename, file_extension = os.path.splitext(filename)
    if file_extension == '.png':
        filename = join(folder_path,filename)
        im = Image.open(filename)
        rgb_im = im.convert('RGB')
        converted_folder_path = join(folder_path,"converted")
        if not os.path.exists(converted_folder_path):
            os.makedirs(converted_folder_path)
        rgb_im.save(join(converted_folder_path, only_filename) + '.jpg')
        print("Image converted: ", filename)
print("All .PNG images have been converted, you can find them in: ",converted_folder_path)
