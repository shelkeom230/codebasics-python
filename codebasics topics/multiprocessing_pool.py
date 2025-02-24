'''
multiprocessing pool 

say, you have 4 cores on your cpu, 

without map reduce computation, 

any 1 core does the task and gives the reuslt and thus, remaning n-1 cores are idle, 
they are not performing any fruitful task

on the other hand,
if you use map reduce computation,
you can divide the task between all the cores, 
they will perform computation and then ,
each one will return the result and after that,
we will merge the result.

map - you divide the work in between units
reduce - you aggreate the result of subtasks back to get the main result.
'''
from multiprocessing import Pool   
 
def f(n):
    return n*n 

if __name__=="__main__":
    arr=[1,2,3,4,5]
    p=Pool(processes=3) # it will only use 3 processes 
    result=p.map(f,arr)
    print(result)
