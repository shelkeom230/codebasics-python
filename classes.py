class MyClass:
    # constructor 
    def __init__(self,nums):
        self.nums=nums 
        self.size=len(nums)
    
    # self key word required as param 
    def getLength(self):
        return self.size 
    
    def getDuobleLength(self):
        return self.getLength()*2 

myObj=MyClass([1,2,3])
print(myObj.getLength())
print("double length: ",myObj.getDuobleLength())