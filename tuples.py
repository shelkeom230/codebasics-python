# immutable list 
x=(0,0,2,2)
y=tuple([4,5,6])
z=(42,)
print(x[0])
print(y,z)

# tuple packing and unpacking 

# packing 
t=1,2,3
print(t)
# unpacking 
a,b,c=t 
print(a,b,c)

# ignoring values with _ 
t1=(1,2,3,4)
x,_,_,w=t1 
print(x,w)

print(t1[1]) # 2
print(t1[-1]) # 4 
print(t1[0:3]) # 1,2,3

# tuple has limited methods 
t3=(1,2,3,4,5)
print(t3.count(2))
print(t3.index(3))

# tuples vs list 
# 1. faster than lists (useful for larger datasets)
# 2. immutable, safer to use for constants or keys in dict 
# 3. if no need of modification , then use tuple instead of a list 

co_ordinates=(10.5,64.4) # for fixed data
user_data=("Omkar",22,"engineer") # for structured data 

# tuples can be used as a key in dict , lists can not as they are mutable 
data={(10,20):"Point A",(30,40):"Point B"}
print(data[10,20],data[30,40])

# swapping values 
a,b=10,20
a,b=b,a 
print(a,b)

# memory efficient 
# tuples use less memory than lists 
lst=[1,2,3]
tpl=(1,2,3)
print(lst.__sizeof__())
print(tpl.__sizeof__())

# tuple comprehensions 
# using map and generator expressions 
scores=tuple(map(int,[50,60,50]))
print(scores)

# summary 
#  Use tuples when immutability is required (e.g., fixed configurations, coordinates).

# ✅ Use tuples as dictionary keys when storing composite data.


# ✅ Use tuples for faster, memory-efficient operations.

# 🚫 Don’t use tuples if data needs modification—use a list instead.