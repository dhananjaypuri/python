#Print factorial of a number

num = int(input("Enter the Number for which you want the factorial : "));

fact = 1;
i = 1;
while(i<=num):
    fact = fact * i;
    i += 1;

print(fact);

a = [20,40,2];
a.sort();

print(a[-1]);