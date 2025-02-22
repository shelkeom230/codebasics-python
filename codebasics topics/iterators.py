"""
internally, for loop uses iter to go the next element
"""

a=["hey","bro","you're","awesome"]

for i in a:
    pass
    # print(i) 

# using iterator 
itr=iter(a)
# print(dir(itr))

# print(itr)

# print all elements using iter 
while True:
    try:
        print(next(itr))
    except StopIteration as e:
        break 

# using iter on list, tuple, dict, char and file 
for i in [1,2,3]:
    print(f'list element: {i}')

print()

for i in (4,5,6):
    print(f'tuple element : {i}')
print()

for key in {'name':'omkar','name':'sristik'}:
    print(f'key : {key}')
print()

for char in "123":
    print(f'char : {char}')
print()

for line in open("D:\\data\\input.txt","r"):
    print(f'line :  {line}')

# implement a reverse iterator 
ranks=["first","second","third"]

itr1=reversed(ranks)

while True:
    try:
        print(next(itr1))
    except StopIteration as e:
        break 
