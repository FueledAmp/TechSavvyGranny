hashesFile = open('stolen.txt', 'r')
hashesFile = hashesFile.read()
data = hashesFile.split('\n')

def toString(y): 
    s = ""
    for x in range(len(y)):
        s+=str(y[x])
        if x+1 != len(y):
            s+=","
    return s

hashesFileOperation = open("dataset.csv", "a")
for x in range(len(data)):
    data[x] = data[x].split('|')
    a = list(data[x])
    del(a[:2])
    del(a[31:38])
    del(a[34:-2])
    del(a[-2])

    hashesFileOperation.write(toString(a)+'\n')

