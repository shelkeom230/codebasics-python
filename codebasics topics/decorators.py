"""
functions are first class objects in python

i.e they can be treated just like any other variable and you can pass them as args to another functoin and even you can return them as a return value."""
import time as t 
import math as m 

def time_it(func):
    def wrapper(*args,**kwargs):
        start=t.time()
        result=func(*args,**kwargs)
        end=t.time()
        print(func.__name__+" took "+str((end-start)*1000)+" milli seconds")
    return wrapper 

@time_it    
def calculate_square(num):

    result=[]
    
    for ele in num:
        result.append(ele*ele)
    return result

@time_it
def calculate_cube(num):
    result=[]
    
    for ele in num:
        result.append(m.pow(ele,3))
    return result

num=range(1,100000)
out_square=calculate_square(num)
out_cube=calculate_cube(num)