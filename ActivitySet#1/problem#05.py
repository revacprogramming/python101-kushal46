# Functions


def computepay(h,r):
       pay = h*r
       if h > 40 :
         pay = 40*r
         pay = pay + (h-40)*1.5*r  
       return pay

h = float(input("Enter Hours:"))
r = float(input("enter the hourly pay:"))
p = computepay(h,r)
print("Pay", p)