"""
Create any multithreaded code using for loop for creating multithreads
for i in range(10):
    th = Thread(target=func_name, args=(i, ))
    
print total active threads in multithreaded code using threading.active_count()
"""
import threading,time 

def calFact(n):
    fact=1
    
    for i in range(1,n+1):
        fact*=i 
    print(fact)


def sleepMe(i):
    print("thread %i is sleep"% i)
    time.sleep(5)
    print("thread %i is awake"% i)
threads=[]
for i in range(11):
    th=threading.Thread(target=calFact,args=(i,))
    th.start()
    threads.append(th)
    print("current active thread count: ",threading.active_count())

for th in threads:
    th.join()

print("done")