# File Organizer
# Diar Shakimov
# Saturday June 15, 2024
''' Sorts files and recently downloaded files into designated location
    e.g. screenshots into SC folder, pdfs into PDF folder, and potentially
    key word based sorting  such as :"152" in the name into MATH152 folder, etc.
'''

'''What will be needed: 
** Optional for constantly running variant: how to notice updates to file database**
- Accessing files
- Changing their path




Updated Goal with Real Life Application: 
Problem: Whenever I download lecture slides from my classes I forget to
         put them in their proper folders leading to tons of unsorted files.

Solution: Run a program which will sort the files into existing folders e.g. 
          sec-5.1 into math152 folder with keyword "sec-" with or statement for 
          "152" if I decide to save other files without sec- keyword

'''

import os # OS allows you to create create/manage files/directories.
import shutil # Shutil allows for file copying and removal



path  = input("Enter path: ")
files = os.listdir(path) #os.listdir gives all the files/folders in cwd


for file in files:
    filename, extension = os.path.splitext(file) 
    #print("FILENAME: ", filename, "EXTENSION: ", extension)
    extension = extension[1:] # get rid of . before extension ".png" -> "png"

    if os.path.exists(path + '/' + extension):
        shutil.move(path + '/' + file, path + '/' + extension +'/' + file)
    
    else: 
        os.makedirs(path + '/' + extension)
        shutil.move(path + '/' + file, path + '/' + extension + '/' + file)
