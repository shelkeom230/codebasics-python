# hashset 
mySet=set()

mySet.add(1)
mySet.add(2)
mySet.add(3)
print(mySet)
print(len(mySet))

print(1 in mySet)
print(2 in mySet)
print(3 in mySet)


mySet.remove(2)
print(2 in mySet)

# set comprehension 
n=int(input("enter set size: "))
mySet={i for i in range(n+1)}
print(mySet)