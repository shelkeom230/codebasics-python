x=[1,2,3,4]
y=[4,True,"hi"] # ordered
z=[]
name="omkar"

print(len(x),len(y),len(z),len(name))

x.append("hello")
print(x)

x.extend([6,7])
print(x)

print(x.pop())
print(x.pop(0))
print(x[0])

x[0]="omkar"
print(x[0]) # lists are mutable, they can be changed
y=x 
print(x,y)