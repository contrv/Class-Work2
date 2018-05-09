def chop(c):
    del c[0]
    del c[len(c)-1]
    
    
colors = ['red','orange', 'purple','blue','green','yellow']
print (colors)
chop (colors)
print (colors)

MoreColors = colors.append('tangerine')
print(colors)
print(MoreColors)

def middle(m):
    return m[0:len(m)-1]
    
rest=middle(colors)
print(rest)
print(colors)