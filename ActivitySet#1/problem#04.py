# Conditional Execution

hrs = input("Enter Hours:")
h = float(hrs)
time = input("enter the pay per hour:")
t = float(time)
if h <= 40 :
  pay = h*t
else :
  pay = 40*t
  pay = pay + (h-40)*1.5*t  
print(pay)
    