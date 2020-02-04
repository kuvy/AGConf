import os
import shutil
with open('device.txt') as f:
    myListDevice = [ line.split() for line in f ]
flatListDevice = [item for sublist in myListDevice for item in sublist]
for path in flatListDevice:
    os.mkdir(path)
    shutil.copy("up.atc", path)