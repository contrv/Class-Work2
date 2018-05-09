fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:',fname)
    exit()
alphebet = dict()
for line in fhand:
    line = line.lower()
    for x in line:
        if x not in 'abcdefghijklmnopqrstuvwxyz': continue
        if x not in alphebet:
            alphebet[x] = 1
        else:
            alphebet[x] +=1

# Sort the dictionary by value
lst = list()
for val, key in alphebet.items():
    lst.append( (val,key) )
lst.sort(reverse = True)

for key, val in lst :
    print(key, val)