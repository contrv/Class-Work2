fhand = open('words.txt')
wordCount= dict()
for line in fhand:
    words = line.split()
    for word in words:
        if word not in wordCount:
            wordCount[word] =  1
        else:
            wordCount[word] +=1
print(wordCount)