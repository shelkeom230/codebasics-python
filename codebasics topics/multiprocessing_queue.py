'''
multiprocessing queue 
-- lives in shared memory
-- used for data sharing between processes

Queue module 
-- lives in in-process memory
-- used to share data between threads'''

import multiprocessing,time
def cal_square(nums,q):
    for ele in nums:
        q.put(ele*ele)

if __name__=="__main__":
    nums=[1,2,3]
    
    start=time.time()
    q=multiprocessing.Queue()
    p1=multiprocessing.Process(target=cal_square,args=(nums,q))
    
    p1.start()
    p1.join()
    
    while q.empty() is False:
        print(q.get())
    
    print("total time taken: ",str((time.time()-start)*1000))
    
