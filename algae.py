import os
import glob
from PIL import Image
import shutil
import pathlib
import cv2

#create directories with continous user input, keeps asking if it is enough.


directory = []
#parent_dir = "C:\\Users\\Giant Toddler\\OneDrive\\Documents\\images"
p_dir = "D:\\images"
access = 0o777

def yorn_1():
                ask1=input("Please Enter the Algae filename to make the directory: ")
                filesp = os.path.join(p_dir, ask1)
                #for root, filesp, in os.path.join(parent_dir, ask1):
                file_1 = os.mkdir(filesp, access)
                #f = open(fname, 'r')
                print("directory '$ s' created" % directory)
while True:
                yorn_1()
                answer=input('Continue making directories, yes or no?: ')
                if answer == 'no':
                                print ("Done.")
                                break

#resize photos
#thumbnails

askhey = input("Please Enter the name of the Folder You want Created: ")
inputFolder = 'D:\\images\\dummy_photos'
access = 0o777
folderJ = os.path.join(inputFolder, askhey)
folderLen = len(inputFolder)
file_fun = os.mkdir(folderJ, access)
i = 0
for img in glob.glob(inputFolder + "/*.jpg"):
                image = cv2.imread(img)
                imgResized = cv2.resize(image, (50,50))
                cv2.imwrite("folderJ/image%04i.jpg" %i, imgResized)
                i +=1
                cv2.imshow('image', imgResized)
                cv2.waitKey(5)
cv2.destroyAllWindows()
print("Done.")

#200 x 200 
import os
from PIL import Image
import glob
import sys

path = "D:\\images\\dummy_photos\\"
dirs = os.listdir(path)

def resize_smaller():
                for item in dirs:
                                if os.path.isfile(path+item):
                                                im = Image.open(path+item)
                                                f, e = os.path.splitext(path+item)
                                                imResize = im.resize((200,200), Image.ANTIALIAS)
                                                imResize.save(f + ' _smaller.jpg', 'JPEG', quality=95)
resize_smaller()
print ("Smaller re-sizes are created for all images in the folder.")

#move images named __
import os
from os import path
import shutil

src = "D:\\images\\dummy_photos\\"

dst = "D:\\images\\dummy_photos\\ok1\\"

files = [i for i in os.listdir(src) if i.startswith("sept") and path.isfile(path.join(src, i))]
for f in files:
                shutil.copy(path.join(src, f), dst)
print("Images named sept moved.")
