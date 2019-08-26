import numpy
from numpy import array

hashesFile = open('stolen.txt', 'r')
hashesFile = hashesFile.read()
hashes = hashesFile.split('\n')

hashesFileOperation = open("dataset.csv", "a")
for x in range(len(hashes)):
    hashes[x] = hashes[x].split('|')
    a = list(hashes[x])
    hashesFileOperation.write(a[0]+','+a[1]+','+a[-1]+'\n')