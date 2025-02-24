"""
write a program using multi-threading which calculates squares and cubes of numbers passed as an array in minimal time
"""

import time,threading

def cal_squares(nums):
    print("squares of numbers")
    for ele in nums:
        time.sleep(0.2)
        print('square: ',ele*ele)

def cal_cubes(nums):
    print("cubes of numbers")
    for ele in nums:
        time.sleep(0.2)
        print('cube: ',ele*ele*ele)

arr=[1,2,3,4]

start=time.time()
t1=threading.Thread(target=cal_squares,args=(arr,))
t2=threading.Thread(target=cal_cubes,args=(arr,))

t1.start()
t2.start()

t1.join()
t2.join()

print("done in : "+str((time.time()-start)*1000)+" milli seconds")