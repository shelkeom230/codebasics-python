# module is a way to reuse a code written by someone else 

# you can use modules written by someone else for free 

import math as m # math is a module here 

print(m.sqrt(25))

print(m.pow(3,2))

# print(dir(m))

print(m.pi)
print(m.log10(100))
print(m.log10(1000))

# floor and ceiling 
print(m.floor(3.5))
print(m.ceil(3.3))

# calender module 
import calendar

cal=calendar.month(2016,1)
print(cal)

print(calendar.isleap(2016))
print(calendar.isleap(2023))

print(dir(calendar))