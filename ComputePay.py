def computepay (hours, rate):
    if hours > 40:
        pay = hours * rate + ((hours -40) * rate * 1.5)
    else:
        pay = hours * rate
    return pay
    
hours = float(input('Enter hours: '))
rate = float(input('Enter rate: '))

total = computepay (hours, rate)
print(total)