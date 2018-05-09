def pay(hours, rate):
    pay = hours * rate
    print (pay)
def overpay(hours, rate):
    overpay = hours * rate + ((hours - 40)*(rate *1.5))
    print (overpay)

try:
    hours = float(input('Enter hours: '))
    rate = float(input('Enter rate: '))
except:
    print ("")
    print ('Please enter numeric value!')
    quit()
if hours > 40:
    pay = hours * rate + (hours - 40) * rate * 0.5
else:
    pay = hours * rate
print ("")
print('Pay: $',pay)
