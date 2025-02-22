# take age as input from cmd and check whether person can vote or not 
import argparse

parser=argparse.ArgumentParser()
parser.add_argument("age",help="age")
parser.add_argument("name",help="name")
args=parser.parse_args()

age=int(args.age)
print(f'{args.name} age: {args.age}')

if age>18:
    print(f'{args.name} can vote')
else:
    print(f'{args.name} can not vote')