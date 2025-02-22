'''
implement a remote control iterator which allows you
to watch all the channels 
'''
class RemoteControl:
    def __init__(self):
        self.channels=["HBO","CNN","SONY","STAR","ZEE"]
        self.index=-1
    
    def __iter__(self):
        return self 
    
    def __next__(self):
        self.index+=1
        if self.index==len(self.channels):
            raise StopIteration
        
        return self.channels[self.index]

r=RemoteControl()
itr=iter(r)

"""
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
# print(next(itr)) # raises stopException
"""

# more easy way 
while True:
    try:
        print(next(itr))
    except StopIteration as e:
        break 
    