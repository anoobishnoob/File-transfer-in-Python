#author: samme qandil
#Item 63 TTA DRILL
#File transfer


import glob, os, shutil


#this line below will needed to changed for source path to be right
source_dir = 'C:/Users/Student/Desktop/Folder X' #Path where your files are at the moment
dst = 'C:/Users/Student/Desktop/Folder Y' #Path you want to move your files to
files = glob.iglob(os.path.join(source_dir, "*.jpg",)) # if you more formats 
#files = glob.iglob(os.path.join(source_dir, "*.txt",)) # copy and paste one of these lines and change the "*.jpg"
for file in files:
    if os.path.isfile(file):
        shutil.copy2(file, dst)



# this is not really much of a program just want the drills to get done
# The way this works is that depending on what files you want moved it will move
# them if you uncomment and comment out the files = line.
# Maybe I will edit this to have a gui later and on a button press it will move a
# type of file


