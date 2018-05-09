mlist = []
while True:
    test = input('Enter a number: ')
    if test == "done" :
        break 
    try:
        num = float(test)
    except:
        print('You are Wrong so try again')
        continue
    x = mlist.append(num)
print(mlist)
print('Maximum:',max(mlist))
print('Minimum:',min(mlist))
    
