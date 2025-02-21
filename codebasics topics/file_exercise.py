"""
you are given with a file input.txt with below data 
6,8
7,6
2,8
9,5
9,6

returns the frequency of an element n passed as args """

def countNum(file_path,n):
    count=0
    with open(file_path,"r") as f:
        for line in f:
            tokens=line.split(',')
            count+=count_tokens(tokens,n)
    return count

def count_tokens(tokens,n):
    cnt=0
    for token in tokens:
        if int(token)==n:
            cnt+=1
    return cnt 

"""
change input.txt so that , it contains the sum of numbers in a line 
when program ends """

def sum_numbers(file_path):
    output_lines=[]
    with open(file_path,"r") as f:
        for line in f.readlines():
            token=line.split(',')
            total=sum_total(token)
            output_lines.append(f"sum : {str(total)} | {line}")
    with open(file_path,"w") as f:
        f.write(output_lines)

def sum_total(tokens):
    sum=0
    for token in tokens:
        sum+=int(token)
    return sum 

if __name__=="__main__":
    file_path="D:\\data\\input.txt"
    result=countNum(file_path,6)
    # print(result)
    result2=sum_numbers(file_path)
    print(result2)