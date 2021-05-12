def computepay(h,r):
    if h <40:
        pay=h*r
    else:
        hr=h-40
        pay=40*r +hr*1.5*r
    return pay
hrs=float(input("Enter hours: "))
rate=float(input("Enter Rate: "))
p=computepay(hrs,rate)
print("Pay",p)
