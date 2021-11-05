#Tell if a number is prime or not

num = int(input("Enter the Number : "));
prime = True;
for item in range(2,num):
    if(num%item == 0):
        prime = False;
        break;
        
    else:
        prime = True;

if(prime):
    print(f"{num} is a Prime number!!!!!");
else:
    print(f"{num} is not a Prime number!!!!!");