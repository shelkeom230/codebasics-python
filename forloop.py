# for loops 
for i in range(5):
    print(i)
    
for i in range(2,6):
    print(i)

for i in range(1,11,2):
    print(i)

def reverseString(str):
    l=0
    h=len(str)-1
    str=list(str)
    while l<=h:
        str[l],str[h]=str[h],str[l]
        l+=1
        h-=1
    print(' '.join(str))

# reverseString("omkar")

i=1
while i<=10:
    print(i); i+=1
