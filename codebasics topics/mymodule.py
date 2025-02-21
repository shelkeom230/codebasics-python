# use functions.py as a module in this file 

import functions as f 


"""
 import a specific function 

from functions import calculate_square_area
"""

area=f.calculate_traingle_area(10,12)
print(area)
print(f.calculate_square_area(10))

# import a module from some other directory 

import countdigits.countDigits as c 

digits=c.count_digits(000)
print(f'number of digits is {digits}') 

"""
if the moudle is totally out of dir 

then use sys 

import sys
sys.path.append('your dir path')
"""