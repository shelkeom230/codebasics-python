'''
use shared memory to calculate squares
'''

import multiprocessing

def cal_square(nums,result,v):
    v.value=5.67
    for idx,ele in enumerate(nums):
        result[idx]=ele*ele 

if __name__=="__main__":
    
    arr=[1,2,3]
    v=multiprocessing.Value('d',0.0)
    result=multiprocessing.Array('i',3)
    p1=multiprocessing.Process(target=cal_square,args=(arr,result,v))
    p1.start()
    p1.join()

    print(v.value)
    print("done")