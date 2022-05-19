# Functions


def computepay():
    hrs = input("Enter Hours:")
    h = float(hrs)
    rate = input("enter the hourly pay:")
    r = float(rate)
    if h <= 40 :
       pay = h*r
    else :
       pay = 40*r
       pay = pay + (h-40)*1.5*r  
    return pay
p = computepay()
print("Pay", p)