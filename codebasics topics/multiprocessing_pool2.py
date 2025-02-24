import time 
from multiprocessing import Pool 

def f(n):
    sum=0
    for x in range(1000):
        sum+=x*x 
    return sum  

if __name__=="__main__":
    t1=time.time()
    p=Pool()
    p.map(f,range(1000000))
    p.close()
    p.join()
    
    print("pool took", time.time()-t1)
    
    
    t2=time.time()
    result=[]
    for ele in range(1000000):
        result.append(f(ele))
    
    print("Normal execution took ",time.time()-t2)