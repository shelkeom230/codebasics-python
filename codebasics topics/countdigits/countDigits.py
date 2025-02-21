# given a number n count the number of digits 

def count_digits(n):
    cnt=0
    while n>0:
        cnt+=1 
        n//=10 
    return cnt 

print(count_digits(101))