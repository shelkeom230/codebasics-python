# Hashmaps (aka dict)

myMap={}
myMap['alice']=88
myMap['bob']=77
print(myMap)
print(len(myMap))

# modify values 
myMap['alice']=50
print(myMap['alice'])

print('alice' in myMap)
myMap.pop('alice')
print('alice' in myMap)

myMap={'alice':90,'bob':70}
print(myMap)

# dict comprehension 
myMap={i:i*2 for i in range(3)}
print(myMap)

myMap2={i:i%2 for i in range(5)}
print(myMap2)

# looping through maps 
myMap={"alice":90,"bob":70}
for key in myMap:
    print(key,myMap[key])
    
for val in myMap.values():
    print(val)
    
for key in myMap.keys():
    print(key)

for key,val in myMap.items():
    print(key,val)