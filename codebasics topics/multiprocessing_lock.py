'''
when two shared variables or resources should not be accessed conceurrently, 
then we can apply lock on those so that ,
when one variable is currently being used,  
then other should be able to to interrupt it

e.g) home bathroom, 
only 1 person can use bathroom at 1 time
'''
import time,multiprocessing

def deposit(bal,lock):
    
    for i in range(100):
        time.sleep(0.01)
        lock.acquire()
        bal.value=bal.value+1 
        lock.release()
        
def withdraw(bal,lock):
    for i in range(100):
        time.sleep(0.01)
        lock.acquire()
        bal.value=bal.value-1
        lock.release()
        
if __name__=="__main__":
    bal=multiprocessing.Value('i',200)
    lock=multiprocessing.Lock()
    p1=multiprocessing.Process(target=deposit,args=(bal,lock))
    p2=multiprocessing.Process(target=withdraw,args=(bal,lock))
    
    p1.start()        
    p2.start()
    
    p1.join()
    p2.join()
    
    print(bal.value)
            