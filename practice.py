scores={
    'maths':90,'english':50,'physics':97
}

for key in scores.keys():
    print(key)

print("values")

for val in scores.values():
    print(val)

# key,val pairs 
for key,val in scores.items():
    print(key,val)