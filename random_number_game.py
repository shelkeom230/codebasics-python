import random

randomNumber=random.randint(1,100)

choices=0

while choices<3:
    n=int(input("guess the number between 1 and 100: "))

    if n==randomNumber:
        print(f"You won!!, the number was {randomNumber}")
        break
    elif n>randomNumber:
        print("You guessed tooo high.")
        choices+=1
    elif n<randomNumber:
        print("You guessed tooo low.")
        choices+=1