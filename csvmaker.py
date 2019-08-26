hashesFileOperation = open("malwareHashes.txt", "r")
hashes = hashesFileOperation.read().split('\n')
hashesFileOperation = open("malwareHashes.csv", "a")
for x in range(len(hashes)):
    hashesFileOperation.write(hashes[x]+",1\n")

#print(hashes[0])
