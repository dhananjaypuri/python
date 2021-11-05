import random

randNumber = random.randint(1,100);
print(randNumber);
number = None;

while(number != randNumber):

    number = int(input("Enter the Number : "));
    if(number == randNumber):
        print("You Guesed it Correct!!!!");
    else:
        print("You guessed it wrong");