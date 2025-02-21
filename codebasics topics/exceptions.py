x=input("enter number1: ")
y=input("enter number2: ")
try:
    z=int(x) / int(y)
except ZeroDivisionError as e:
    print('Division by zero: ',e)
    z=None  
except TypeError as e:
    print('type mismatch occured: ',e)
    z=None 
print(f'division is {z}')