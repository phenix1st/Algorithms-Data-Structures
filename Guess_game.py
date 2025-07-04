import random

secret_number=random.randint(0,10)

guesses=0
guesses_limit=3
while guesses < guesses_limit:
    guesses+=1
    enter=int(input("Enter an integer :"))
    if enter==secret_number:
        print("Congratulations you won")
        break
    else :
        print(f"attempt number {guesses} failed")
else:
    print("Sorry you lost the number was",secret_number)