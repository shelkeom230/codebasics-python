num1=int(input("pick a number: "))
num2=int(input("pick another number: "))

print("1. add\n 2. subtract \n 3. product \n 4. divide\n5. exit\n")

choice=int(input("enter your choice: "))


if choice==1: print(num1+num2)
elif choice==2: print(num1+num2)
elif choice==3: print(num1*num2)
elif choice==4: print(num1//num2)
elif choice==5: 
    print("exitted")
else: print("invalid choice.")

