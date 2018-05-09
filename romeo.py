def wordsList (list, value):
    for v in list:
        if v == value:
            return True
        return False 

fname = input ("Enter file name: ")         
fhand = open (fname)
wordsList =[]
for line in fhand:
    Words = line.split()
    for x in Words:
        if x in wordsList: continue
        wordsList.append(x)
wordsList.sort()
print (wordsList)