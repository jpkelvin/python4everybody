hrs= float(input("Enter Hours"))
rate=float(input("Enter Rate"))
pay=0
if hrs <40:
    pay=hrs*rate
else:
    hr=hrs-40
    pay=40*rate +hr*1.5*rate
print(pay)
