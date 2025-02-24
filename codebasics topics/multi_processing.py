import multiprocessing
import multiprocessing.process

'''
processes does not share variables in between them 
every process has it's own copy of variables which it maintaines.

threads share data and variables among them
'''
sq_result=[]
def cal_square(nums):
    global sq_result
    for ele in nums:
        print("square: ",str(ele*ele))
        sq_result.append(ele*ele)
    print("inside func : result: ",sq_result)

'''
def cal_cube(nums):
    time.sleep(4)
    for ele in nums:
        print("cube: ",str(ele*ele*ele))
'''

if __name__=="__main__":
    arr=[1,2,3]
    p1=multiprocessing.Process(target=cal_square,args=(arr,))
    p1.start()
    p1.join()
    
    print("inside main: result: ",sq_result)
    print("done")