# implemnet a calculator using cmd line args 
import argparse

parser=argparse.ArgumentParser()
parser.add_argument("--num1",help="first number") # -- makes args as optional
parser.add_argument("--num2",help="second number")
parser.add_argument("--operation",help="operation", choices=["add","subtract","multiply"]) # choices allows only passing specified args 
args=parser.parse_args()

print(args.num1)
print(args.num2)
print(args.operation)

n1=int(args.num1)
n2=int(args.num2)
result=None 

if args.operation=="add":
    result=n1+n2 
elif args.operation=="subtract":
    result=n1-n2 
elif args.operation=="multiply":
    result=n1*n2 
print(f'result: {result}')