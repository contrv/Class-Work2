str = 'X-DSPAM-Confidence:0.8475'
begin = str.find('.')
num = float (str[begin+1:])
print(num)