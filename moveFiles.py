import shutil
import os

source = 'C:\Users\Wil\Desktop\Folder A'
dest = 'C:\Users\Wil\Desktop\Folder B'

files = os.listdir(source)

def moveFiles():
    for f in files:
        if f.endswith('.txt'):
            shutil.move(source + '\\' + f,dest)
            print dest + '\\' + f
        else:
            break

moveFiles()
