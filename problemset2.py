"""def date(in_d,in_m):
    #in_d = d,
    #in_m = m,
    if in_m in range(3,6):
        print("True")
    else:
        print("False")

d = input("Enter day of month : ")
m = input("Enter month : ")
date(d,m)"""

"""def c_interest(p,r,t):
    c = (p*r*t)
    print(c)

principal = input("Enter principal amount:")
eval_p = eval(principal)
time = input("Enter duration:")
eval_t = eval(time)
rate = input("Enter rate:")
eval_r = eval(rate)

c_interest(eval_p,eval_r,eval_t)"""

"""def windchill(t,v):
  if v in range(3,120) :
    wc = (35.74 + 0.6215*t) + (0.4275*t - 35.75)
    print(wc)
  else:
    print("Velocity should be greater than 3 and less than 120")

temp = abs(float(input("Enter temperature: ")))
if  temp <= 50:
    ws = float(input("Enter wind speed: "))
    windchill(temp,ws)
else: print("Temperature should be below 50")"""

"""import math
x = float(input("Enter value of x"))
y = float(input("Enter value of y"))
pc = math.atan2(y,x)
pc = 180 * pc/math.pi

print(pc)"""

"""import math
import random
u = random.uniform(0,1)
v = random.uniform(0,1)
w = (math.sin(2 * math.pi(v))) -(2 * math.In(u)) * (1/2)
print(w)"""


"""x = int(input("Enter an integer: "))
y = int(input("Enter an integer: "))
z = int(input("Enter an integer: "))

if x < y < z or x > y > z:
    print("True")
else:
    print("False")"""

d = int(input("Enter day of month: "))
m = int(input("Enter month(1-12): "))
y = int(input("Enter year: "))

y_0 = y-1
x = y_0 + y_0/4 - y_0/100 + y_0/400
m_0 = m + 12 * ((14 - m)/12) - 2
d_0 = (d + x + (31 * m_0)/12)%7

print(round(d_0))









