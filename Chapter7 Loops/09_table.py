#Print table of the a number

num = int(input("Enter the number : "));
i=1;

#With while loop

while(i<=10):
    print(str(num) + " * " + str(i) + " = ", (num*i));
    i+=1;

#With For loop

for i in range(1,11):
    print(f"{num} * {i} = {num*i}");