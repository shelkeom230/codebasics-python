# left skewed binary tree 

class Node:
    def __init__(self,key):
        self.left=None
        self.right=None 
        self.key=key
    

root=Node(1)
root.left=Node(2)
root.left.left=Node(3)