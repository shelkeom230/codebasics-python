nums=[1,2,3,4,5]
even,odd=[],[]
# print evens 
for ele in nums:
    if ele%2==0:
        even.append(ele)
    else:
        odd.append(ele)
print(even,odd)

# using list comprehension
even=[i for i in nums if i%2==0]
odd=[i for i in nums if i%2!=0]
print(even,odd)

import math as m 
squares=[i*i for i in nums]
cubes=[m.pow(i,3) for i in nums]

print(f'squares: {squares} \ncubes: {cubes}')

sq_roots=[m.pow(i,0.5) for i in nums]
print(sq_roots)

# zip function 
cities=["mumbai","new york","paris"]
countries=["india","london","france"]
z=zip(cities,countries)
print(z)

for a in z:
    print(a)
    
d={city:country for city,country in zip(cities,countries)}
print(d)