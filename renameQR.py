import os

offset = 150

for filename in os.listdir('.'):
    n1 = filename.split(' ')[2].split('.')[0]
    n2 = int(filename.split(' ')[2].split('.')[0]) + offset
    newfilename = filename.replace(n1, str(n2))
    os.rename(filename, newfilename)
